def loe_failist(file:str)->str:
    """Loeme tekst failist
    """
    f=open(file,"r") #f=file
    stroka=f.readlines() #str
    f.close()
    return stroka #list
stroka=loe_failist("TextFile1.txt")
print(stroka)
def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    f=open(file,"r")
    list_=[]
    for str in f:
        list_.append(str.strip()) #strip-поиск символа и удаление его, append-добавление к списку
        f.close()
        return list_
spisok=loe_failist_listisse("TextFile1.txt")
print(spisok)

def salvesta_failisse(file:str):
    """Salvesta text failisse
    """
    f=open(file,"a")
    text=input("Sisesta text:")
    f.write(text+"\n")
    f.close()

for i in range(10):    #повторение
    salvesta_failisse("Loetelu.txt")

def faili_sisu_umberkirjutamine(file:str):
    text=input("Sisesta uus text:")
    with open(file,"w") as f:
        f.write(text+"\n")

faili_sisu_umberkirjutamine(input("TextFile1.txt")