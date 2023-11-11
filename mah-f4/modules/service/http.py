from sploitkit import *
import os

class http_service(Module):
    """
    Http server başlatması. os.system("sudo python3 -m http.server {port} directory
    Author: Mahmut P.
    Version: 1.0
    """
    config = Config({
        Option(
            "port",
            "port",
            True,
            ): 80,
        Option(
            "directory",
            "yayın dizini",
            True,
            ): "."
        })
    def run(self):
        self.logger.info("ctrl + c = exit")
        os.system(f"sudo python3 -m http.server {self.config.option('port').value} --directory {self.config.option('directory').value}")

