from configuration.routes.routes import Routes
from internal.routes import user, auth

__routes__ = Routes(routers=(user.router, auth.router))   