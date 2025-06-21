sayilar = [11,22,3,6,7,8,9]
def tekMi(xx):
    if xx%2!=0: return False
yeniDizi=list(filter(tekMi,sayilar))
print("sayilar:",sayilar)
print("yeniDizi:",yeniDizi)