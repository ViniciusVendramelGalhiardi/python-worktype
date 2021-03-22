from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from fastapi.openapi.utils import get_openapi
from  app.utils.config_files import ConfigFiles
from app.router import clienteRouter
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

app = FastAPI(title="Conectcar WorkType")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Redirect"])
async def redirect():
    response = RedirectResponse(url='/docs')
    return response

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="ConectCar WorkType - Python",
        version="2.5.0",
        description="Exemplo de utilização Python.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
app.include_router(clienteRouter.router_cliente)