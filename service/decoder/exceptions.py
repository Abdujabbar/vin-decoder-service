class BaseDecodeException(Exception):
    pass


class NotFoundException(Exception):
    def __str__(self):
        return 'NotFound'


class InternalServerErrorException(Exception):
    def __str__(self):
        return 'Internal Error'


class UnauthorizedException(Exception):
    def __str__(self):
        return 'You are not authorized'


class UnexpectedException(Exception):
    def __str__(self):
        return 'UnexpectedException'
