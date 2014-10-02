import datetime
import logging
import os
import time


class LogFormatter(logging.Formatter):
    converter = time.gmtime

    def format(self, record):
        formatted = logging.Formatter.format(self, record)

        if hasattr(record, "host"):
            formatted = ("[%10s]  " % record.host) + formatted

        formatted = self.formatTime(record) + "  " + formatted

        return formatted


def log_to_file(config, word):
    formatter = LogFormatter()

    now = datetime.datetime.utcnow()
    log_name = now.strftime("%Y-%m-%d_%H:%M:%S") + "-" + word + ".log"
    log_path = os.path.join(config["deploy"]["log-directory"], log_name)
    handler = logging.FileHandler(log_path, mode="w")
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(handler)

    return log_path
