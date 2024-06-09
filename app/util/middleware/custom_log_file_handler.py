import os
import time
from logging.handlers import TimedRotatingFileHandler


class CustomTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None

        current_time = self.rolloverAt - self.interval
        time_tuple = (
            self.utc and time.gmtime(current_time) or time.localtime(current_time)
        )
        dfn = self.rotation_filename(
            self.baseFilename + "." + time.strftime("%Y-%m-%d", time_tuple)
        )

        if not self.delay:
            self.stream = self._open()

        if os.path.exists(dfn):
            os.remove(dfn)

        self.rotate(self.baseFilename, dfn)
        if not self.delay:
            self.stream = self._open()

        new_rollover_at = self.computeRollover(current_time)
        while new_rollover_at <= current_time:
            new_rollover_at += self.interval

        self.rolloverAt = new_rollover_at
