
class StatusCodeException (Exception):
    def __innit__(self, message):
        self.message = message