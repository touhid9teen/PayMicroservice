from datetime import timedelta
from django.utils import timezone
from service1.settings import SECRET_KEY
import jwt

def token_generator(service):
    exp = timezone.now() + timedelta(hours=1)
    payload = {
        'exp': exp,
        'service_user_name' : service.service_user_name,
        'service_name' : service.service_name,
        'password' : service.password,
        'id': service.id,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def refresh_token_generator(service):
    exp = timezone.now() + timedelta(days=7)
    payload = {
        'exp': exp,
        'service_user_name' : service.service_user_name,
        'service_name' : service.service_name,
        'password' : service.password,
        'id': service.id,
        'iat': timezone.now(),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token