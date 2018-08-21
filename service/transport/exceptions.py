
class NotFoundException(Exception):
    def __str__(self):
        return "NOTFOUND"

class InternalServerErrorException(Exception):
    pass


class UnauthorizedException(Exception):
    pass

