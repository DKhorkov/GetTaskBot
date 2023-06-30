import logging
import os


if not os.path.exists('logs'):
    os.mkdir('logs')


logging.basicConfig(
    level=logging.DEBUG,
    filename='logs/logs.log',
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)

logger = logging.getLogger('GetTaskBot')
