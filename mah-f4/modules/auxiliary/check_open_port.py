from sploitkit import *
import socket
class check_port(Module):
    """
    check open port
    Author: Mahmut P.
    Version: 1.0
    """
    config = Config({
        Option(
            "target",
            "hedef",
            True,
            ):"127.0.0.1",
        Option(
            "port",
            "port",
            True,
            ): 80
        })
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((self.config.option("target").value, self.config.option("port").value))
        if result == 0:
            self.logger.info("Port is open")
        else:
            self.logger.warning("Port is not open")
        sock.close()

