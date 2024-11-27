import jwt
from rest_framework.exceptions import PermissionDenied
from transferMoneyService.settings import SECRET_KEY

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise PermissionDenied('Token has expired')
    except jwt.InvalidTokenError:
        raise PermissionDenied('token is invalid')


def get_token_from_header(auth_header):
    parts = auth_header.split()
    if parts[0].lower() != 'bearer':
        raise PermissionDenied('Authorization header must start with Bearer')
    if len(parts) == 1:
        raise PermissionDenied('Token not provided')
    elif len(parts) > 2:
        raise PermissionDenied('Authorization header must be Bearer token')
    return parts[1]