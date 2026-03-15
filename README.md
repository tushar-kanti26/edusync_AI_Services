# 🎓 EduSync: AI-Powered Educational Synchronization Platform

<div align="center">

![EduSync Logo](https://img.shields.io/badge/EduSync-FF6B6B?style=for-the-badge&logo=book&logoColor=white)  
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![Pinecone](https://img.shields.io/badge/Pinecone-000000?style=for-the-badge&logo=pine&logoColor=white)](https://www.pinecone.io/)
[![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Amazon S3](https://img.shields.io/badge/Amazon_S3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white)](https://aws.amazon.com/s3/)
[![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

**Revolutionizing Education with AI-Driven Insights and Seamless Collaboration** 🚀

*Transform fragmented learning into synchronized success. EduSync harnesses the power of cutting-edge AI to create an intelligent, real-time educational ecosystem.*

</div>

---

## 🌟 What is EduSync?

EduSync is a groundbreaking educational platform that leverages advanced AI technologies to synchronize learning experiences across students, educators, and institutions. By integrating **LangChain** for intelligent language processing, **Pinecone** for vector-based knowledge retrieval, **Redis** for lightning-fast caching, **PostgreSQL** for robust data management, **Amazon S3** for scalable storage, **Docker** for seamless deployment, and **Render** for scalable hosting, EduSync creates a unified hub where knowledge flows freely and efficiently.

Whether you're a student seeking instant answers, a professor managing course materials, or an institution tracking progress, EduSync adapts to your needs with AI-powered precision.

---

## ✨ Key Features

### 🤖 AI-Powered Learning Tools
- **Intelligent Chatbot**: Powered by LangChain, our chatbot provides contextual, conversational learning assistance.
- **Smart Document Analysis**: Extract insights, generate summaries, and create quizzes from uploaded materials using advanced NLP.
- **Vector Search**: Pinecone enables semantic search across vast knowledge bases for instant, relevant information retrieval.
- **Intelligent Analyzer**: Extracts past question papers from the material hub, predicts topic-wise importance (high, medium, low) for different subjects, and presents insights with color-coded indicators (red for high, yellow for medium, green for low).


---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| 🐍 **Backend** | Python | Core application logic |
| 🦜 **AI Framework** | LangChain | LLM orchestration and chains |
| 🌲 **Vector Database** | Pinecone | Semantic search and embeddings |
| 🔴 **Caching** | Redis | High-performance data caching |
| 🐘 **Database** | PostgreSQL | Relational data storage |
| ☁️ **Storage** | Amazon S3 | Scalable cloud object storage |
| 🐳 **Containerization** | Docker | Application packaging |
| ☁️ **Hosting** | Render | Cloud deployment platform |

---

## 🚀 Quick Start

### Prerequisites
- 🐳 Docker installed
- 🐍 Python 3.8+
- 🔑 API keys for Pinecone, Gemini (for LangChain), Amazon S3, and Render

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tushar-kanti26/edusync_AI_Services.git
   cd edusync
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and database credentials
   ```

3. **Run with Docker**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Web App: http://localhost:3000
   - API Docs: http://localhost:8000/docs

### Manual Setup (Alternative)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up PostgreSQL and Redis
# Configure your database connections

# Run the application
python app/main.py
```
---

## 🙏 Acknowledgments

- **LangChain** for powering our AI capabilities
- **Pinecone** for vector search excellence
- **Redis** for blazing-fast caching
- **PostgreSQL** for reliable data management
- **Docker** for containerization magic
- **Render** for seamless cloud hosting


---

## 💻 Tech Stack

**Backend (API Engine)**
* FastAPI (Python)
* PostgreSQL
* SQLAlchemy (Async ORM) & Alembic (Migrations)
* Passlib & python-jose (JWT Authentication)
* Uvicorn (ASGI Server)

**AI & RAG Microservice**
* Retrieval-Augmented Generation (RAG) Pipeline
* Vector Database for Semantic Search
* LLM API Integration (Dynamic Summaries, JSON Quiz Generation, Chat)
* External deployment on Render

**External Services**
* Cloudinary (Multipart File Storage)
* Railway (Deployment)

---

## 🛠️ Local Development Setup

Get the backend engine running on your local machine in under 2 minutes.

### Prerequisites
* Python 3.14
* PostgreSQL & redis running locally

### 1. Clone & Initialize
```bash
git clone https://github.com/tushar-kanti26/edusync_AI_Services.git
cd edusync-backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Clone & Initialize
Create a .env file in the root directory and add your credentials:
``` bash
# Database
DATABASE_URL=postgresql+asyncpg://postgres:yourpassword@localhost:5432/edusync

# Security
SECRET_KEY=generate_a_strong_random_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Cloudinary (File Storage)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 3. Database Migrations
Push the database tables to your local PostgreSQL instance:
```bash
python -m alembic upgrade head
```

### 4. Ignite the Server
```bash
uvicorn app.main:app --reload
```

The API is now live at http://127.0.0.1:8000.
Visit http://127.0.0.1:8000/docs for the interactive Swagger UI!



## 🤝 Team Byte Force
This project was architected and developed for DoubleSlash 4.0.

Creator :-Tushar Kanti Sinha


<div align="center">


<i>"Bringing order to academic chaos."</i>
</div>