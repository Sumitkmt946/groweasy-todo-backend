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
```
```bash
# install deps
pip install -r requirements.txt  # agar tumne banaya ho
# ya manually:
pip install fastapi uvicorn "python-jose[cryptography]" passlib[bcrypt] sqlalchemy pydantic[email]
```
```bash
# run server
uvicorn app.main:app --reload

```

Server will run on http://127.0.0.1:8000

Swagger docs: http://127.0.0.1:8000/docs

## Main Features

User signup & login

JWT-based auth

Get logged-in user's profile

Todo CRUD (create, list, update status) per user

API Endpoints (examples) :
###Signup
```bash
curl -X POST http://127.0.0.1:8000/auth/signup ^
  -H "Content-Type: application/json" ^
  -d "{\"name\": \"Sumit\", \"email\": \"sumit@example.com\", \"password\": \"password123\"}"
```
###Login
```bash
curl -X POST http://127.0.0.1:8000/auth/login ^
  -H "Content-Type: application/json" ^
  -d "{\"email\": \"sumit@example.com\", \"password\": \"password123\"}"
```
###Sample response:
```bash
{
  "access_token": "JWT_TOKEN_HERE",
  "token_type": "bearer"
}
```

###Get Todos
```bash
curl -X GET http://127.0.0.1:8000/todos/ ^
  -H "Authorization: Bearer JWT_TOKEN_HERE"
```

###Create Todo
```bash
curl -X POST http://127.0.0.1:8000/todos/ ^
  -H "Authorization: Bearer JWT_TOKEN_HERE" ^
  -H "Content-Type: application/json" ^
  -d "{\"title\": \"First Todo\", \"description\": \"Finish GrowEasy assignment\"}"
```

###Update Todo
```bash
curl -X PATCH http://127.0.0.1:8000/todos/1 ^
  -H "Authorization: Bearer JWT_TOKEN_HERE" ^
  -H "Content-Type: application/json" ^
  -d "{\"completed\": true}"
```



## ⭐ Assignment Requirements
✔ JWT Auth  
✔ CRUD Todos  
✔ Clean API  
✔ README with curl commands  

## 🙌 Author
**Sumit Kumawat**




