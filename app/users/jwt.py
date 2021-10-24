import jwt
from datetime import datetime, timedelta
from ..core.settings import settings


def create_token(user_id):
    return _create_token(
        token_type="bearer",
        lifetime=timedelta(minutes=settings.EXPIRE_TIME_MINUTES),
        sub=user_id
    )


def _create_token(token_type, lifetime, sub):
    payload = {}
    expire_time = datetime.utcnow() + lifetime
    payload['type'] = token_type
    payload['exp'] = expire_time
    payload['iat'] = datetime.utcnow()
    payload['sub'] = str(sub)
    return {'token': jwt.encode(payload, settings.SECRET_KEY, settings.ALGORITHM)}



