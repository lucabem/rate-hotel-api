from concurrent.futures import ThreadPoolExecutor, as_completed
from src.service.rate_downloader import RateDownloaderService
from src.utils.utils import DateUtils

class RateDownloaderWrapper:

    def __init__(self, threads:int = 5, fmt:str ='%Y-%m-%d') -> None:
        self.threads = int(threads)
        self.dates   = DateUtils.get_next_dates(days=31, fmt=fmt)

    def _runner(self, date: str) -> str:
        downloader_service = RateDownloaderService(date)
        return downloader_service.call()

    def call(self):
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            future_to_date = {executor.submit(self._runner, date): date for date in self.dates}
            for future in as_completed(future_to_date):
                date = future_to_date[future]
                try:
                    result = future.result()
                    print(result)
                except Exception as e:
                    print(f"Download {date} failed for {result}: {e}")