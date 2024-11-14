# Write a python program that has a class store which keeps a record of code and prices of each product. 
# Display a menu of all products to the user and prompt him/her to enter the quantity of each item required. 
# Generate a bill and display the total amount 

class Store:
    def __init__(self):
        # Initialize a dictionary with product codes as keys and (name, price) as values
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
        print("Code\tProduct\t\tPrice")
        for code, (name, price) in self.products.items():
            print(f"{code}\t{name}\t\t{price} Rs.")
    
    def generate_bill(self):
        total_amount = 0
        bill_details = []
        
        while True:
            try:
                code = int(input("\nEnter the product code (or 0 to finish): "))
                
                if code == 0:
                    break
                
                if code not in self.products:
                    print("Invalid product code. Please try again.")
                    continue
                
                quantity = int(input(f"Enter quantity for {self.products[code][0]}: "))
                if quantity <= 0:
                    print("Quantity should be positive.")
                    continue
                
                product_name, price = self.products[code]
                amount = price * quantity
                total_amount += amount
                bill_details.append((product_name, quantity, price, amount))
            
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
        
        self.print_bill(bill_details, total_amount)
    
    def print_bill(self, bill_details, total_amount):
        print("\n--- Bill Summary ---")
        print("Product\t\tQuantity\tPrice\tAmount")
        for name, quantity, price, amount in bill_details:
            print(f"{name}\t\t{quantity}\t\t{price}\t{amount} Rs.")
        print("\nTotal Amount:", total_amount, "Rs.")

# Instantiate the Store and run the billing process
store = Store()
store.display_products()
store.generate_bill()