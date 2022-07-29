import logging

from energomera.protocol.ce import ErrorCode

text_format = '%(asctime)s %(levelname)s (%(threadName)s) [%(name)s] %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=text_format, datefmt=date_format)

_LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':
    error = ErrorCode.ParametersError
    _LOGGER.error(error)
