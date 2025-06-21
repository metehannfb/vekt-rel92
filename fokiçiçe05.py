import datetime
saat = int(datetime.datetime.now().strftime("%H"))
def selamlar():
    def sabah():
        return"Günaydın.saat:" + str(saat)
    def ogle(): 
        return"iyi günler. Saat:" +str(saat)+":"+datetime.datetime.now().strftime("%M")
    print("Merhaba",sabah() if saat<9 else ogle())
selamlar()