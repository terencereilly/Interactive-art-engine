# Deploying Django Backend to Heroku (via Heroku Dashboard)

## 1. Prepare Your Django App for Heroku

- Ensure your code is committed to a GitHub repo (Heroku Dashboard can deploy from GitHub).
- Add a `requirements.txt` (run `pip freeze > requirements.txt` if missing).
- Add a `Procfile` with:
  ```
  web: gunicorn interactive_art_engine.wsgi
  ```
- Ensure `gunicorn` is in your `requirements.txt`.
- Set `ALLOWED_HOSTS` in `settings.py` to include your Heroku app domain (e.g., `['.herokuapp.com']`).
- Set `DEBUG = False` for production.
- Use `dj-database-url` and `whitenoise` for database and static files:
  - Add to `requirements.txt`:
    ```
    dj-database-url
    whitenoise
    ```
  - Update `settings.py` for static files and database config (see below for code snippets).

## 2. Push Your Code to GitHub

- Make sure your latest code is pushed to your GitHub repository.

## 3. Create a New Heroku App via Dashboard

- Go to https://dashboard.heroku.com/
- Click “New” > “Create new app”
- Choose a unique app name and region.

## 4. Connect to GitHub

- In the app dashboard, go to “Deploy” tab.
- Choose “GitHub” as the deployment method.
- Connect your GitHub account and select your repo.

## 5. Configure Environment Variables

- In “Settings” > “Config Vars”, add:
  - `SECRET_KEY` (use a secure value)
  - `DEBUG` = `False`
  - Any other secrets (Firebase, etc.)
  - `ALLOWED_HOSTS` (if needed)
  - `DATABASE_URL` (Heroku sets this automatically for Postgres)

## 6. Set Up Static Files

- In “Settings” > “Buildpacks”, add:
  - Python (should be auto-detected)
- Make sure `STATIC_ROOT` is set in `settings.py` (e.g., `STATIC_ROOT = BASE_DIR / 'staticfiles'`).

## 7. Deploy

- In “Deploy” tab, click “Deploy Branch” (or enable automatic deploys).
- Wait for the build to finish.

## 8. Run Migrations

- In “Resources” or “More” > “Run Console”, open a Heroku shell.
- Run:
  ```
  python manage.py migrate
  python manage.py collectstatic --noinput
  ```

## 9. Test Your App

- Visit your Heroku app URL (e.g., `https://your-app-name.herokuapp.com/`).
- Check admin, login, and artwork instance pages.

---

Let me know if you want code snippets for any of the settings or files!