from sploitkit import *
import requests

class check_http_status_code(Module):
    """
    check http status code
    Author: Mahmut P.
    Version: 1.0
    """
    config = Config({
        Option(
            "url",
            "example https://stackoverflow.com",
            True,
            ): "https://stackoverflow.com"
        })

    def run(self):
        self.logger.info("url= "+self.config.option("url").value)
        r = requests.head(self.config.option("url").value)
        self.logger.info(f"code: {r.status_code}")
        
