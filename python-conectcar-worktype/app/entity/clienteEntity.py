from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class ClienteEntity(Base):
    __tablename__ = "cliente"

    idcliente = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    placa_veiculo  = Column(String)
    endereco  = Column(String)
