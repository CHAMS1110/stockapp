import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 96f4a5ea160a345defdfff0320144e7c469ce70f'
}


def get_meta_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()


def get_price_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}/prices".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()[0]


def get_histo_price_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}/prices?startDate=2012-1-1&endDate=2022-3-3".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()