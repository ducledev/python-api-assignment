import falcon
from . import db, resources, settings
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend


def user_loader(payload: dict):
    username = payload.get('username')
    password = payload.get('password')
    if username == settings.JWT_CONFIG['username'] and password == settings.JWT_CONFIG['password']:
        return username
    else:
        return None


auth_backend = JWTAuthBackend(user_loader,
                              secret_key=settings.JWT_CONFIG['secret_key'],
                              verify_claims=['exp'],
                              required_claims=['exp'])
auth_middleware = FalconAuthMiddleware(auth_backend, exempt_methods=['HEAD'])

app = falcon.API(
    middleware=[
        auth_middleware,
        db.SQLAlchemySessionManager(db.Session),
    ],
)

app.add_route('/customers', resources.CustomerCollectionResource())
app.add_route('/customers/{customer_id}', resources.CustomerItemResource())
