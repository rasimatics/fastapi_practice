from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm.session import Session
import jwt
from .crud import user_service
from ..db.dependency import get_db
from ..core.settings import settings



security = HTTPBearer()


def get_current_user(db: Session = Depends(get_db), credentials: str = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, settings.SECRET_KEY, settings.ALGORITHM)

    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Could not validate credentials'
        )

    user = user_service.get(db=db, id=payload['sub'])
    if not user:
        raise HTTPException(
            status_code=404, detail='User not found'
        )
        
    return user