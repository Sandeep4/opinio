__author__ = 'sandeep'


class Error(Exception):
    """ Generic Error for client """
    pass


class ValidationError(Error):
    """ Error in case of invalid input """
    pass


class HTTPError(Error):
    """ Error Response from API """
    pass
