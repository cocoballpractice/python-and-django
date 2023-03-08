class VendingMachine:
    
    stock=0
    price=0
    
    def __init__(self, stock, price):
        self.stock = stock
        self.price = price
        
    def get_price(self):
        return self.price
        
    def get_stock(self):
        return self.stock
    
    def minus_stock(self, stock):
        self.stock -= stock