import time
d = open("evalexec05.py")
o = d.readlines()
for aa in o:
    # print(a)
    # eval(aa)
    exec(aa)
    time.sleep(10)