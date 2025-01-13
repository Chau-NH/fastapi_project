# Prerequisite
- Python-3.1x

# FastAPI Project
- Run Postgresql server locally
```bash
cd docker
docker compose up -d
```

- Create Virtual evironment
```bash
python3 -m venv myenv
source venv/Script/activate (for Windows)
```

- Install Dependencies
```bash
pip install -r requirements.txt
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

- Generate Secret key
```bash
openssl rand –hex 32
```