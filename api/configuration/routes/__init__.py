from configuration.routes.routes import Routes
from internal.routes import user, auth, files, text_input

__routes__ = Routes(routers=(user.router, auth.router, files.router, text_input.router))