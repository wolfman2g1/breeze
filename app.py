from fastapi import FastAPI
import uvicorn
import logging
import logging.config
from breeze.logging_config import LOGGING_CONFIG
from fastapi import APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
#from  breeze.settings import config
from breeze.api import ping

"Log setup"
#logging.config(LOGGING_CONFIG) //TODO fix this error
logger = logging.getLogger(__name__)


def configure_app():
    #logger.info("Using Config %s", config.ENV)
    app = FastAPI(docs_url="/api/v1/docs")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials = True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.include_router(ping.router)
    return app

if __name__ == "__main__":
    logger.info("Starting Breeze")
    app = configure_app()
    uvicorn.run(app,host="0.0.0.0")