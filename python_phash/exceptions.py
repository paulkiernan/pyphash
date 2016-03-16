# Package Exceptions
class PHashError(Exception):
    pass

def _phash_errcheck(rc, func, args):
    """
    Error check callback

    @raises: RuntimeError if the wrapped function returns -1
    """

    if rc == -1:
        raise PHashError('%s %r returned %s' % (func, args, rc))
    else:
        return rc
