import sys
from datetime import datetime
from scapy.all import srp,Ether,ARP,conf 
from sploitkit import *

class arp_scan(Module):
    """ 
    hedef ağı tarar"
    Author: Mahmut P.
    Version: 1.0
    """
    config = Config({
        Option(
            "interface",
            "tarama interface",
            True
            ): "ens33",
        Option(
            "ips",
            "hedef ip okleti",
            True
            ):"192.168.0.0/24"
        })
    def run(self):
        
        try:
            self.logger.info("Taranıyor...")
            conf.verb = 0
            ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = self.config.option("ips").value),
                     timeout = 2,
                     iface = self.config.option("interface").value,
                    inter = 0.1)
            self.logger.debug("IP - MAC")
            list_of_test = []
            for snd,rcv in ans:
                self.logger.info(rcv.sprintf(r"%ARP.psrc% - %Ether.src%"))
                list_of_test.append(r"%ARP.psrc% - %Ether.src%")
            if list_of_test == []:
                self.logger.warning("Hedef bulunamadı")

            self.logger.info("Tarama tamamlandı.")

        except:
            self.logger.failure("Hata oluştu")
        
        """
        self.logger.info("Taranıyor...")
        conf.verb = 0
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = self.config.option("ips").value),
                 timeout = 2,
                 iface = self.config.option("interface").value,
                 inter = 0.1)
        self.logger.debug("IP - MAC")
        list_of_test = []
        for snd,rcv in ans:
            self.logger.info(rcv.sprintf(r"%ARP.psrc% - %Ether.src%"))
            list_of_test.append(r"%ARP.psrc% - %Ether.src%")
        if list_of_test == []:
            self.logger.warning("Hedef bulunamadı")
        self.logger.info("Tarama tamamlandı.")
        """
