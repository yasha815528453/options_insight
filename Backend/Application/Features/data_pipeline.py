### should be a script
## the entry point of data etl


##initialize tda api client
api_client = tdaapi_client()


for stock in optionable_stocks:
    stock, calls, puts = api_client.fetch_data(stock)
    stock_manager.update....
    stock_manager.update table..?
    options_manager.update..something..
    (all the level 1 tables are filled)
##for stock in all stocks
###get data for each of the stock


###clean/process



### finally insert them to respective tables.
