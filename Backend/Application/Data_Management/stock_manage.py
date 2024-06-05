
import mysql_client..
import tables from config...?

in some file, there should be a list of like defined tables
like
stock_info
options
ivchart
ivhistory
etc...

mysql_client has the actual sqls written in,
with parameters you can fill in.

class stock_manager:

    def __init__(self) -> None:
        pass

    def update_stock(mysql_client, data..):
        ticker, stock_data = data

        mysql_client.update(tables.stock_info, ticker, stock_data)

class options? or in a parallel file?
