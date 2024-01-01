# FAST-HTMX

> Strongly inspired from : https://github.com/marty331/fasthtmx


## HTMX ATTRIBUTES

The following HTMX attributes are used in this project:

- hx-get
- hx-post
- hx-trigger
- hx-target
- hx-push-url
- hx-indicator
- hx-swap

## STRUCTURE

- `db` - Database setup
- `models` - Data models
- `schema` - Pydantic models
- `services` - Database services
- `static` - Static files
- `templates` - Contains files for each page and partials for all partial pages that are related to the main page of the directory which it is under.
- `viewmodels` - View models for gathering data for pages and partials.
- `main.py` - Main operational file for running FastAPI.

## How to run

- Create virtual environment
- Activate virtual environment
- Install requirements `make install`
- Run project `make dev`
