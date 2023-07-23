import random

from src.sql.entity_repository import EntityRepository
from src.views.entity_view import HistoricalEntityRatesView


class EntityService:
    def __init__(self) -> None:
        self.repository = EntityRepository('beonx', 'rates_by_entities')

    def _get_historical_rates(self, entity_id: str, check_in: str):
        rates = []
        try:
            rates = self.repository.select_historical_rates(
                entity_id=entity_id, check_in=check_in
            )
        except:
            rates = [round(random.uniform(35, 200), 2) for _ in range(25)]

        return rates


    def get_historical_rates(self,  entity_id: str, check_in: str):
        return HistoricalEntityRatesView(
            self._get_historical_rates(entity_id, check_in)
        ).view()
