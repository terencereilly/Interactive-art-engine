from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .forms import CreateInstanceForm
from .models import ArtworkTemplate, ArtworkInstance
from .utils.firestore import create_firestore_instance_collection
from django.contrib.auth.models import User
import json
from django.utils.safestring import mark_safe



# Deactivate instance view
@login_required
def deactivate_instance(request, uuid):
    instance = get_object_or_404(ArtworkInstance, firestore_collection_id=uuid, user=request.user, is_active=True)
    if request.method == "POST":
        instance.is_active = False
        instance.save()
        return redirect("versions")
    return render(request, "deactivate_instance_confirm.html", {"instance": instance})

# Create your views here.


def versions(request):
    version_to_instance = {}
    if request.user.is_authenticated:
        active_instances = ArtworkInstance.objects.filter(user=request.user, is_active=True)
        version_to_instance = {inst.version: inst for inst in active_instances}
    return render(request, "versions.html", {"version_to_instance": version_to_instance})


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
            # Enforce one active instance per user per version
            existing = ArtworkInstance.objects.filter(user=request.user, version=template_version, is_active=True)
            if existing.exists():
                error_message = "You already have an active instance for this artwork version. Please deactivate it before creating a new one."
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
                    # Create Firestore collection and documents
                    create_firestore_instance_collection(collection_id, instance.expiration_date())
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
    # Debug prints for licensing/expiry
    print("[DEBUG] is_license_valid:", instance.is_license_valid())
    print("[DEBUG] expiration_date:", instance.expiration_date())
    print("[DEBUG] start_date:", instance.start_date)
    print("[DEBUG] duration_days:", instance.duration_days)
    print("[DEBUG] is_active:", instance.is_active)

    # Prepare instance data for frontend (JSON serializable)
    instance_data = {
        "firestore_collection_id": f"messages_{instance.firestore_collection_id}",
        "template": instance.template.title,
        "version": instance.version,
        "licenseValid": instance.is_license_valid(),
        "expiresAt": instance.expiration_date().isoformat(),
        "duration_days": instance.duration_days,
        "start_date": instance.start_date.isoformat(),
        "is_active": instance.is_active,
    }
    return render(request, "artwork_instance.html", {
        "instance": instance,
        "instance_data_json": mark_safe(json.dumps(instance_data)),
    })


@login_required
def dashboard(request):
    instances = ArtworkInstance.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'instances': instances})
