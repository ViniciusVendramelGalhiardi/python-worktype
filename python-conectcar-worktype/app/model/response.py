from pydantic import BaseModel, json


class Response(BaseModel):
    status: int
    mensagem: str
    conteudo: str
 
def getResponse(status, mensagem, conteudo):
    response_object = Response(
        status=status,
        mensagem= mensagem,
        conteudo = conteudo
    ) 
    return response_object