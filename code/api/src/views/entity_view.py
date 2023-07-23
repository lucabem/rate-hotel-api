from src.views.view import View


class HistoricalEntityRatesView(View):
    def __init__(self, sql_rows):
        super().__init__(sql_rows)

    def view(self):
        return {
            "data": {
                "count": len(self.sql_rows), 
                "items": self.sql_rows
        }}
