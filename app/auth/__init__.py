def init_api(api):
    from app.auth import controllers
    api.add_resource(controllers.UserRegistration, '/registration')
    api.add_resource(controllers.UserLogin, '/login')
    api.add_resource(controllers.UserLogoutAccess, '/logout/access')
    api.add_resource(controllers.UserLogoutRefresh, '/logout/refresh')
    api.add_resource(controllers.TokenRefresh, '/token/refresh')
    api.add_resource(controllers.AllUsers, '/users')
    api.add_resource(controllers.SecretResource, '/secret')


def init_jwt(app):
    from flask_jwt_extended import JWTManager

    jwt = JWTManager(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        from app.auth import models
        jti = decrypted_token['jti']
        return models.RevokedTokenModel.is_jti_blacklisted(jti)
