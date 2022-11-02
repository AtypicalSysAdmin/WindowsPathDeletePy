import sys 
sys.dont_write_bytecode = True


import logging
from logging.handlers import RotatingFileHandler
import traceback

logger = logging.getLogger("Application Log")
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(".\\Logs\\tracebacklog.txt", mode='w', maxBytes=10000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
# try:
#     1/0 
# except Exception as e:
#     logger.error(str(e))
#     logger.error(traceback.format_exc())