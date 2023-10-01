from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from .controllers import router_awesome



app = FastAPI(
    title="Awesome App",
    version="1.0.0",
    description="Basic FastApi app",
    docs_url="/",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=500)
# Add your router imports here
app.include_router(router_awesome, prefix="/v1")