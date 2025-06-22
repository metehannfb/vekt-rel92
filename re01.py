import re
xx = "ahmet al rekli bir şal aldi."
print(re.findall("al",xx))
print(re.findall("şal",xx))
print("\"al\" ifadesine göre böl:",re.split("al", xx))
print("boşluklara göre böl:",re.split(" ",xx))
print("Bütün boşlukları \"zzz\" ile değiştir:",re.sub("güzel", "iyi", xx))
print("Bütün \"güzel\" ifadelerini \"iyi\" ile değiştir:",re.sub(" ", "zzz", xx)) 