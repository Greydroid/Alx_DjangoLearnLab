# Security Best Practices Implemented

## settings.py
- `DEBUG = False`: Prevents sensitive debug info from being shown.
- `SECURE_BROWSER_XSS_FILTER`: Helps block reflected XSS attacks.
- `SECURE_CONTENT_TYPE_NOSNIFF`: Prevents MIME-sniffing.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE`: Cookies only over HTTPS.
- `ALLOWED_HOSTS`: Restricts which domains can access the app.

## Templates
- CSRF protection added with `{% csrf_token %}` in all form templates.

## Views
- Used Django ORM (`.filter(...)`) instead of raw SQL.
- Validated user input using Django forms to sanitize inputs.

## Middleware
- Added Content Security Policy using `django-csp` to prevent XSS.

## Manual Tests
- Attempted CSRF attack: blocked ✅
- Input fields escaped scripts: ✅

