import logging

from pprint import pprint

text_format = '%(asctime)s %(levelname)s (%(threadName)s) [%(name)s] %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=text_format, datefmt=date_format)

_LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':
    _LOGGER.info("test")
    _LOGGER.error("test")
