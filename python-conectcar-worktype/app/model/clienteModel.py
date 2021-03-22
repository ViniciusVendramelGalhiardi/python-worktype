from pydantic import BaseModel,constr
from pydantic.types import  constr

class ClienteModel(BaseModel):
    nome: str
    placa_veiculo: str
    endereco: str