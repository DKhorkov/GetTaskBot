import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename='logs.log',
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)

logger = logging.getLogger('GetTaskBot')

TOKEN = "YOUR TELERGAM BOT TOKEN HERE"
