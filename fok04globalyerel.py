xx = 11
def foksiyon1():
    global xx
    xx= 22
    print("yereldeki:",xx)
    def ictekiFonksiyon():
     global xx
     xx = 33
    print("İçteki fonksiyon:",xx)
    ictekiFonksiyon()
    print("Yereldeki2:",xx)
foksiyon1()
print("Globaldeki:",xx)
