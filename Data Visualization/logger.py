import os
from datetime import datetime

class Logger:
    def __init__(self, file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.file_path = file_path

    def log(self, message):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        with open(self.file_path, 'a') as f:
            f.write(f"{timestamp} {message}\n")
