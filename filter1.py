sayilar = [11,22,3,6,7,8,9]
def tekMi(xx):
    if xx%2==0: return "çift"
    else: return "tek"

yeniDizi=[]
for a in sayilar:
    yeniDizi.append(tekMi(a))
print("sayilar: ",sayilar)
print("yeniDizi:",yeniDizi)