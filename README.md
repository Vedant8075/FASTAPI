# 🛒 FastAPI E-Commerce Backend

A RESTful E-Commerce Backend API built with **FastAPI** that provides CRUD operations for managing products. This project demonstrates how to build a scalable backend using FastAPI, Pydantic, and Python.

---

## 🚀 Features

* Create new products
* Retrieve all products
* Retrieve a product by ID
* Update existing products
* Delete products
* Automatic API documentation using Swagger UI
* Data validation using Pydantic
* UUID-based product identification

---

## 🛠️ Tech Stack

* Python 3.11+
* FastAPI
* Uvicorn
* Pydantic
* UUID

---

## 📂 Project Structure

```
ecommerce-backend/
│
├── main.py              # FastAPI application
├── models.py            # Pydantic models
├── database.py          # In-memory data storage
├── crud.py              # CRUD operations
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-ecommerce-backend.git
```

### 2. Navigate to the project

```bash
cd fastapi-ecommerce-backend
```

### 3. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

| Method | Endpoint                 | Description         |
| ------ | ------------------------ | ------------------- |
| GET    | `/products`              | Get all products    |
| GET    | `/products/{product_id}` | Get a product by ID |
| POST   | `/products`              | Add a new product   |
| PUT    | `/products/{product_id}` | Update a product    |
| DELETE | `/products/{product_id}` | Delete a product    |

---

## 📝 Sample Product JSON

```json
{
  "name": "Wireless Mouse",
  "description": "Ergonomic Bluetooth Mouse",
  "price": 999.99,
  "stock": 25,
  "category": "Electronics"
}
```

---

## 📦 Example Requests

### Create Product

```http
POST /products
```

### Get All Products

```http
GET /products
```

### Update Product

```http
PUT /products/{product_id}
```

### Delete Product

```http
DELETE /products/{product_id}
```

---

## ✅ Validation

The API uses **Pydantic** models to validate:

* Product name
* Price
* Stock quantity
* Category
* Description

Invalid requests automatically return appropriate HTTP error responses.

---

## 🧪 Future Improvements

* Database integration (PostgreSQL/MySQL)
* SQLAlchemy ORM
* User authentication with JWT
* Shopping cart functionality
* Order management
* Product image upload
* Pagination and filtering
* Search functionality
* Docker support
* Unit and integration testing

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Built using **FastAPI** and **Python** as a learning project to understand REST API development and CRUD operations.
