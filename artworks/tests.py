from django.test import TestCase

# Create your tests here
# 
#  FirestoreIntegrationTests
#
# To crete a new colelction and one document in Firestore, then read it back and verify the content.
# 
import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
from django.test import TestCase


#  if I want to run this specific test, I can use the command:
# python manage.py test artworks.FirestoreIntegrationTest.test_firestore_write_and_read
# 
class FirestoreIntegrationTest(TestCase):
   @classmethod
   def setUpClass(cls):
      super().setUpClass()
      load_dotenv()
      FIREBASE_CRED_PATH = os.getenv("FIREBASE_CRED_PATH")
      if FIREBASE_CRED_PATH and not firebase_admin._apps:
         cred = credentials.Certificate(FIREBASE_CRED_PATH)
         firebase_admin.initialize_app(cred)
      cls.firestore_client = firestore.client()

   def test_create_new_collection(self):
      # Create a new collection and add a document
      new_collection = "new_test_collection"
      doc_id = "first_doc"
      doc_ref = self.firestore_client.collection(new_collection).document(doc_id)
      doc_data = {"message": "This is a new collection!", "user": "tester"}
      doc_ref.set(doc_data)

      # Read the document back
      doc = doc_ref.get()
      data = doc.to_dict()
      self.assertIsNotNone(data)
      self.assertEqual(data["message"], "This is a new collection!")
      self.assertEqual(data["user"], "tester")

   def test_firestore_write_and_read(self):
      doc_ref = self.firestore_client.collection("test_collection").document("test_doc")
      test_message = "Hello Terence from Django TestCase!"
      doc_ref.set({"message": test_message})
      doc = doc_ref.get()
      data = doc.to_dict()
      self.assertIsNotNone(data)
      self.assertEqual(data.get("message"), test_message)

   def test_firestore_second_user_message(self):
      # Ensure the first message exists
      doc_ref1 = self.firestore_client.collection("test_collection").document("test_doc")
      doc_ref1.set({"message": "Hello Terence from Django TestCase!"})

      # Add a second message as another user
      doc_ref2 = self.firestore_client.collection("test_collection").document("test_doc_2")
      second_message = "Hello from a second user!"
      doc_ref2.set({"message": second_message, "user": "user2"})

      # Read all messages in the collection
      docs = list(self.firestore_client.collection("test_collection").stream())
      messages = {doc.id: doc.to_dict() for doc in docs}

      self.assertIn("test_doc", messages)
      self.assertIn("test_doc_2", messages)
      self.assertEqual(messages["test_doc_2"]["message"], second_message)
      self.assertEqual(messages["test_doc_2"]["user"], "user2")