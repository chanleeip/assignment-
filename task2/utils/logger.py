import logging
from logging.handlers import TimedRotatingFileHandler
import datetime
from time import sleep
import os
import json
from dotenv import load_dotenv


load_dotenv()

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.datetime.fromtimestamp(record.created).isoformat(),
            "name": record.name,
            "level": record.levelname,
            "message": record.msg % record.args,  # handle formatted messages
            "pathname": record.pathname,
            "lineno": record.lineno,
        }
        return json.dumps(log_record)


class JsonRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        self.formatter = JSONFormatter()


def create_logger(name, path,use_json=False):

    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)
    if use_json:
        log_filename = datetime.datetime.now().strftime(f"{path}")
        f_handler = JsonRotatingFileHandler(
            log_filename, when="midnight", interval=1, backupCount=30, encoding='utf-8'
        )
        f_handler.suffix = "%Y-%m-%d"
        f_handler.setLevel(logging.INFO)
        logger.addHandler(f_handler)
    else:
        log_filename = datetime.datetime.now().strftime(f"{path}")
        f_handler = TimedRotatingFileHandler(
            log_filename, when="midnight", interval=1, backupCount=30
        )
        f_handler.suffix = "%Y-%m-%d"

        c_handler = logging.StreamHandler()

        c_handler.setLevel(logging.INFO)
        f_handler.setLevel(logging.INFO)

        c_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
    return logger


logPath = "logs"
if not os.path.exists(logPath):
    os.makedirs(logPath)
logger = create_logger("log", f"{logPath}/logs.json",use_json=False)
