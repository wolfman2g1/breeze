from fastapi import FastAPI
import uvicorn
import logging
import logging.config
from  breeze_service.logging_config import LOGGING_CONFIG
from fastapi.middleware.cors import CORSMiddleware
from  breeze_service.settings import config
from breeze_service.api import ping

"Log setup"
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


def configure_app():
    logger.info("Using Config %s", config.ENV)
    app = FastAPI(docs_url="/api/v1/docs")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.include_router(ping.router)
    return app


if __name__ == "__main__":
    logger.info("Starting Breeze")
    app = configure_app()
    uvicorn.run(app, host="0.0.0.0")
