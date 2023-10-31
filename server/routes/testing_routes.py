from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
from loguru import logger

from server.processor.testing_processor import check_name

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


class InputJson(BaseModel):
    name: Dict


@api_router.post('/user')
async def user_info(input: InputJson):
    try:
        data = dict(input).get('name')
        result = check_name(data)
        return {"data": result}
    except Exception as error:
        logger.error(f"Error: {error}")
