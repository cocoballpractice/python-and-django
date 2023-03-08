import Person
import VendingMachine

p_money = int(input("당신이 소지한 금액을 입력해주세요"))
v_info = list(map(int, input("자판기의 커피 재고와 가격을 '재고 가격' 형식으로 적어주세요 (예시 : 20 500)").split(' ')))

p = Person.Person(p_money)
v = VendingMachine.VendingMachine(v_info[0], v_info[1])

pm = p.get_money()
vs = v.get_stock()
vp = v.get_price()

print("설정한 소지금 :", pm)
print("설정한 자판기의 커피 재고와 가격 :", vs, vp)

while True:
    question = input("커피를 구매하시겠습니까? : 예(Y) / 아니오(N)")
    if question == "Y":
        p.use_vending_machine(v)
    elif question == "N":
        print("[System] 이용해주셔서 감사합니다 안녕히 가세요")
        break
    else:
        print("[Error] 잘못된 입력입니다.")