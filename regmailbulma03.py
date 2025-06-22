import re
def anaekran():
    eposta = input("eposta girin: ")

    # +90 ile başlayan, sonra 5 ve 9 rakamdan oluşan GSM numarası
    desen = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    if re.fullmatch(desen, eposta):
        print("eposta geçerli.")
    else:
        print("Geçersiz eposta. Kurallar uygun bir eposta giriniz.")
    anaekran()

anaekran() 
