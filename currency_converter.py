import requests

print("💱 Currency Converter")

base_currency = input("Enter base currency (e.g., USD): ").upper()
target_currency = input("Enter target currency (e.g., INR): ").upper()
amount = float(input("Enter amount: "))

url = f"https://open.er-api.com/v6/latest/{base_currency}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if target_currency in data["rates"]:
        rate = data["rates"][target_currency]
        converted_amount = amount * rate

        print(f"\n💰 {amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("❌ Invalid target currency code.")
else:
    print("❌ Unable to fetch exchange rates.")
