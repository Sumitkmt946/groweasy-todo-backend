# GrowEasy Todo API

Simple Todo backend built with **FastAPI + SQLite** for the GrowEasy Full Stack assignment.

## Tech Stack

- FastAPI
- SQLAlchemy + SQLite
- JWT auth (access token)
- Pydantic

## Setup & Run

```bash
# create & activate venv (optional)
python -m venv venv
venv\Scripts\activate   # Windows

# install deps
pip install -r requirements.txt  # agar tumne banaya ho
# ya manually:
pip install fastapi uvicorn "python-jose[cryptography]" passlib[bcrypt] sqlalchemy pydantic[email]

# run server
uvicorn app.main:app --reload



