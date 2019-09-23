from class_db import *
from colorama import init
from colorama import Fore, Back, Style
init()

dataBase = db()

newContact = list()

#router
def query(data):
    if data == 'help':
        return print(Fore.BLUE + "Add record: name email phone adress\n"
                     "Select record: name/email/phone/adress={...} [or all, example: *=*]\n"
                     "Delete record: del name/email/phone/adress={...}\n"
                     "Update record: upd name/email/phone/adress={...} (where) name/email/phone/adress={...} [example: upd email=newemailjessi@mail.com name=Jessi]\n"
                                 "Close note: press Space and Enter")
    if 'del' in data:
        listAgr = data.split('=')
        listAgr[0] = listAgr[0][4:]
        dataBase.deleteRecord(listAgr[0], listAgr[1])
        return print(Fore.RED + 'Done')
    if 'upd' in data:
        listAgr = data.split(' ')
        listAgr.pop(0)
        secondListAgr = list()
        for x in range(len(listAgr)):
            secondListAgr.append(listAgr[x].split('='))
        dataBase.updateRecord(secondListAgr[0][0], secondListAgr[0][1], secondListAgr[1][0], secondListAgr[1][1])
        return print(Fore.YELLOW + 'Done')
    if '=' in data:
        listAgr = data.split('=')
        result = dataBase.selectRecord(listAgr[0], listAgr[1])
        for x in range(len(dataBase.selectRecord(listAgr[0], listAgr[1]))):
            print(Fore.GREEN + str(result[x]))
    else:
        if data == ' ':
            exit(Fore.MAGENTA + 'Close note contact')
        countContact = data.split(' ')
        for x in countContact:
            newContact.append(x)
        dataBase.creatRecord(newContact)
        print(Fore.LIGHTGREEN_EX + 'Done')

if __name__ == "__main__":
    while True:
        data = input()
        query(data)
        print(Fore.RESET + Back.RESET + Style.RESET_ALL)  