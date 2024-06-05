
class mysql_client_interactor:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager


    def insert_into_table(table, data, parameters?):
        get connection,
        sql = f"somethingsomething {table}"..?

        execute
        release connection..

    def read_from_something(table, something):
        get Connec
        execute

        return


    def aggregate_something_data_something(table, table)
        something something
        ### pure sql execution to get 1 table's data
        ### calculate a bunch and put into another table..


class mysql_pool_client:

    def __init__(self) -> None:
        self.connection = pooled connection


    def read_something()...:
        return data...
