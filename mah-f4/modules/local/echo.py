from sploitkit import *

class echo(Module):
    """ 
    Ekrana degeri yazar
    Author: Mahmut P.
    Version: 1.0
    """
    config = Config({
        Option(
            'deger',
            "yazılacak değer",
            True,
        ): "test"
    })
    def run(self):
        self.logger.info(self.config.option("deger").value)
