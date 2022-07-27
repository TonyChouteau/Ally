
from utils.logger import Logger

logger = Logger("Ally")

class Ally:

    def __init__(self):
        self.router = {
            "ping": self.ping,
            "message": self.message
        }

    def handle(self, route_name, data):
        route = self.router.get(route_name)
        if route:
            route(data)  # noqa

    def ping(self, _):
        logger.log("ping")
        return "pong"

    def message(self, data):
        logger.log("message")
        logger.log(data)
        return "Ok"