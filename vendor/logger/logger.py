import logging
import datetime
import os


class Logger:
    "Helper to load config values from config file"

    _logger = None

    def __init__(self, app_path):
        # init logger
        self.logger = logging.getLogger()
        self._check_path_and_create("%s/logs" % app_path)
        handler = logging.FileHandler("%s/logs/log-%s.txt" % (app_path, datetime.date.today().strftime("%Y%m%d")))
        formatter = logging.Formatter(
                '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def debug(self, msg):
        self.logger.debug(msg)

    @staticmethod
    def _check_path_and_create(log_path):
        if not os.path.isdir(log_path):
            os.makedirs(log_path)
