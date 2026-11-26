from fastapi import FastAPI , HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import settings
from app.database.connection import engine

app = FastAPI(title=settings.APP_NAME)


@app.get("/health/live")
def live():
    return {
        "status" : "ok" , 
        "message":f"{settings.APP_NAME} is running"
    }

@app.get("/health/ready")
def ready():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status" :"ok",
            "database" : "connected"
        }
    except SQLAlchemyError:
        raise HTTPException(status_code=503,detail="Database Unavailable")    
