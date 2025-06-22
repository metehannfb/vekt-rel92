try:
    a =  5000
    b =  "6000"
    print (a+b)
except Exception as aa:
    print("Hata oluştu")
    print("Hata kodu:",aa)
    if str(aa) == "unsopported operand type(s)for +: 'int' and 'str'" :
        print("+ işlemi için  ikiside string yada ikiside int olmalı." )