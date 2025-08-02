##  Security Configuration Summary

The following security measures were implemented in `settings.py` to ensure safe production deployment:

- `DEBUG = False` to disable verbose error messages.
- `ALLOWED_HOSTS` restricts allowed domains.
- HTTPS enforced via `SECURE_SSL_REDIRECT`.
- Secure cookies via `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`.
- HSTS enabled for 1 year with subdomains and preload support.
- Headers like `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`, and `SECURE_BROWSER_XSS_FILTER` prevent XSS and clickjacking.

> This config strengthens the application’s defense against XSS, CSRF, clickjacking, and sniffing attacks.

