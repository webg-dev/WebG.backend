from fastapi import APIRouter

from .web_page.endpoint import router as web_page_router

api_router = APIRouter()
api_router.include_router(web_page_router)
