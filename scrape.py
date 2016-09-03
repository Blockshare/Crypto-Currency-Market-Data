import requests, json


def market_prices():

    btc_data = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin")
    eth_data = requests.get("https://api.coinmarketcap.com/v1/ticker/ethereum")
    ltc_data = requests.get("https://api.coinmarketcap.com/v1/ticker/litecoin")

    bitcoin = btc_data.json()
    ethereum = eth_data.json()
    litecoin = ltc_data.json()

    btc_params = {
        'price': bitcoin[0]['price_usd'],
        'symbol': bitcoin[0]['symbol'],
        'market_cap': bitcoin[0]['market_cap_usd'],
        'percentage_change_24h': bitcoin[0]['percent_change_24h'],
        'volume': bitcoin[0]['24h_volume_usd']
    }

    eth_params = {
        'price': ethereum[0]['price_usd'],
        'symbol': ethereum[0]['symbol'],
        'market_cap': ethereum[0]['market_cap_usd'],
        'percentage_change_24h': ethereum[0]['percent_change_24h'],
        'volume': ethereum[0]['24h_volume_usd']
    }  

    ltc_params = {
        'price': litecoin[0]['price_usd'],
        'symbol': litecoin[0]['symbol'],
        'market_cap': litecoin[0]['market_cap_usd'],
        'percentage_change_24h': litecoin[0]['percent_change_24h'],
        'volume': litecoin[0]['24h_volume_usd']
    }

    params = {
        'market_prices': {
            'bitcoin': btc_params,
            'ethereum': eth_params,
            'litecoin': ltc_params
        }
    }

    return params


if __name__=='__main__':
    data = market_prices()
    market_data = json.dumps(data, indent=2, sort_keys=True)
    print(market_data)
