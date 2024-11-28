'''Write a python program that has a class store which keeps a record of
code and prices of each product. Display a menu of all products to the
user and prompt him/her to enter the quantity of each item required.
Generate a bill and display the total amount'''

class Store:

    def __init__(self):
        self.products = {
            1: ("Milk", 20),
            2: ("Bread", 15),
            3: ("Eggs", 5),
            4: ("Butter", 45),
            5: ("Cheese", 50),
            6: ("Juice", 30),
            7: ("Chips", 10),
            8: ("Chocolate", 25)
        }

    def display_products(self):
        print("\nAvailable Products:")
        print("Code\tProduct\tPrice")
        for code, (product, price) in self.products.items():
            print(f"{code}\t{product}\t\t{price} Rs.")
    
    def generate_bill(self):
        total_amt = 0
        bill_details = []

        while(True):
            try:
                code = int(input("Enter Product Code (Or 0 to Finish)"))
                if code == 0:
                    break

                if code not in self.products:
                    print("Invalid Code. Please try again")
                    continue

                quantity = int(input(f"Enter Quantity For {self.products[code][0]} : "))
                if quantity <= 0:
                    print("Quantity Should Be Positive.")
                    continue

                product_name, price = self.products[code]
                amount = price * quantity
                total_amt += amount
                bill_details.append((product_name, quantity, price, amount))
            
            except ValueError:
                print("Invalid Input. Please Enter Numeric Values Only")
        self.print_bill(bill_details, total_amt)

    def print_bill(self, bill_details, total_amt):
        print("\n-----Bill Summary----")
        print("Product\tQuantity\tPrice\tAmount")
        for name, quantity, price, amt in bill_details:
            print(f"{name}\t{quantity}\t\t{price}\t{amt} Rs.")
        print(f"Total Amount : {total_amt} Rs.")

store = Store()
store.display_products()
store.generate_bill()