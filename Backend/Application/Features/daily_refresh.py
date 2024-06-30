

data_repo = data_repo.()
schwab = schwab_client()..

data_processor(data_repo)
#initialize some processors or managers or etc..

for stock in ticker_list:
    data = schwab_client.get_data(stock)
    manager.process(data)
