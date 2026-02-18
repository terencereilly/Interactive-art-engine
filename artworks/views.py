
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .forms import CreateInstanceForm
from .models import ArtworkTemplate, ArtworkInstance
from django.contrib.auth.models import User

# Create your views here.

@login_required
def versions(request):
    return render(request, "versions.html")


@login_required
def create_instance(request):
    error_message = None
    initial = {}
    # Pre-select template if provided in query params
    template_param = request.GET.get("template")
    if template_param in dict(CreateInstanceForm.TEMPLATE_CHOICES):
        initial["template"] = template_param
    if request.method == "POST":
        form = CreateInstanceForm(request.POST)
        if form.is_valid():
            template_version = form.cleaned_data["template"]
            duration_days = form.cleaned_data["duration_days"]
            # Enforce one active instance per user
            existing = ArtworkInstance.objects.filter(user=request.user, is_active=True)
            if existing.exists():
                error_message = "You already have an active instance. Please deactivate it before creating a new one."
            else:
                # Get the template object
                template_obj = ArtworkTemplate.objects.filter(version=template_version).first()
                if not template_obj:
                    error_message = "Selected template does not exist."
                else:
                    # Generate unique Firestore collection ID
                    collection_id = get_random_string(16)
                    instance = ArtworkInstance.objects.create(
                        template=template_obj,
                        user=request.user,
                        version=template_version,
                        firestore_collection_id=collection_id,
                        duration_days=duration_days,
                        is_active=True
                    )
                    return redirect("artwork_instance", uuid=collection_id)
        else:
            error_message = "Please correct the errors below."
    else:
        form = CreateInstanceForm(initial=initial)
    return render(request, "create_instance.html", {"form": form, "error_message": error_message})


# Instance detail view (for iframe page)
@login_required
def artwork_instance(request, uuid):
    instance = get_object_or_404(ArtworkInstance, firestore_collection_id=uuid, user=request.user)
    return render(request, "artwork_instance.html", {"instance": instance})
