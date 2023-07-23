class View:
    def __init__(self, sql_rows, wrapper=None, grouped_data_wrapper=None, grouped_keys=None):
        self.sql_rows = sql_rows
        self.wrapper = wrapper
        self.grouped_keys = grouped_keys
        self.grouped_data_wrapper = grouped_data_wrapper or wrapper

    def view(self):
        return {
            self.wrapper: self.sql_rows
        }