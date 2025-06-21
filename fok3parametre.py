kayitNo = 1
def kayit_olustur(ad,soyad,numara):
    global kayitNo
    print(f"\n{kayitNo}.kayıt oluşturuldu.")
    print(f"Soyad:{soyad} Ad:{ad} Numara:{numara}\n")
    kayitNo+=1

kayit_olustur("metehan","bölükbas","338")
kayit_olustur("338","bölükbas","metehan")
kayit_olustur("metehan",numara="338",soyad="bölükbas") 