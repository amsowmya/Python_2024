class CashRegister:
    TAX_DECIMAL = 0.05

    def __init__(self, cashier):
        self.cashier = cashier
        self.products = {} 

    def add_products(self, new_product, quantity=1):
        self.products[new_product["name"]] = {
            "price": new_product["price"],
            "quantity": quantity
        }

    def show_products(self):
        print(self.products)
    
    def remove_products(self, product):
        del self.products[product]

    def update_price(self, product, new_price):
        self.products[product]['price'] = new_price 

    def find_subtotal(self):
        subtotal = 0
        for product_info in self.products.values():
            subtotal += product_info['price'] * product_info['quantity']
        return subtotal
    
    def print_subtotal(self):
        print(self.find_subtotal())

    def find_taxes(self):
        return round(self.find_subtotal() * CashRegister.TAX_DECIMAL, 2)

    def print_taxes(self):
        print(f"Taxes: {self.find_taxes()}")

    def find_total(self):
        return round(self.find_subtotal() + self.find_taxes(), 2)
    
    def print_total(self):
        print(f"Total bill is : {self.find_total()}")

    def clear_product(self):
        self.products.clear()

# create an instance
my_cash_register = CashRegister("Joe")

# create the products
product_1 = {"name": "Pizza", "price": 10.2}
product_2 = {"name": "Chacolate", "price": 15}
product_3 = {"name": "Soap", "price": 12}

# add the product
my_cash_register.add_products(product_1)
my_cash_register.add_products(product_2, 2)
my_cash_register.add_products(product_3, 3)

# show products 
my_cash_register.show_products()

# Remove a product
my_cash_register.remove_products("Pizza")
my_cash_register.show_products()

# update the price of a product
my_cash_register.update_price("Chacolate", 20)
my_cash_register.show_products()

# Print the subtotal toal and tax
my_cash_register.print_subtotal()
my_cash_register.print_taxes() 
my_cash_register.print_total() 

# Clear the purchase 
my_cash_register.clear_product()
my_cash_register.show_products()
