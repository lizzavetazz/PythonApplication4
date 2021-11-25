from module import*
users=loe_failist_listisse["users.txt"]
passwords=loe_failist_listisse["passwords.txt"]

while True:
    print("Näita kõike-0, Reg-1, Avt-2, Välja-3")
    v=int(input())
    if v==0: 
        koik_kasutajad(users, passwords)
    elif v==1:
        print("Registreerimine")
        register(users,passwords)
    elif v==2:
            print("Autoriseerimine")
            if password.index(pas)==users.index(user):
                print("Tere tuleemast!")


#Autoriseerimine teeme
    elif v==3:
        print("Välja")
        faili_sisu_umberkirjutamine("users.txt", users)
        faili_sisu_umberkirjutamine("passwords.txt", passwords)
#valmis
    else:
        print("On vaja valida 1,2 või 3")#kõik on olemas
