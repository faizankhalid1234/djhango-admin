# Django Full Setup Guide

## Tailwind CSS Setup (Production Way)
1. Install: `pip install django-tailwind`
2. Add `tailwind` to `INSTALLED_APPS`.
3. Run:
   - `python manage.py tailwind init theme`
   - `python manage.py tailwind install`
   - `python manage.py tailwind start` (reload watcher)

In this project, Tailwind CDN is already added in `templates/base.html` for instant styling.

## Media File Upload/Render
- `Student.image` uses `ImageField`.
- `MEDIA_URL` and `MEDIA_ROOT` are configured in settings.
- Development serving for media is enabled in `myproject/urls.py`.

## Authentication and Authorization
- Register: `/accounts/register/`
- Login: `/accounts/login/`
- Logout: `/accounts/logout/`
- Protected routes use `login_required`.
- Add/Delete student operations require permissions.

## FBV vs CBV
- FBV add student: `/accounts/students/add-fbv/`
- CBV add student: `/accounts/students/add-cbv/`
- CBV detail: `/accounts/students/<id>/`

## Querying, Filtering, Ordering, Aggregation
- Search by username/email with `Q`.
- Filter by branch.
- Order by username/age ascending or descending.
- Aggregates: total students, average age, branch-wise counts.

## PythonAnywhere Deploy Checklist
1. Push project to GitHub.
2. Create PythonAnywhere account and new web app.
3. Create virtualenv and install dependencies:
   - `pip install django pillow`
4. Set WSGI path to your project.
5. Configure static files:
   - URL: `/static/` -> project static directory
   - URL: `/media/` -> media directory
6. Run migrations:
   - `python manage.py migrate`
7. Reload PythonAnywhere web app.
