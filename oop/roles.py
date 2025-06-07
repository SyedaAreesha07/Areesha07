from loggers.file_logger import Logger

class AdminRole:
    def log(self, username, action):
        with Logger("admin.log") as logger:
            logger.write_log(f"[ADMIN] {username}: {action}")

class HRRole:
    def log(self, username, action):
        with Logger("hr.log") as logger:
            logger.write_log(f"[HR] {username}: {action}")
from loggers.file_logger import Logger

class AdminRole:
    def log(self, username, action):
        with Logger("admin.log") as logger:
            logger.write_log(f"[ADMIN] {username}: {action}")

class HRRole:
    def log(self, username, action):
        with Logger("hr.log") as logger:
            logger.write_log(f"[HR] {username}: {action}")
