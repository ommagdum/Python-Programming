# Input initial investment and annual interest rate
initial_investment = float(input("Enter the initial investment amount: "))
annual_interest = float(input("Enter the annual interest rate (in percentage): "))
years = int(input("Enter the number of years: "))

# For loop to calculate investment value over time
investment_value = initial_investment
for year in range(1, years + 1):
    investment_value += investment_value * (annual_interest / 100)
    print(f"Value of investment after year {year}: {investment_value:.2f}")