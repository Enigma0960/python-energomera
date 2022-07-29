import logging

from pprint import pprint

from energomera.protocol.ce import ErrorCode
from energomera.manager import Manager

text_format = '%(asctime)s %(levelname)s (%(threadName)s) [%(name)s] %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=text_format, datefmt=date_format)

_LOGGER = logging.getLogger(__name__)
manager = Manager()


@manager.handler(cmd=[10, 11, 12])
def call_test_1(): pass


@manager.handler(cmd=[10, 12])
def call_test_2(): pass


@manager.handler(cmd=[10])
def call_test_3(): pass


@manager.handler(cmd=[11])
def call_test_4(): pass


@manager.handler(cmd=[10, 11])
def call_test_5(): pass


@manager.handler(cmd=[10])
def call_test_6(): pass


@manager.handler(cmd=[10])
def call_test_7(): pass


if __name__ == '__main__':
    pprint(manager.tree._tree)
