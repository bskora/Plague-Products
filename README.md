# Plague Products

## Running in Codex / container environments

This project defaults to PostgreSQL locally/production unless `DATABASE_URL` is set.

If you need to run in a sandbox that does not have PostgreSQL available, enable SQLite mode:

```bash
export DJANGO_USE_SQLITE=true
python manage.py migrate
python manage.py check
python manage.py runserver 0.0.0.0:8000
```

### Database selection order

1. `DATABASE_URL` (highest priority)
2. SQLite when `DJANGO_USE_SQLITE=true` (or `CODEX_ENV=true`)
3. Local PostgreSQL fallback from `PlagueProducts/settings.py`

This keeps production/local PostgreSQL behavior intact while allowing Codex-safe runs with an isolated `db.sqlite3` file.
