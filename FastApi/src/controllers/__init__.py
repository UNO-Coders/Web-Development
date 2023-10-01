from fastapi import APIRouter

router_awesome = APIRouter(prefix="/awesome")

from .route import *