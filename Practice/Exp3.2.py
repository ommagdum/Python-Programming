'''Write a python program using for loop to calculate the value of
an investment. Input an initial 2 value of investment and annual
interest, and calculate the value of investment over time.'''

investment = int(input("Enter Investment Amount : "))
annual_int = float(input("Enter Annual Interest : "))
years = int(input("Enter Number Of Years : "))

investment_ovt = investment
for year in range(1, years + 1):
    investment_ovt += investment * (annual_int / 100)
    print(f"Value Of Investment After {years} Years : {investment_ovt:.2f}")