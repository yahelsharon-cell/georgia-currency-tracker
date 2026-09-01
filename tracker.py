import os
import requests
from dotenv import load_dotenv

# 1. Load the hidden vault (.env)
load_dotenv()

# 2. Get the API key securely
api_key = os.getenv("EXCHANGE_API_KEY")

# 3. Set up the API address
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/ILS"

# 4. Fetch the data from the internet
print("Fetching live exchange rates...")
response = requests.get(url)
data = response.json()

# 5. Extract the Lari rate and print it
if response.status_code == 200:
    gel_rate = data["conversion_rates"]["GEL"]
    print(f"1 ILS = {gel_rate} GEL")
    print("Time to start budgeting for the road trip.")
else:
    print("Error fetching data:", data)