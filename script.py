import requests

def get_all_cryptocurrencies():
    # Fetch all cryptocurrencies data from CoinGecko API
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        for idx, crypto in enumerate(data, start=1):
            print(f"{idx}. {crypto['name']} ({crypto['symbol']}): ${crypto['current_price']}")
    else:
        print("Failed to fetch cryptocurrency data")

def analyze_cryptocurrencies(choices):
    # Fetch specific cryptocurrencies data from CoinGecko API based on user choices
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": ",".join(choices),
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        for crypto in data:
            print(f"{crypto['name']} ({crypto['symbol']}): ${crypto['current_price']}")
            print(f"Market Cap Rank: {crypto['market_cap_rank']}")
            print(f"24h Change: {crypto['price_change_percentage_24h']}%")
            print("--------------")
    else:
        print("Failed to fetch cryptocurrency data")

def main():
    print("Fetching top 10 cryptocurrencies...")
    get_all_cryptocurrencies()
    
    choices = input("Enter the numbers of cryptocurrencies you want to analyze (comma-separated): ").split(",")
    
    analyze_cryptocurrencies(choices)

if __name__ == "__main__":
    main()
