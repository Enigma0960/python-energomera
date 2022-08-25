import logging

from energomera.system import Manager, BaseProtocol

text_format = '%(asctime)s %(levelname)s (%(threadName)s) [%(name)s] %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=text_format, datefmt=date_format)

_LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':
    manager = Manager(protocol=BaseProtocol())


    @manager.handler(cmd=[10])
    def example_1(key, data):
        _LOGGER.info(f'example_1: {key}: {data}')


    manager._process([10, 11, 12, 13])
