# 🛡️ Cyber Fraud Detection System

A web-based **Cyber Fraud Detection System** designed to help identify and assess potentially fraudulent activities using a modern full-stack architecture.

The project combines a **Django frontend**, **FastAPI backend**, **SQLite database**, and **Docker** for containerized deployment.

---

## 🚀 Features

- 🔍 Cyber fraud detection and analysis
- 📊 Risk assessment of reported transactions/incidents
- 🌐 Django-based web interface
- ⚡ FastAPI backend for REST APIs
- 🗄️ SQLite database integration
- 🐳 Dockerized frontend and backend
- 🔗 REST API communication between frontend and backend
- 📱 Responsive web interface
- 📋 Fraud report management

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │      User           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Django Frontend   │
                    │      Port 8000      │
                    └──────────┬──────────┘
                               │
                         REST API
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FastAPI Backend   │
                    │      Port 8000      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   SQLite Database   │
                    └─────────────────────┘
```

---

## 📁 Project Structure

```text
cyber-fraud-detection/
│
├── Backend/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── Dockerfile
│
├── Frontend/
│   ├── config/
│   ├── my_app/
│   ├── manage.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

### Frontend
- Python
- Django
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- SQLAlchemy
- REST API

### Database
- SQLite

### Deployment & DevOps
- Docker
- Docker Compose

---

## ⚙️ Getting Started

### Prerequisites

Make sure you have the following installed:

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)

---

## 🐳 Running with Docker

Clone the repository:

```bash
git clone https://github.com/ashwinsiby029/cyber-fraud-detection.git
```

Navigate into the project:

```bash
cd cyber-fraud-detection
```

Build and start the containers:

```bash
docker compose up --build
```

To run the containers in the background:

```bash
docker compose up -d --build
```

Check running containers:

```bash
docker ps
```

To stop the application:

```bash
docker compose down
```

---

## 🌐 Accessing the Application

Once the containers are running, open the application in your browser:

```text
http://localhost:8000
```

The FastAPI API documentation can be accessed through:

```text
http://localhost:8000/docs
```

> The exact port may vary depending on the configuration in `docker-compose.yml`.

---

## 🔌 API

The backend is built using **FastAPI** and provides RESTful endpoints for communication with the frontend.

FastAPI automatically provides interactive API documentation through Swagger UI.

```text
/docs
```

You can use the Swagger interface to:

- View available endpoints
- Send API requests
- Test request parameters
- Inspect API responses

---

## 🗄️ Database

The project uses **SQLite** for data storage.

The backend uses SQLAlchemy to interact with the database.

The database layer is responsible for storing and retrieving application data related to fraud reports.

---

## 🔐 Security Considerations

This project is intended primarily for **educational and demonstration purposes**.

Before deploying it to production, consider implementing:

- Authentication and authorization
- HTTPS
- Input validation
- Secure secret management
- Rate limiting
- Proper CORS configuration
- Production-grade database
- Logging and monitoring
- Secure API authentication
- Environment variables for sensitive configuration

**Never commit passwords, API keys, tokens, or production secrets to GitHub.**

---

## 🧪 Development

To make changes to the project:

```bash
git checkout -b feature/your-feature
```

After making changes:

```bash
git add .
git commit -m "Add your feature"
git push origin feature/your-feature
```

---

## 📌 Future Improvements

Possible future enhancements include:

- 🤖 Machine-learning-based fraud classification
- 📈 Advanced fraud analytics dashboard
- 🔔 Real-time fraud alerts
- 👤 User authentication and role management
- 🧠 Fraud pattern recognition
- 📊 Interactive data visualization
- 🌍 IP and geolocation-based analysis
- ☁️ AWS deployment
- 🔐 Improved API security
- 📝 Automated fraud report generation

---

## 👨‍💻 Author

**Ashwin Siby**

Bachelor of Computer Applications graduate with an interest in **Cybersecurity, Ethical Hacking, Network Security, and Software Development**.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational and learning purposes.
