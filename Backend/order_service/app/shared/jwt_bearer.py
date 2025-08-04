from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "secret-key")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(status_code=403, detail="Formato inválido del token.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Token inválido o expirado.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="No se proporcionó token.")

    def verify_jwt(self, token: str) -> bool:
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return True
        except JWTError as e:
            print("Token inválido:", e)
            return False

def get_current_user_id(token: str = Depends(JWTBearer())) -> int:
    print(" Token recibido:", token)  

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")
        print("Usuario autenticado (sub):", user_id) 
        return int(user_id)
    except Exception as e:
        print("Error al decodificar token:", e)
        raise HTTPException(status_code=403, detail="No autorizado")

