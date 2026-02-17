from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ArtworkTemplate(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	visual_config = models.JSONField()
	version = models.CharField(max_length=10)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return f"{self.title} ({self.version})"

class ArtworkInstance(models.Model):
	template = models.ForeignKey(ArtworkTemplate, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	version = models.CharField(max_length=10)
	firestore_collection_id = models.CharField(max_length=100, unique=True)
	start_date = models.DateTimeField(default=timezone.now)
	duration_days = models.PositiveIntegerField(default=30)
	is_active = models.BooleanField(default=True)
	def expiration_date(self):
		return self.start_date + timezone.timedelta(days=self.duration_days)
	def is_license_valid(self):
		return self.is_active and timezone.now() < self.expiration_date()
	def __str__(self):
		return f"Instance {self.firestore_collection_id} ({self.version})"
