from TheCustomer import Customer
from TheItem import Item
from TheCashier import Cashier

cart = {}
userId = 0

def displayItems(char):
    for i in itemsList:
        if i.id[0] == char:
            print(i.id,i.name,i.price)


c1 = Customer("Ali","Hassan",123,"ali123",123456)
c2 = Customer("Khaled","Hassan",444,"kaled123",123456)
c3 = Customer("Rami","Nael",555,"rami123",123456)
customersList = [c1,c2,c3]

i1 = Item("T123456",'sharp',500)
i2 = Item("T452221",'sony',350)
i3 = Item("C123456",'hp',600)
i4 = Item("D123456",'sony',200)
i5 = Item("T578541","Panasonic",500)
i6 = Item("T852147","LG",500)
i7 = Item("T789654","Samsung",400)
i8 = Item("C718234","Dell",400)
i9 = Item("C789654","Sony",400)
i10 = Item("C789654","Acer",400)
i11 = Item("C789654","Lenovo",400)
i12 = Item("C789654","Toshiba",400)
i13 = Item("D789654","Samsung",400)
i14 = Item("D789654","Panasonic",400)
i15 = Item("D789654","Canon",400)
i16 = Item("V789654","Sony",400)
i17 = Item("V789654","Philips",400)
i18 = Item("V789654","Toshiba",400)
itemsList = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18]

def login():
    global cart
    global userId
    global q
    while True:
        userName = input("Enter username: ")
        password = int(input("Enter Password: "))
        flag = False
        for cust in customersList:
            if cust.userName == userName and password == cust.password:
                flag = True
                customerName = cust.firstName + " " + cust.lastName
                userId = cust.id
                cart[userId] = []
                break
        if flag == True:
            print("Welcome " + customerName)
            break
        else:
            print("userName/password error")
login()

print("1- TV\n2- Computers\n3- DVD\n4- Digital Camera\n5- go to the cashier")
ch = int(input('Your Choice: '))
while True:
    if ch == 1:
        displayItems('T')
    elif ch == 2:
        displayItems('C')
    elif ch == 3:
        displayItems('V')
    elif ch == 4:
        displayItems('D')
    elif ch == 5:
        break
    elif ch == 6:
        def deletecust():
            print("^ delete item - customer ^\n1-for delete all item\n2-for delete item in index 0\n3-for delete item in index 1"
                  "\n4-for delete item in index 2\n5-for delete item in index 3\n6-for delete item in index 4\n7-Exit")
            print(cart)
            deleted = input("Enter choice")
            for i in deleted:
                if deleted == "1":
                    del cart[userId]
                elif deleted == "2":
                    del cart[userId][0]
                elif deleted == "3":
                    del cart[userId][1]
                elif deleted == "4":
                    del cart[userId][2]
                elif deleted == "5":
                    del cart[userId][3]
                elif deleted == "6":
                    del cart[userId][4]
                elif deleted == "7":
                    break
                continue
        deletecust()
        delete = input("contine? [y/n]")
        if delete == "n":
            print(cart)
            print("1- TV\n2- Computers\n3- DVD\n4- Digital Camera\n5- go to the cashier\n6- delete item ")
            ch = int(input('Your Choice: '))
        elif delete == "y":
            deletecust()

    itemId = input("Enter Item's id:")
    q = input("Quantity:")
    p = 1500
    cart[userId].append([itemId,q])
    print(cart)
    inp = input("Contine?[y/n]:")
    if inp == "n" or inp == "N":
        print("1- Tv\n2- Computers\n3- DVD Players\n4- Digital Camera\n5- go to the cashier\n6-delete item")
        ch = int(input("Your choice:"))
def deletecash():
                print("^ delete item - cashier ^\n1-for all item\n2-for delete item in index 0\n3-for delete item in index 1"
                        "\n4-for delete item in index 2\n5-for delete item in index 3\n6-for delete item in index 4\n7-Exit")
                print(cart)
                deleted = input("Enter choice")
                for i in deleted:
                    if deleted == "1":
                        del cart[userId]
                    elif deleted == "2":
                        del cart[userId][0]
                    elif deleted == "3":
                        del cart[userId][1]
                    elif deleted == "4":
                        del cart[userId][2]
                    elif deleted == "5":
                        del cart[userId][3]
                    elif deleted == "6":
                        del cart[userId][4]
                    elif deleted == "7":
                        break
while True:
    username = input("username for cashier:")
    password = int(input("password for cashier:"))
    use = "ahmadAlaga"
    passs = 123456
    if username == use and password == passs:
        print("1- displayCart\n2- delete")
        x = input("Enter choice cashier :")
        for i in x:
            if x == "1":
                print("displayCart", cart)
                print("1- displayCart\n2- delete ")
            elif x == "2":
                deletecash()
                print("1- displayCart\n2- delete")
    else:
        print("userName/password error")