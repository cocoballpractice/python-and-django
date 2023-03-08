class Person:
    
    money=0
    
    def __init__(self, money):
        self.money = money
        
    def get_money(self):
        return self.money
    
    def minus_money(self, money):
        self.money -= money
        
    def use_vending_machine(self, v):
        vp = v.get_price()
        vs = v.get_stock()
        pm = self.get_money()
    
        if vs >= 1:
            if pm >= vp:
                print("[System] 자판기를 이용합니다. 커피의 가격은 " + str(vp) +"원 입니다.")
                self.minus_money(vp)
                v.minus_stock(1)
                pm = self.get_money()
                vs = v.get_stock()
                print("[Info] 커피 구매 후 잔액 : " + str(pm) +"원")
                print("[Info] 자판기 남은 커피 재고 :", vs)
            else:
                print("[Error] 잔액이 부족하여 커피를 구매할 수 없습니다")
        else:
            print("[Error] 재고가 부족하여 커피를 구매할 수 없습니다")