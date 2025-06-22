try:
    print(10/0)
except Exception as hata:
     print("Hata oluştu")
     print("hata kodu:",hata)
     if str(hata) == "division by zero":
      print("Bölme işleminde bölen 0 olmamalı.")
input()     