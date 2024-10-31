from configuration.routes.routes import Routes
from internal.routes import user, admin

__routes__ = Routes(routers=(user.router, admin.router))