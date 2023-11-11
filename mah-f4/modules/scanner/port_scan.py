from sploitkit import *
import socket
import sys
import re


class portscan(Module):
    """
    port scan
    Author: Mahmut P.
    Version: 1.0
    """
    config = Config({
        Option(
            "ip",
            "hedef ip",
            True,
            ):"127.0.0.1",
        Option(
            "min_port",
            "başlangıç portu",
            True,
            ): 1,
        Option(
            "max_port",
            "son port",
            True,
            ):65535
        })
    def run(self):
        ip_model = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        port_model = re.compile("([0-9]+)-([0-9]+)")

        min_port = self.config.option("min_port").value
        max_port = self.config.option("max_port").value

        open_ports = []

    
        ip = self.config.option("ip").value
        self.logger.info(f"{ip} is a IP address to scan")



        for port in range(min_port, max_port + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.8)
                    s.connect((ip, port))
                    open_ports.append(port)

            except:
                pass

        for port in open_ports:
             self.logger.info(f"Port {port} is OPEN on {ip}.")
