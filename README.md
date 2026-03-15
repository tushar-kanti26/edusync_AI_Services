# 🎓 EduSync: AI-Powered Educational Synchronization Platform

<div align="center">

![EduSync Logo](https://img.shields.io/badge/EduSync-FF6B6B?style=for-the-badge&logo=book&logoColor=white)  
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![Pinecone](https://img.shields.io/badge/Pinecone-000000?style=for-the-badge&logo=pine&logoColor=white)](https://www.pinecone.io/)
[![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

**Revolutionizing Education with AI-Driven Insights and Seamless Collaboration** 🚀

*Transform fragmented learning into synchronized success. EduSync harnesses the power of cutting-edge AI to create an intelligent, real-time educational ecosystem.*

</div>

---

## 🌟 What is EduSync?

EduSync is a groundbreaking educational platform that leverages advanced AI technologies to synchronize learning experiences across students, educators, and institutions. By integrating **LangChain** for intelligent language processing, **Pinecone** for vector-based knowledge retrieval, **Redis** for lightning-fast caching, **PostgreSQL** for robust data management, **Docker** for seamless deployment, and **Render** for scalable hosting, EduSync creates a unified hub where knowledge flows freely and efficiently.

Whether you're a student seeking instant answers, a professor managing course materials, or an institution tracking progress, EduSync adapts to your needs with AI-powered precision.

---

## ✨ Key Features

### 🤖 AI-Powered Learning Tools
- **Intelligent Chatbot**: Powered by LangChain, our chatbot provides contextual, conversational learning assistance.
- **Smart Document Analysis**: Extract insights, generate summaries, and create quizzes from uploaded materials using advanced NLP.
- **Vector Search**: Pinecone enables semantic search across vast knowledge bases for instant, relevant information retrieval.

### 📚 Collaborative Learning Environment
- **Real-Time Collaboration**: WebSocket-powered study rooms for live group sessions.
- **Material Sharing**: Secure upload and verification of educational resources.
- **Discussion Forums**: AI-moderated forums with intelligent answer ranking.

### ⚡ Performance & Scalability
- **Redis Caching**: Ultra-fast data retrieval and session management.
- **PostgreSQL Database**: Reliable, ACID-compliant data storage for all educational data.
- **Docker Containerization**: Easy deployment and scaling across environments.
- **Render Hosting**: Cloud-native deployment for global accessibility.

### 🔒 Security & Access Control
- **Role-Based Access Control**: Tailored permissions for students, teachers, and administrators.
- **Data Encryption**: End-to-end encryption for sensitive educational data.
- **Audit Trails**: Comprehensive logging for compliance and security monitoring.

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| 🐍 **Backend** | Python | Core application logic |
| 🦜 **AI Framework** | LangChain | LLM orchestration and chains |
| 🌲 **Vector Database** | Pinecone | Semantic search and embeddings |
| 🔴 **Caching** | Redis | High-performance data caching |
| 🐘 **Database** | PostgreSQL | Relational data storage |
| 🐳 **Containerization** | Docker | Application packaging |
| ☁️ **Hosting** | Render | Cloud deployment platform |

---

## 🚀 Quick Start

### Prerequisites
- 🐳 Docker installed
- 🐍 Python 3.8+
- 🔑 API keys for Pinecone, OpenAI (for LangChain), and Render

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/edusync.git
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

## 📖 Usage

### For Students
1. **Sign up/Login**: Create your account and join your class.
2. **Access Materials**: Browse verified course materials and AI-generated summaries.
3. **Ask Questions**: Use the AI chatbot for instant help or post in discussion forums.
4. **Study Sessions**: Join live study rooms for collaborative learning.

### For Educators
1. **Upload Content**: Share PDFs, videos, and other materials.
2. **AI Tools**: Generate quizzes and infographics from your content.
3. **Monitor Progress**: Track student engagement and performance.
4. **Moderate Discussions**: Verify answers and maintain quality in forums.

### For Administrators
1. **Manage Users**: Control access and roles across the platform.
2. **Analytics**: View comprehensive usage and performance metrics.
3. **System Configuration**: Customize settings for your institution.

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can get involved:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💻 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 🚀 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔄 Open a Pull Request

Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **LangChain** for powering our AI capabilities
- **Pinecone** for vector search excellence
- **Redis** for blazing-fast caching
- **PostgreSQL** for reliable data management
- **Docker** for containerization magic
- **Render** for seamless cloud hosting

---

<div align="center">

**Made with ❤️ for the future of education**

[🌐 Website](https://edusync.render.com) | [📧 Contact](mailto:team@edusync.com) | [🐛 Report Issues](https://github.com/your-username/edusync/issues)

</div>
Our Live Study Room bypasses standard HTTP polling. We built a custom WebSocket `ConnectionManager` that holds open TCP connections in RAM to broadcast live chat to both Web and Mobile clients seamlessly. 
* **The Killer Feature:** When a student closes their app or laptop, the socket drops. Our server catches the `WebSocketDisconnect` event, calculates the exact session duration in seconds, and asynchronously writes their study hours to the database.

### 3. Bulletproof Security
Instead of just basic login, we implemented **Role-Based Access Control (RBAC)** at the endpoint level. If a student maliciously attempts to `PATCH` an answer to mark it as official, the FastAPI gatekeeper intercepts the token, checks the `RoleEnum`, and blocks it with a `403 Forbidden`.

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
git clone [https://github.com/your-repo/edusync-backend.git](https://github.com/tushar-kanti26/edusync_AI_Services.git)
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

Tushar Kanti Sinha


<div align="center">


<i>"Bringing order to academic chaos."</i>
</div>