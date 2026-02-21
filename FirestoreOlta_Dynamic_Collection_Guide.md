# FirestoreOlta Dynamic Collection Integration

## Purpose
This guide explains how to update your artwork frontend to use a unique Firestore collection for each instance, as provided by the Django backend. This ensures that each instance has its own persistent storage and avoids hardcoded collection names.

## Steps

### 1. FirestoreOlta Initialization
Replace the old initialization with:

```javascript
function getFirestoreCollectionId() {
  const params = new URLSearchParams(window.location.search);
  return params.get("collection") || null;
}

const firestoreCollectionId = getFirestoreCollectionId();
const olta = FirestoreOlta({ collection: firestoreCollectionId });
```

### 2. Message Fetching and Submission
Update your React code to:

```javascript
const [messages, setMessages] = useState([]);

useEffect(() => {
  olta.onUpdate(() => {
    const allMessages = olta.getAll() || [];
    setMessages(allMessages);
  });
  setMessages(olta.getAll() || []);
}, []);





async function handleOltaSubmit(userText, cellId) {
  if (!userText || userText.trim().length === 0) return;
  await olta.create({ text: userText.trim(), cellId });
}
```












### 3. Remove Hardcoded "messages" Parameter
- All calls to `olta.getAll("messages")` and `olta.create("messages", ...)` should be replaced with `olta.getAll()` and `olta.create({...})`.

### 4. Django Template
Ensure your Django template passes the collection ID in the iframe URL:

```html
<iframe
  src="...vercel.app?template={{ instance.version }}&collection={{ instance_data_json.firestore_collection_id }}"
  ...
></iframe>
```

## Result
Each artwork instance now uses its own Firestore collection, enabling robust, scalable, and secure persistent storage for user messages.

---

**Patch Example:**

```diff
// FirestoreOlta initialization
-function getFirestoreCollectionId() {
-  const params = new URLSearchParams(window.location.search)
-  return params.get("collection") || null
-}
-
-const firestoreCollectionId = getFirestoreCollectionId()
-const olta = firestoreCollectionId
-  ? FirestoreOlta({ collection: firestoreCollectionId }) // Persistent Firestore mode
-  : FirestoreOlta() // Ephemeral/local mode (demo)
+function getFirestoreCollectionId() {
+  const params = new URLSearchParams(window.location.search);
+  return params.get("collection") || null;
+}
+
+const firestoreCollectionId = getFirestoreCollectionId();
+const olta = FirestoreOlta({ collection: firestoreCollectionId });

// Message fetching
-olta.onUpdate(() => {
-  const allMessages = olta.getAll("messages") || [];
-  setMessages(allMessages);
-});
-setMessages(olta.getAll("messages") || []);
+olta.onUpdate(() => {
+  const allMessages = olta.getAll() || [];
+  setMessages(allMessages);
+});
+setMessages(olta.getAll() || []);

// Message submission
-async function handleOltaSubmit(userText, cellId) {
-  if (!userText || userText.trim().length === 0) return;
-  await olta.create("messages", { text: userText.trim(), cellId });
-}
+async function handleOltaSubmit(userText, cellId) {
+  if (!userText || userText.trim().length === 0) return;
+  await olta.create({ text: userText.trim(), cellId });
+}
```

---

**This ensures each instance uses its own Firestore collection, as intended.**
