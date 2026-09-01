import os
import requests
from dotenv import load_dotenv

# We moved the URL creation into its own function so we can test it safely
def build_api_url(api_key, base_currency):
    return f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("EXCHANGE_API_KEY")
    
    # We now call our new function here
    url = build_api_url(api_key, "ILS")
    
    print("Fetching live exchange rates...")
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        gel_rate = data["conversion_rates"]["GEL"]
        print(f"1 ILS = {gel_rate} GEL")
        print("Time to start budgeting for the road trip.")
    else:
        print("Error fetching data:", data)