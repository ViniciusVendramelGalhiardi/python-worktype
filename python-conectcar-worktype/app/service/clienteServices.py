from fastapi import FastAPI, APIRouter, Request
from typing import Optional
from pydantic import BaseModel
import requests
import json 
from app.utils.config_files import ConfigFiles
from fastapi import logger 
from app.model.clienteModel import ClienteModel
from app.data.clienteData import ClienteFactory, insert, getById, delete, update, getAll
from app.model.response import Response, getResponse
from app.entity.clienteEntity import ClienteEntity

def InserirCliente(request: ClienteModel):
    try:
        clienteEntity = ClienteFactory(request)
        insert(clienteEntity)
        return getResponse(200, "Sucesso", '')
    except Exception as e:
        return getResponse(400, "Request error.", '')

def BuscarPorId(Id: int):
    try:
        cli = ClienteEntity()
        cli = getById(Id)
        return getResponse(200, "Sucesso", json.dumps(cli, default=encoder_cliente)) 
    except Exception as e:
        return getResponse(400, "Request error.")

def DeletaPorId(Id: int):
    try:
        delete(Id)
        return getResponse(200, "Sucesso", '') 
    except Exception as e:
        return getResponse(400, "Request error.")

def AtualizarCliente(request: ClienteModel, id: int):
    try:
        clienteEntity = ClienteFactory(request)
        update(clienteEntity, id)
        return getResponse(200, "Sucesso",'')
    except Exception as e:
        return getResponse(400, "Request error.", json.dumps(clienteEntity, default=encoder_cliente))


def BuscarTodos():
    try:
        response = getAll()
        return getResponse(200, "Sucesso", json.dumps(response, default=encoder_cliente)) 
    except Exception as e:
        return getResponse(400, "Request error.")


def encoder_cliente(cliente):
    if isinstance(cliente,ClienteEntity):
        return {'nome': cliente.nome, 'placa_veiculo': cliente.placa_veiculo, 'endereco': cliente.endereco}
