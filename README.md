# SENTINEL 🛡️

### Autonomous Infrastructure Monitoring & Incident Response Platform

SENTINEL is an infrastructure monitoring platform designed to monitor application hosts, collect system metrics, detect unhealthy behaviour, and support structured incident response.

It uses a lightweight monitoring agent to collect host-level metrics such as CPU, memory, and disk usage. The collected data is sent to a FastAPI backend, where it can be validated, stored, analyzed, and used to detect potential infrastructure issues.

The long-term goal is to build a reliable platform that can identify infrastructure problems, provide evidence-based insights, and support safe, controlled self-healing actions.

---

## 🎯 Project Goals

- Monitor infrastructure health through real-time system metrics.
- Collect CPU, memory, and disk usage through lightweight agents.
- Store and retrieve monitoring data efficiently.
- Detect abnormal behaviour using configurable rules.
- Generate incidents with supporting evidence.
- Provide operators with incident acknowledgement and resolution workflows.
- Gradually introduce safe, controlled self-healing capabilities.

## 🏗️ Architecture

```text
Monitored Host
     |
     v
Monitoring Agent
     |
     | CPU / Memory / Disk Metrics
     v
FastAPI Backend
     |
     v
Data Validation
     |
     v
PostgreSQL Database
     |
     v
Rule Evaluation
     |
     v
Incident Detection
     |
     v
Operator Response
```

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| Database | PostgreSQL (Supabase) |
| ORM | SQLAlchemy 2.x |
| Database Migrations | Alembic |
| Validation | Pydantic |
| Monitoring Agent | Python, psutil |
| HTTP Communication | HTTPX |
| Background Jobs | Redis, Celery/RQ (planned) |
| Testing | pytest, HTTPX |
| Deployment | Docker, AWS (planned) |
| AI Integration | Groq (planned) |

## 📌 Current Development Status

**Phase 1 — Backend Core**

SENTINEL is currently under active development.

### Completed
- [x] Initial FastAPI application setup
- [x] Application health endpoint
- [x] Database readiness endpoint
- [x] PostgreSQL connection configuration
- [x] SQLAlchemy declarative base
- [x] Initial Agent model
- [x] Initial Metric model
- [x] Model import verification

### In Progress / Upcoming
- [ ] Alembic configuration and database migrations
- [ ] Service registry and Service model
- [ ] CRUD APIs
- [ ] Authentication and authorization
- [ ] Agent metric ingestion API
- [ ] Database integration tests
- [ ] Monitoring agent implementation
- [ ] Alert rules and incident management

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.12+
- PostgreSQL database (or Supabase project)
- Git

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd sentinel
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
APP_NAME=Sentinel
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:5432/DATABASE
DEBUG=True
```

Replace the database placeholders with your PostgreSQL connection details.

**Important:** Never commit your `.env` file or expose database credentials publicly.

### 5. Run the application

```bash
python -m uvicorn app.main:app --reload
```

If your local Windows environment has trouble loading the optional `httptools` extension, use:

```bash
python -m uvicorn app.main:app --reload --http h11
```

### 6. Verify the application

Once the server is running, open:

| Endpoint | Purpose |
|---|---|
| `/health/live` | Checks whether the application is running |
| `/health/ready` | Checks whether the database is reachable |
| `/docs` | Interactive Swagger API documentation |

## 🗺️ Development Roadmap

| Phase | Focus | Status |
|---|---|---|
| Phase 1 | Backend Core, Database, APIs, Authentication | 🚧 In Progress |
| Phase 2 | Redis and Background Jobs | ⏳ Planned |
| Phase 3 | Monitoring Agent and Real-time Metrics | ⏳ Planned |
| Phase 4 | Docker and Containerization | ⏳ Planned |
| Phase 5 | CI/CD with GitHub Actions | ⏳ Planned |
| Phase 6 | AWS Deployment | ⏳ Planned |
| Phase 7 | AI-powered Insights and Safe Self-Healing | ⏳ Planned |

## 🔐 Security Principles

SENTINEL aims to follow these principles as the platform evolves:

- Secure agent authentication.
- Least-privilege access.
- Evidence-based incident analysis.
- Allowlisted remediation actions.
- Human approval for sensitive operations.
- Audit logging for important actions.

AI-generated recommendations will not be allowed to execute arbitrary system commands.

## 📂 Project Structure

```text
sentinel/
│
├── app/
│   ├── core/
│   │   └── config.py
│   │
│   ├── database/
│   │   ├── base.py
│   │   └── connection.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   └── metric.py
│   │
│   └── main.py
│
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*The project structure will evolve as new modules are implemented.*

## 🌱 Project Vision

SENTINEL aims to evolve from a basic infrastructure monitoring backend into an intelligent incident-response platform.

The focus is not just on detecting infrastructure problems, but also on understanding their causes, presenting useful evidence, and enabling safe and controlled remediation.

---

**Status:** 🚧 Active Development  
**Current Phase:** Phase 1 — Backend Core  
**Built with:** Python · FastAPI · PostgreSQL · SQLAlchemy