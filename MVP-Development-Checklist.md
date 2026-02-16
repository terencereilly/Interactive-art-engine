# MVP Development Workplan: “Messages to the Future” (6 Days)

## Day 1 — Models & Admin Setup (Backend: Django)
- [ ] Create Company, CompanyUser, Artwork, Version models
- [ ] Register models in Django admin
- [ ] Seed initial data: “Messages to the Future” artwork, Versions A, B, C
- [ ] Test: Can create/edit all models in admin, versions linked to artwork
- [ ] Commit & push to GitHub

## Day 2 — Artwork Instance & Licensing (Backend)
- [ ] Create ArtworkInstance and License models
- [ ] Build instance creation API/form (select version & duration, auto-generate UUID & license, auto-calculate end_date)
- [ ] Enforce 1 active instance per company, generate unique URL for instance
- [ ] Test: Instance created, UUID assigned, license dates correct, only 1 active instance per company
- [ ] Commit & push to GitHub

## Day 3 — Frontend Integration (React + Three.js)
- [ ] Integrate React + Three.js canvas
- [ ] Set up UI for desktop & mobile (conditional rendering, mobile detection hook)
- [ ] Connect instance UUID from URL to Firestore collection
- [ ] Embed public “Messages to the Future” as iframe for testing
- [ ] Test: Canvas renders, mobile interface works, UUID passed to frontend
- [ ] Commit & push to GitHub

## Day 4 — Message Flow & Firestore (Frontend)
- [ ] Implement message submission flow (write messages to Firestore collection messages_<UUID>)
- [ ] Apply version-based moderation (Free Write vs Filtered Write)
- [ ] Handle expired instance (block submissions)
- [ ] Display messages in real-time on canvas
- [ ] Test: Messages saved in Firestore, moderation rules applied, expired instances block submissions
- [ ] Commit & push to GitHub

## Day 5 — Admin Dashboard & CRUD (Backend + Frontend)
- [ ] Create API: GET /company/artwork-instances (list all instances for company)
- [ ] Admin features: update status (active/disabled), extend license end_date, soft-delete instance (block public access)
- [ ] Dashboard: display total messages & status per instance
- [ ] Test: Admin can update/delete/manage license, deleted instances inaccessible publicly
- [ ] Commit & push to GitHub

## Day 6 — Testing, Demo Data & Deployment (Full-Stack)
- [ ] Seed demo data: 1 Company, 1 Artwork, 3 Versions, 1 ArtworkInstance, 1 License
- [ ] Manual testing: create instance, submit messages, moderation, expiry, CRUD
- [ ] Deploy backend: Heroku/Render/Railway (Django), set up environment variables, database, static files
- [ ] Deploy frontend: Vercel/Netlify (React), connect to backend & Firestore
- [ ] Confirm Firestore collections per instance
- [ ] Test live demo instance
- [ ] Commit & push final code to GitHub

---

### General Testing & Deployment Steps
- [ ] Use GitHub for version control (feature branches, pull requests)
- [ ] Write minimal unit tests for Django models and API endpoints
- [ ] Use Heroku CLI or dashboard for backend deployment
- [ ] Use Vercel/Netlify CLI or dashboard for frontend deployment
- [ ] Document environment variables and setup in README
- [ ] After each deployment, verify:
  - [ ] Backend API is live and reachable
  - [ ] Frontend loads and connects to backend/Firestore
  - [ ] Firestore collections are created per instance
