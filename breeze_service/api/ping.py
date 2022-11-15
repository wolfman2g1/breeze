from fastapi import APIRouter
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1")

@router.get("/ping")
def pong():
    """ This endpoint will return a JSON object to test that the app is working"""
    return {"ping": "PONG!"}
