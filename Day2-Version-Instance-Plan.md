# Day 2 — Version Selection & Instance Creation

## Objective
Allow artist/admin to create venue-specific instances from the two templates.

---

## PART C — Version Selection & Instance Creation Engine

### 1. Create Version Selection Page
- **Files:** `artworks/views.py`, `artworks/templates/versions.html`, `artworks/urls.py`
- Add a `/versions/` route.
- View lists available artwork templates (A & B) with preview iframes.
- No database writes yet.

### 2. Create Instance Creation Endpoint
- **Files:** `artworks/views.py`, `artworks/forms.py`, `artworks/templates/create_instance.html`, `artworks/urls.py`
- Add `/create-instance/` route (GET: show form, POST: process).
- Form lets user select template/version.

- On POST:
  - Check if user has an active instance:  
    `ArtworkInstance.objects.filter(user=request.user, is_active=True)`
  - If exists, block creation and show message.
  - If not, generate:
    - Unique UUID (use Python’s `uuid` library)
    - Firestore collection name: `messages_<uuid>`
    - License fields: `licenseValid = True`, `expiresAt = start_date + duration_days`
  - Create new `ArtworkInstance` in Django.
  - Redirect to `/artwork/<uuid>/`.

### 2a. Create Artwork Instance Detail Page
- **Files:** `artworks/views.py`, `artworks/templates/artwork_instance.html`, `artworks/urls.py`
- Add `/artwork/<uuid>/` route.
- View fetches the `ArtworkInstance` by uuid.
- **Renders an iframe with the correct template and collectionId in the URL, e.g.:**
  ```html
  <iframe src="https://msg-nu-ashen.vercel.app/?template=1A&collection=messages_<uuid>"></iframe>
  ```
- This ensures the frontend artwork uses the correct Firestore collection for this instance.








### 3. Enforce One Active Instance per User
- In instance creation view, enforce only one active instance per user.
- Show error if user tries to create another.

### 4. Register Instance Creation in Admin
- Ensure new instances appear in Django admin for review.

### 5. Test the Flow
- Test `/versions/` page displays templates and previews.
- Test `/create-instance/` form and POST logic.
- Confirm only one active instance per user.
- Confirm unique Firestore collection ID and URL.

---

## Day 2 Success Criteria
- Admin/artist can create a venue instance from template A or B.
- Unique Firestore collection ID generated.
- Unique URL for each instance works.
- One active instance per venue enforced.

---

**Learning Outcomes:**
- LO1: Django view and form handling
- LO2: Firestore integration
- LO7: User/instance logic and validation
