import os
import firebase_admin
from firebase_admin import credentials, firestore
from django.utils import timezone

# Initialize Firebase Admin SDK (only once)
if not firebase_admin._apps:
    cred = credentials.Certificate(os.environ.get('FIREBASE_CREDENTIALS_PATH'))
    firebase_admin.initialize_app(cred)

db = firestore.client()

def create_firestore_instance_collection(uuid, expires_at):
    """
    Create Firestore collection for artwork instance with license fields.
    Collection name: messages_<uuid>
    Fields:
      - licenseValid: true
      - expiresAt: <timestamp>
    """
    collection_name = f"messages_{uuid}"
    # Store license metadata in a special document
    license_doc = db.collection(collection_name).document("license")
    license_doc.set({
        "licenseValid": True,
        "expiresAt": expires_at.isoformat(),
    })
    return collection_name
