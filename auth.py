import json
from flask import _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH_DOMAIN = 'majeed.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'capstone'

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

# Auth Header 

def get_token_auth_header():

    if 'Authorization' not in request.headers:
        raise AuthError({
            'code': 'Authorization_header_missing',
            'description': 'Authorization header is expected'
        },401)
    auth = request.headers.get('Authorization')

    parts = auth.split()
    if parts[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must start with Bearer'
        },401)
    elif len(parts) < 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'token is invalid'
        },401)
    elif len(parts) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must be bearer token'
        },401)
    token = parts[1]
    return token

def check_permissions(permission, payload):
    if permissions not in payload:
        raise AuthError({
            'code': 'invalid_calaims',
            'description': 'permissions not included in JWT'
        }, 400)
    elif permission not in permissions:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'permission not encluded'
        }, 401)
    return True

def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH_DOMAIN}/.wll-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'code': 'Authorization malformed'
            }, 401)
    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                issuer='https://'+ AUTH0_DOMAIN + '/'
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'token expired'
            }, 401)
        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'Invalid_claims',
                'description': 'Incorrect claims, check issuer and audience'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'Invalid_claims',
                'description': 'Unable to parse authentication token'
            }, 400)
    raise AuthError({
        'code': 'Invalid_claims',
        'description': 'Unable to parse authentication token'
        }, 400)
        
def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            try:
                payload = verify_decode_jwt(token)
            except BaseException:
                raise AuthError({
                    'code': 'Invalid Token',
                    'description': 'Token is invalid'
                },401)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator
    
