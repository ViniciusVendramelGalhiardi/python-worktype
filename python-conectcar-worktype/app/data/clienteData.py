from app.entity.clienteEntity import ClienteEntity
from sqlalchemy import or_
from .base import session_factory  
from app.model.clienteModel import ClienteModel

def getById(id: int):
    session = session_factory()
    response = session.query(ClienteEntity).get(id)

    session.close()
    return response

def getAll():
    session = session_factory()
    response = session.query(ClienteEntity).all()
    session.close()
    return response


def insert(request: ClienteEntity):
    session = session_factory()
    session.add(request)  
    session.commit()
    session.close()

def update(request: ClienteEntity, id:int):
    request.idcliente = id
    session = session_factory()
    response = session.query(ClienteEntity).get(id)
    response.nome = request.nome
    response.endereco = request.endereco
    response.placa_veiculo = request.placa_veiculo
    session.commit()
    session.close()    

def delete(id: int):
    session = session_factory()
    session.query(ClienteEntity).\
                filter(ClienteEntity.idcliente == id).\
                delete()

    session.commit()
    session.close()    


def ClienteFactory(request: ClienteModel):
    cli = ClienteEntity()
    cli.endereco = request.endereco
    cli.nome = request.nome
    cli.placa_veiculo = request.placa_veiculo
    return cli


