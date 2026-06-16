import requests

def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 20,
        'page': 1
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Check for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_and_filter(data):
    search = input("Enter a coin name to search (or press Enter to see top 20): ").lower()
    
    print(f"\n{'Name':<20} | {'Price (USD)':<15}")
    print("-" * 40)
    
    found = False
    for coin in data:
        if search in coin['name'].lower():
            print(f"{coin['name']:<20} | ${coin['current_price']:,.2f}")
            found = True
    
    if not found:
        print("No coins found matching your search.")

if __name__ == "__main__":
    print("Fetching latest crypto data...")
    data = get_crypto_data()
    if data:
        display_and_filter(data)