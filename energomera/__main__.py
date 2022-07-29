import logging

from energomera.protocol.ce import ErrorCode
from energomera.manager import Manager

text_format = '%(asctime)s %(levelname)s (%(threadName)s) [%(name)s] %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=text_format, datefmt=date_format)

_LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':
    error = ErrorCode.ParametersError
    _LOGGER.error(error)

    manager = Manager()


    @manager.handler([10])
    def test_1():
        pass

    @manager.handler([10])
    def test_1_1():
        pass

    @manager.handler([11])
    def test_1_2():
        pass


    @manager.handler([10, 12])
    def test_2():
        pass


    @manager.handler([10, 12, 1])
    def test_3():
        pass


    @manager.handler([10, 12, 1])
    def test_4():
        pass


    @manager.handler([10, 12, 2])
    def test_4():
        pass


    _LOGGER.info(manager.tree._tree)
