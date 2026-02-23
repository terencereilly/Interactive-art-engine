
from django.utils import timezone
from interactive_art_engine.settings import get_firestore_client

def create_firestore_instance_collection(uuid, expires_at):
    """
    Create Firestore collection for artwork instance with license fields.
    Collection name: messages_<uuid>
    Fields:
      - licenseValid: true
      - expiresAt: <timestamp>
    """
    db = get_firestore_client()
    collection_name = f"messages_{uuid}"
    # Store license metadata in a special document
    license_doc = db.collection(collection_name).document("license")
    license_doc.set({
        "licenseValid": True,
        "expiresAt": expires_at,
    })
    # Create a dummy document to ensure collection exists for reads
    db.collection(collection_name).document("init").set({"init": True})
    return collection_name
