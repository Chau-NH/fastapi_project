from fastapi import FastAPI
from fastapi_pagination import add_pagination
from routers import company, task, user, auth

app = FastAPI()

app.include_router(company.router)
app.include_router(task.router)
app.include_router(user.router)
app.include_router(auth.router)

add_pagination(app)

@app.get('/')
async def health_check():
    return "API Service is up and running!"