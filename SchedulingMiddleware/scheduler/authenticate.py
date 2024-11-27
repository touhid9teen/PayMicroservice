from rest_framework.authentication import BaseAuthentication
from django.core.exceptions import PermissionDenied
from .anonymous import CustomerModel
import jwt
from .utils import decode_token, get_token_from_header

class CustomAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if auth_header:
            token = get_token_from_header(auth_header)
            if token:
                try:
                    payload = decode_token(token)
                    return CustomerModel(**payload), token
                except jwt.ExpiredSignatureError:
                    raise PermissionDenied('Token has expired')
                except jwt.InvalidTokenError:
                    raise PermissionDenied('Invalid token')
            return None




