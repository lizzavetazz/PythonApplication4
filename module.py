def koik_kasutajad(users,passwords):
    i=0
    for user in users:
        print(user,end="-")
        print(passwords[i])
        i+=1

def passautomat()->str:
    """Пароль создается машиной
    """
    str0="*/!"
    str1="0123456789"
    str2="qwertyuiopasdfghjklzxcvbnm"
    str3=str2.upper() #все знаки со str2 заглавными 
    str4=str0+str1+str2+str3
    ls=list(str4) #список [".",",",":",";"...]
    random.shuffle(ls) #перемешиваем
#извлекаем из списка 12 рандомных символов
    psword="".join([random.choise(ls) for x in range(12)])
#psword on valmis
    return psword
def paskontroll(psword: str)->bool:
    ls=list(psword)
    for e in ls:
        if e.isdigit(): d=True
        if e.isalpha(): a=True
        if e.isupper(): u=True
        if e in islower():l=True
        if e in list("*/!"): s=True
    if d==True and a==True and u==True and l==True and s==True:
        t=True
    else:
        t=False
    return t
def register(users:list,passwords:list):
    while 1:
        log=input("Kasutajatunnus")
        if log not in users:
            print("Tunnis sobib")
            break
        else:
            print("See nimi juba on olemaas listis")
            v=input("Arvuti-A või ise-Iloob parool")
            if v.upper()=="A":
                pas=passautomat()
            elif v.upper()=="I":
                    while 1:
                        pas=input("Sisesta oma parool")
                        tulemus=(pas)
                        if tulemus==True:
                            users.append(log)
                            passwords.append(pas)
                            break