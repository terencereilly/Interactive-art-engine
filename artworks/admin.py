from django.contrib import admin
from .models import ArtworkTemplate, ArtworkInstance

@admin.register(ArtworkTemplate)
class ArtworkTemplateAdmin(admin.ModelAdmin):
	list_display = ('title', 'version', 'created_at')

@admin.register(ArtworkInstance)
class ArtworkInstanceAdmin(admin.ModelAdmin):
	list_display = (
		'firestore_collection_id',
		'user',
		'version',
		'is_active',
		'start_date',
		'duration_days'
	)
	search_fields = ('firestore_collection_id', 'user__username')
