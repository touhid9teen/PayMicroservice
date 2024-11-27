from datetime import timedelta
from django.utils import timezone
from auth_service.settings import SECRET_KEY
import jwt

def token_generator(user):
    exp = timezone.now() + timedelta(hours=1)
    payload = {
        'exp': exp,
        'email' : user.email,
        'username' : user.username,
        'user_number' : user.user_number,
        'current_balance': float(user.current_balance),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def refresh_token_generator(user):
    exp = timezone.now() + timedelta(days=7)
    payload = {
        'exp': exp,
        'email' : user.email,
        'username' : user.username,
        'user_number' : user.user_number,
        'current_balance': float(user.current_balance),
        'iat': timezone.now(),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token