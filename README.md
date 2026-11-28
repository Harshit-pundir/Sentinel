# SENTINEL 🛡️

### Autonomous Infrastructure Monitoring & Incident Response Platform

SENTINEL is an infrastructure monitoring platform designed to monitor application hosts, collect system metrics, detect unhealthy behaviour, and support structured incident response.

It uses a lightweight monitoring agent to collect host-level metrics such as CPU, memory, and disk usage. The collected data is sent to a FastAPI backend, where it can be validated, stored, analyzed, and used to detect potential infrastructure issues.

The long-term goal is to build a reliable platform that can identify infrastructure problems, provide evidence-based insights, and support safe, controlled self-healing actions.

---

## 🎯 Project Goals

- Monitor infrastructure health through system metrics.
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
| Database Driver | pg8000 |
| Validation | Pydantic |
| Configuration | Pydantic Settings |
| Monitoring Agent | Python, psutil (planned) |
| HTTP Communication | HTTPX |
| Background Jobs | Redis, Celery/RQ (planned) |
| Testing | pytest, HTTPX |
| Deployment | Docker, AWS (planned) |
| AI Integration | Groq (planned) |

## 📌 Current Development Status

**Phase 1 — Backend Core**

SENTINEL is currently under active development. The initial backend foundation and database migration workflow have been implemented.

### Completed

- [x] Initial FastAPI application setup
- [x] Application liveness endpoint
- [x] Database readiness endpoint
- [x] PostgreSQL connection configuration
- [x] Supabase PostgreSQL integration
- [x] SQLAlchemy 2.x declarative base
- [x] Initial Agent model
- [x] Initial Metric model
- [x] Model import verification
- [x] Alembic initialization and configuration
- [x] Initial database migration generated
- [x] Agent and Metric tables created through Alembic
- [x] Migration successfully applied to Supabase
- [x] Alembic migration version tracking
- [x] Initial database migration committed and pushed to GitHub

### Database Tables

| Table | Purpose |
|---|---|
| `agents` | Stores monitoring agent information |
| `metrics` | Stores CPU, memory, and disk usage metrics |
| `alembic_version` | Tracks applied database migrations |

### In Progress / Upcoming

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
- PostgreSQL database or Supabase project
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Harshit-pundir/Sentinel.git
cd Sentinel
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
DATABASE_URL=postgresql+pg8000://USER:PASSWORD@HOST:5432/DATABASE
DEBUG=True
```

Replace the database placeholders with your PostgreSQL or Supabase connection details.

**Important:**
- Never commit your `.env` file.
- Never expose database credentials publicly.
- Keep `.env` in `.gitignore`.
- Use the appropriate database connection details for your environment.

### 5. Apply database migrations

Initialize or update the database schema using Alembic:

```bash
python -m alembic upgrade head
```

Check the currently applied migration:

```bash
python -m alembic current
```

To generate a migration after changing SQLAlchemy models:

```bash
python -m alembic revision --autogenerate -m "Describe your changes"
```

Review generated migration files before applying them.

### 6. Run the application

```bash
python -m uvicorn app.main:app --reload
```

If your local Windows environment has trouble loading the optional `httptools` extension, use:

```bash
python -m uvicorn app.main:app --reload --http h11
```

### 7. Verify the application

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
├── alembic/
│   ├── versions/
│   │   └── 6ad6f03df117_create_agents_and_metrics_tables.py
│   ├── env.py
│   └── script.py.mako
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
├── alembic.ini
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
**Built with:** Python · FastAPI · PostgreSQL · SQLAlchemy · Alembic