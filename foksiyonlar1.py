# def selamlar():
#     print("="*10,"Metehan","="*10)
#     print(" "*10,"nasılsın\n")
# selamlar()
# selamlar()


# def selamlar(xx):
#     print("="*10,xx,"="*10)
#     print(" "*10,"nasılsın\n")    
# selamlar("selam")
# selamlar("merhaba")

def selamlar(xx):
    return f"{'='*10} {xx} {'='*10} \n {""*10}nasılsın\n"

selamlar("selam")
print(selamlar("merhaba"))