
# Test to Confirm that model methods (expiration_date, is_license_valid) work as expected.
# python manage.py shell
# Then…

from artworks.models import ArtworkInstance

# Get your test instance (replace with the correct ID if needed)
instance = ArtworkInstance.objects.get(firestore_collection_id="ocean-001")

# Check expiration date
print("Expiration date:", instance.expiration_date())

# Check if license is valid
print("Is license valid?", instance.is_license_valid())

# TEST Passed
# Check expiration date
print("Expiration date:", instance.expi>>> # Check expiration date
>>> print("Expiration date:", instance.expiration_date())
Expiration date: 2026-04-03 17:44:14.762676+00:00
>>> 
>>> # Check if license is valid
>>> print("Is license valid?", instance.is_license_valid())
Is license valid? True





# 
# Test to check expiry of license
# 
from artworks.models import ArtworkInstance
from django.utils import timezone

# Get your instance
instance = ArtworkInstance.objects.get(firestore_collection_id="ocean-001")

# Set start_date to 50 days ago (assuming duration_days is 30 or 45)
instance.start_date = timezone.now() - timezone.timedelta(days=50)
instance.save()

# Now test the methods
print("Expiration date:", instance.expiration_date())
print("Is license valid?", instance.is_license_valid())

# Test Passed
# 
# Now test the methods
print("Expiration date:", instance.expiration_da>>> # Now test the methods
>>> print("Expiration date:", instance.expiration_date())
Expiration date: 2026-02-12 18:17:34.742784+00:00
>>> print("Is license valid?", instance.is_license_valid())
Is license valid? False






# 
# Test Firebase (Firestore) reads and writes in your Django project
# 
# python manage.py shell
# Then…

import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()
FIREBASE_CRED_PATH = os.getenv("FIREBASE_CRED_PATH")
if FIREBASE_CRED_PATH and not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CRED_PATH)
    firebase_admin.initialize_app(cred)

firestore_client = firestore.client()

# Write: Add a test document
doc_ref = firestore_client.collection("test_collection").document("test_doc")
doc_ref.set({
    "message": "Hello from Django!",
})

# Read: Fetch the document back
doc = doc_ref.get()
print("Document data:", doc.to_dict())

# 
# TEST PASSED
# 
# Read: Fetch the document back
doc = doc_ref.get()
print("Document data:", doc.to_dict())update_time {
  seconds: 1771353020
  nanos: 376121000
}

>>> 
>>> # Read: Fetch the document back
>>> doc = doc_ref.get()
>>> print("Document data:", doc.to_dict())
Document data: {'message': 'Hello from Django!'}




import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()
FIREBASE_CRED_PATH = os.getenv("FIREBASE_CRED_PATH")
if FIREBASE_CRED_PATH and not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CRED_PATH)
    firebase_admin.initialize_app(cred)

firestore_client = firestore.client()

doc_ref = firestore_client.collection("new_test_collection").document("first_doc")
doc_data = {"message": "This is a new collection!", "user": "tester"}
doc_ref.set(doc_data)