try:
    s1 = int(input("1.Sayıyı giriniz"))
    s2 = int(input("2.Sayıyı giriniz"))
    if s1>100 or s1>100:
        raise TypeError("sayılar 0-100 arasında olmalı")
    else:
        işlem =input ("yapılcak işlem nedir? (+,-,*,/)")
        if işlem == "+" : print("sonuç:",s1+s2)
        elif işlem == "/" : print("sonuç:",s1/s2)  
except Exception as xx:
     print("Hata mesaji", xx)     