from module import*
users=["Liza"]
passwords=["132465"]

while True:
    print("Reg-1, Avt-2, Välja-3")
    v=int(input())
    if v==0:
        from module import*
    elif v==1:
        print("Registreerimine")
        register(users,passwords)
    elif v==2:
            print("Autoriseerimine")
#Autoriseerimine teeme
    elif v==3:
        print("Välja")
#valmis
    else:
        print("On vaja valida 1,2 või 3")#kõik on olemas
