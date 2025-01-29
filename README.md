# 🥗 FatSecret API Integration with FastAPI

This project integrates the **FatSecret API** using **FastAPI** and **OAuth 2.0 authentication** to search for food items.

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sechiburman/fatsecret-fastapi.git
cd fatsecret-fastapi
```

### 2️⃣ Create a Virtual Environment 
```bash
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Create a .env File
```bash
FATSECRET_CLIENT_ID=your_client_id
FATSECRET_CLIENT_SECRET=your_client_secret
```
### 5️⃣ Run the FastAPI Server
```bash
uvicorn main:app --reload
```

### 🔹 Swagger UI (API Docs)
After starting the server, open:

👉 Swagger UI

Example: http://127.0.0.1:8000/docs
