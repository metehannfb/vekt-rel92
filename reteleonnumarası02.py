import re
telefon = input("telefon numarsı girin")
desen = r"^0[5][0-9]{9}$"
if re.fullmatch(desen,telefon):
    print("telefon numarsı geçerli.")
    print("11 haneli, 0 ile başlayan ve rakamlardan oluşan numara giriniz.")

