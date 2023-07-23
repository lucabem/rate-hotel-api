
from datetime import datetime, timedelta


class DateUtils:

    @staticmethod
    def get_dates_by_month(month: int, fmt: str):
        if not 1 <= month <= 12:
            raise ValueError("Invalid month. Month should be an integer between 1 and 12.")

        start_date = datetime(datetime.now().year, month, 1)
        last_day = 31  
        while True:
            try:
                end_date = start_date.replace(day=last_day)
                break
            except ValueError:
                last_day -= 1

        dates = []
        current_date = start_date
        while current_date <= end_date:
            dates.append(current_date.strftime(fmt))
            current_date += timedelta(days=1)

        return dates
    
    @staticmethod
    def get_next_dates(days: int, fmt: str):
        current_date = datetime.today()
        next_dates = []
        for i in range(days):
            next_dates.append(current_date.strftime(fmt))
            current_date += timedelta(days=1)
        
        return next_dates


    
    @staticmethod
    def format_date_to_str(date: datetime, fmt: str) -> str:
        return date.strftime(fmt)
    
    @staticmethod
    def get_current_month():
        return datetime.now().month