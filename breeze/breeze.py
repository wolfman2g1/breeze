from fastapi import FastAPI
import uvicorn
import logging
import logging.config
from fastapi import APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger(__name__)
router = APIRouter()

def configure_app():
    app = FastAPI(docs_url="/api/v1/docs")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials = True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

if __name__ == "__main__":
    logger.info("Starting Breeze")
    app = configure_app()
    uvicorn.run(app,host="0.0.0.0")