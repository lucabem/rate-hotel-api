from src.sql.sql_repository import SQLRepository


class EntityRepository(SQLRepository):
    def __init__(self, database, table) -> None:
        super().__init__(database, table)

    def select_historical_rates(self, entity_id, check_in):
        return self._execute_select(
            f"SELECT * FROM {self.database}.{self.name} WHERE entity_id = {entity_id} AND check_id = DATE'{check_in}'"
        )
