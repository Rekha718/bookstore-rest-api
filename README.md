# 📚 **Bookstore REST API using FastAPI**

A simple yet powerful **Bookstore Management API** built with **FastAPI**, demonstrating CRUD operations, data validation, and clean architecture using **Pydantic**, **SQLAlchemy**, and **SQLite**.

---

## 🚀 **Features**
✅ Create, Read, Update, and Delete (**CRUD**) books  
✅ Input validation using **Pydantic Schemas**  
✅ Error handling with proper **HTTP responses**  
✅ Persistent data storage using **SQLite**  
✅ Modular and clean **folder structure**  
✅ Auto-generated API documentation with **Swagger UI** and **ReDoc**

---

## 🏗️ **Tech Stack**

| Component      | Technology Used     |
|----------------|--------------------|
| **Framework**  | FastAPI            |
| **Database**   | SQLite             |
| **ORM**        | SQLAlchemy         |
| **Validation** | Pydantic           |
| **Language**   | Python 3.10+       |
| **Docs**       | Swagger UI / ReDoc |

---

## 📁 **Folder Structure**

```
bookstore_api/
 ├── main.py                     # Entry point for the FastAPI app
 ├── models.py                   # SQLAlchemy models
 ├── schemas.py                  # Pydantic schemas for validation
 ├── database.py                 # Database connection and session management
 ├── books.db                    # SQLite database file
 ├── README.md                   # Project documentation
 ├── requirements.txt            # Python dependencies for FastAPI project
 ├── .gitignore                  # Ignored files for Git
 └── Bookstore_Project_Report.pdf   # Project report (optional)

```

---

## ⚙️ **Installation & Setup**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Rekha718/bookstore-rest-api
cd bookstore-rest-api
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

> 💡 If you don’t have a `requirements.txt`, generate it using:
```bash
pip freeze > requirements.txt
```


### 3️⃣ Run the Application
```bash
uvicorn main:app --reload
```

---

## 🌐 **API Documentation**

Once the server starts, open in your browser:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧩 **API Endpoints**

| Method | Endpoint | Description |
|--------|-----------|-------------|
| **POST** | `/books/` | Add a new book |
| **GET** | `/books/` | Get all books |
| **GET** | `/books/{book_id}` | Get a book by ID |
| **PUT** | `/books/{book_id}` | Update a book |
| **DELETE** | `/books/{book_id}` | Delete a book |

---

## 🧠 **Example JSON**

### ➕ Add a Book (`POST /books/`)
```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "price": 499.00,
  "quantity": 10
}
```

---

## ✅ **Example Responses**

**201 Created**
```json
{
  "id": 1,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "price": 499.00,
  "quantity": 10
}
```

**404 Not Found**
```json
{
  "detail": "Book not found"
}
```

---

## 🧰 **Error Handling**

- 🚫 Proper validation errors for invalid data types  
- ❌ `404` for missing books  
- ⚠️ `400` for invalid operations  
- 💬 Uses `HTTPException` for clear client feedback  

---

## 🧾 **License**

This project is open-source and available under the **MIT License**.

---

## 👩‍💻 **Author**

**Rekha R**  
📍 *Bangalore, India*  

🔗 **Connect with me:**  
- [💼 LinkedIn](https://www.linkedin.com/in/rekhar1/)  
- [🧠 GitHub](https://github.com/Rekha718?tab=repositories)
