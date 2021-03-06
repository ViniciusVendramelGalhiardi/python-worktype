import time
from typing import Dict
import jwt 
from app.utils.config_files import ConfigFiles
from datetime import datetime 

JWT_SECRET = ConfigFiles.SecretKey()
JWT_ALGORITHM = 'HS256'  

def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def token_response(token: str):
    return {
        "access_token": token
    }

def decodeJWT(token: str) -> dict:
    
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        date = datetime.fromtimestamp(float(decoded_token["exp"])) if 'exp' in decoded_token else datetime.now()
        ConfigFiles().setUerId(decoded_token["uid"])
        return decoded_token if date >= datetime.now() else None
    except:
        return {} 
 