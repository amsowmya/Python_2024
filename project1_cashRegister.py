class CashRegister:

    PRODUCT_LIST = {"Soap": 10, "Shampoo": 5, "Chacolate": 15, "Candy": 2}
    TAX = 0.05
        
    def __init__(self):
        self._items = {}
    
    # @items.deleter
    # def items(self):
    #     print("Delete all the items")
    #     self._items = None

    def add_product(self, product):
        if product in CashRegister.PRODUCT_LIST:
            if product in self._items:
                self._items[product] += 1
            else:
                self._items[product] = 1 

    def remove_product(self, product):
        if product in self._items:
            self._items[product].remove() 

    def show_product(self):
        for item in self._items.keys():
            print(item)
    
    def print_bill(self):
        bill = {}
        total_price = 0
        for item in self._items.keys():
            no_of_prod = self._items[item]
            price = CashRegister.PRODUCT_LIST[item]
            price += no_of_prod * price
            total_price += price
            bill[item] = price
        bill['Total price: '] = total_price
        return bill

    def find_total_amount(self):
        total_price = 0
        for item in self._items.keys():
            no_of_prod = self._items[item]
            price = CashRegister.PRODUCT_LIST[item]
            total_price += no_of_prod * price
        return total_price 

    def find_total_with_tax(self):
        amount = self.find_total_amount()
        amount_with_tax = (amount * CashRegister.TAX) + amount
        return amount_with_tax

cash = CashRegister()

cash.add_product("Shampoo")
cash.add_product("Soap")
cash.add_product("Chacolate")

cash.show_product()

amount = cash.find_total_amount()
print("Total amount : ", amount)

amount_with_tax = cash.find_total_with_tax()
print("Total amount with tax: ", amount_with_tax)

# del cash.items 

cash.show_product()
bill = cash.print_bill()
print(bill)