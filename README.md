# FastAPI Project

- Run Postgresql server locally
```bash
cd docker
docker compose up -d
```
- Run Migration script
```bash
cd app
alembic upgrade head
```

- Start server
```bash
cd app
uvicorn main:app --reload
```