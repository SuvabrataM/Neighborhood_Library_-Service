Neighborhood Library Service
# Neighborhood Library Service

A complete FastAPI + PostgreSQL based Library Management System with HTML, CSS and JavaScript frontend.

# Features

## Book Management

- Add Books
- Update Books
- Delete Books
- Search Books by:
  - ID
  - Title
  - Author
- View All Books
- Soft Delete Support

---

## Member Management

- Add Members
- Update Members
- Delete Members
- Search Members by:
  - ID
  - Name
  - Phone Number
- View All Members
- Soft Delete Support

---

## Borrow Management

- Borrow Books
- Return Books
- Prevent Borrowing Unavailable Books
- Current Holdings Per Member
- Borrow History Per Member
- Automatic Available Copies Tracking

---

# Technologies Used

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- HTML
- CSS
- JavaScript
- Uvicorn

---

# Project Structure

Neighborhood_Library_-Service/
│
├── app/
│   ├── routes/
│   │   ├── books.py
│   │   ├── members.py
│   │   └── borrow.py
│   │
│   ├── config.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── frontend/
│   ├── index.html
│   ├── books.html
│   ├── members.html
│   ├── borrow.html
│   ├── script_books.js
│   ├── script_members.js
│   ├── script_borrow.js
│   └── style.css
│
├── requirements.txt
└── README.md

# Installation Steps

Step 1 - Clone Repository

git clone <repository_url>
________________________________________
Step 2 - Create Virtual Environment

python -m venv venv
Activate Virtual Environment:
Windows

venv\Scripts\activate
________________________________________
Step 3 - Install Dependencies

pip install -r requirements.txt
________________________________________
Step 4 - Configure Database
Update database credentials inside:

app/config.py
Example:

DATABASE_URL = "postgresql://postgres:password@localhost:5432/library_db"
________________________________________
Step 5 - Run FastAPI Server

uvicorn app.main:app --reload
________________________________________
Access URLs
FastAPI Swagger UI

http://127.0.0.1:8000/docs
Frontend
Open:

frontend/index.html
________________________________________
API Endpoints
Books
Method	Endpoint
POST	/books/
GET	/books/
PUT	/books/{book_id}
GET	/books/search/id/{book_id}
GET	/books/search/title/{title}
GET	/books/search/author/{author}
DELETE	/books/delete/id/{book_id}
DELETE	/books/delete/title/{title}
DELETE	/books/delete/author/{author}
________________________________________
Members
Method	Endpoint
POST	/members/
GET	/members/
PUT	/members/{member_id}
GET	/members/search/id/{member_id}
GET	/members/search/name/{name}
GET	/members/search/phone/{phone}
DELETE	/members/delete/id/{member_id}
DELETE	/members/delete/name/{name}
DELETE	/members/delete/phone/{phone}
________________________________________
Borrow Operations
Method	Endpoint
POST	/borrow/
PUT	/borrow/return/{record_id}
GET	/borrow/member_currentholding/{member_id}
GET	/borrow/history/{member_id}
________________________________________
Future Enhancements
•	JWT Authentication
•	Role Based Access
•	Docker Support
•	React Frontend
•	Deployment on cloud
________________________________________
Author
Developed using FastAPI, PostgreSQL and JavaScript.

---

# 2. requirements.txt

```txt
fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
python-dotenv
________________________________________
4. Git Commands
git init
git add .
git commit -m "Initial Library Management System Commit"
________________________________________
5. Run Project
uvicorn app.main:app --reload
Open Swagger:
http://127.0.0.1:8000/docs
Frontend:
Open index.html directly in browser.
