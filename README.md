# SENTINEL

Infrastructure monitoring and incident-response platform.

An agent collects host metrics (CPU, memory, disk) and sends them to a FastAPI backend. Rules detect unhealthy behaviour, create incidents with evidence, and an operator can acknowledge and resolve them.

## Status
🚧 In active development (Phase 0: foundation)

## Tech stack
Python, FastAPI, PostgreSQL (Supabase), SQLAlchemy, Alembic, Redis, pytest

## Run locally
    python -m venv .venv
    pip install -r requirements.txt
    uvicorn app.main:app --reload

## Roadmap
- [x] FastAPI app with health endpoint
- [ ] Database connection and migrations
- [ ] Auth and service registry
- [ ] Agent and metric ingestion
- [ ] Alert rules and incidents