from fastapi import APIRouter, FastAPI, HTTPException, Request, Response, logger, Depends, status 
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
import json   
from app.utils.config_files import ConfigFiles
from app.model.response import getResponse
from app.model.clienteModel import ClienteModel
from app.data.clienteData import ClienteFactory
from app.service.clienteServices import InserirCliente, BuscarPorId, DeletaPorId, AtualizarCliente, BuscarTodos
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

router_cliente = APIRouter(
    prefix="/Cliente",
    tags=["Cliente"]
)

@router_cliente.post("/Adicionar/", dependencies=[Depends(JWTBearer())])
async def addCliente(ClienteModel: ClienteModel):
    response = InserirCliente(ClienteModel)
    return JSONResponse(status_code = response.status, 
                        content = response.__dict__)

@router_cliente.get("/BuscarPorId/{id}", dependencies=[Depends(JWTBearer())])
async def buscarId(id: int):
    response = BuscarPorId(id)
    return JSONResponse(status_code = response.status, 
                        content = response.__dict__)   

@router_cliente.delete("/Deletar/{id}", dependencies=[Depends(JWTBearer())])
async def deletarCliente(id: int):
    response = DeletaPorId(id)
    return JSONResponse(status_code = response.status, 
                        content = response.__dict__)


@router_cliente.put("/Atualizar/{id}", dependencies=[Depends(JWTBearer())])
async def atualizarCliente(ClienteModel: ClienteModel, id: int):
    response = AtualizarCliente(ClienteModel, id)
    return JSONResponse(status_code = response.status, 
                        content = response.__dict__)


@router_cliente.get("/BuscarTodos", dependencies=[Depends(JWTBearer())])
async def buscarTodos():
    response = BuscarTodos()
    return JSONResponse(status_code = response.status, 
                        content = response.__dict__)