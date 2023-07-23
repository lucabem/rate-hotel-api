
import datetime
from time import sleep
from src.utils.utils import DateUtils
import src.config.config_defaults as cf

class RateDownloaderService:

    def __init__(self, date: str) -> None:
        self.path: str = cf.LANDING_PATH
        self.frmt: str = cf.LANDING_FORMAT
        self.date: str = date

    def _download_service(self) -> str:
        sleep(1)
        return'{}/{}/rates_{}.{}'.format(
            self.path,           
            DateUtils.format_date_to_str(
                date=datetime.datetime.utcnow(),
                fmt='%Y-%m-%d'), 
            self.date,
            self.frmt
        )
    
    def call(self):
        return self._download_service()
    
    