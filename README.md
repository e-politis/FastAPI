# FastAPIcourse

This is a FastAPI project that demonstrates a simple blog application using SQLAlchemy for the ORM and SQLite as the database. The project includes user authentication and CRUD operations for blog posts.

## Project Structure


```md
FastAPIcourse/
├── pycache/
├── blog.db
├── blog/
│ ├── init.py
│ ├── database.py
│ ├── hashing.py
│ ├── main.py
│ ├── models.py
│ ├── oauth2.py
│ ├── repository/
│ ├── routers/
│ │ ├── init.py
│ │ ├── authentication.py
│ │ ├── blog.py
│ │ ├── user.py
│ ├── schemas.py
│ ├── token.py
├── main.py
├── requirements.txt
└── .gitignore
```

## Features

- **User Authentication**: Implemented using OAuth2 and JWT tokens.
- **CRUD Operations for Blogs**:
  - Create a new blog post.
  - Retrieve all blog posts.
  - Retrieve a single blog post by ID.
  - Update a blog post.
  - Delete a blog post.
- **User Management**:
  - Create a new user.
  - Retrieve user details by ID.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/e-politis/FastAPI.git
    cd FastAPI
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```sh
    uvicorn main:app --reload
    ```

5. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000`.

## API Endpoints

- **Authentication**:
  - `POST /login`: Login a user and get a JWT token.

- **User**:
  - `POST /user`: Create a new user.
  - `GET /user/{id}`: Get a user by ID.

- **Blog**:
  - `GET /blog`: Get all blog posts.
  - `POST /blog`: Create a new blog post.

## .gitignore

The `.gitignore` file includes the following:
- `__pycache__/`
- `*.db`
- `.env`


## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)

