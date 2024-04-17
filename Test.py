import requests

def get_btc_to_eth_rate():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eth")
        data = response.json()
        btc_to_eth_rate = data["bitcoin"]["eth"]
        return btc_to_eth_rate
    except Exception as e:
        print("Error fetching data:", e)
        return None

if __name__ == "__main__":
    rate = get_btc_to_eth_rate()
    if rate is not None:
        print("BTC to ETH rate:", rate)