import logging

from pprint import pprint

from energomera.protocol.ce import ErrorCode
from energomera.manager import Manager, Group

text_format = '%(asctime)s %(levelname)s (%(threadName)s) [%(name)s] %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=text_format, datefmt=date_format)

_LOGGER = logging.getLogger(__name__)
manager = Manager(protocol=None)


group = Group([10, 13])

@manager.handler(cmd=[10, 11, 12])
def call_test_1(*args):
    _LOGGER.info(f'Test 1: {args}')


@manager.handler(cmd=group([10,21])) # 10, 13, 10, 21
def call_test_any(*args):
    _LOGGER.info(f'Test 1: {args}')


@manager.handler(cmd=[10, 12])
def call_test_2(*args):
    _LOGGER.info(f'Test 2: {args}')


@manager.handler(cmd=10)
def call_test_3(*args):
    _LOGGER.info(f'Test 3: {args}')


@manager.handler(cmd=[11])
def call_test_4(*args):
    _LOGGER.info(f'Test 4: {args}')


@manager.handler(cmd=[10, 11])
def call_test_5(*args):
    _LOGGER.info(f'Test 5: {args}')


@manager.handler(cmd=[10])
def call_test_6(*args):
    _LOGGER.info(f'Test 6: {args}')


@manager.handler(cmd=[10])
def call_test_7(*args):
    _LOGGER.info(f'Test 7: {args}')

@manager.handler(cmd=[10, 42])
def _(*args):
    _LOGGER.info(f'Test 7: {args}')


    # manager._tree.call([10, 11, 13, 14, 15])
    # manager._tree.call([10, 12, 13, 14, 15, 21])
    # manager._tree.call([10, 42])
    # manager._tree.call([10, 42, 42, 42, 42, 42])

    # manager._tree.remove(call_test_5)

    # manager._tree.call([10, 11, 13, 14, 15])
    pass
