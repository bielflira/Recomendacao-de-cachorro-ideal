import jwt
from datetime import datetime, timedelta

SECRET = "segredo123"

def gerar_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")
