import tda...

class TD_Client:

    #use the env for api key, stuff like that..


    #define methods to get options, or stocks.
    # and return in a form that you'd like to use.

    #### ALSO!, rate limiting is required.
    # maybe add it directly into this class, since
    # only this tda uses rate limit.

    ##example!
    def fetch_option_data(api_client, symbol): -> list:
        data = api_client.get_option_data(symbol)
        cleaned_data = {
            'symbol': data['symbol'],
            'strike_price': float(data['strikePrice']),
            'expiration_date': data['expirationDate'],
            'option_type': data['optionType'],
            'price': float(data['lastPrice'])
            ....
            .
        }
        return [stock, optionchain_call, puts..idk]
