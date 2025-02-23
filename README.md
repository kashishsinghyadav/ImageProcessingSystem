 
## 🚀 Overview
This is an **asynchronous image processing API** built using **FastAPI, Celery, and Redis**. It allows users to upload images, process them asynchronously, and retrieve the processing status.

## 🎯 Features
- **Upload images** and queue them for processing.
- **Asynchronous task execution** using Celery.
- **Track image processing status** via API.
- **Webhook support** for real-time updates.
- **Dockerized** for easy deployment.





## 🔧 Tech Stack
| Component      | Technology  |
|---------------|------------|
| **Backend**   | FastAPI    |
| **Async Tasks** | Celery + Redis |
| **Database**  | PostgreSQL  |
| **Storage**   | Local  |
| **Web Server** | Uvicorn    |

---



## 🛠 Installation & Setup

### **1️⃣ Clone Repository**
```sh
https://github.com/kashishsinghyadav/ImageProcessingSystem
cd ImageProcessingSystem
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Start Redis Server**
```sh
redis-server
```

### **4️⃣ Start Celery Worker**
```sh
celery -A worker.tasks worker --loglevel=info
```

### **5️⃣ Run FastAPI Server**
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🐳 Docker Setup

### **Run with Docker Compose**
```sh
docker-compose up --build
```

---

## 📌 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

---


