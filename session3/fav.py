menu = ['bun ga', 'bun cha', 'bun nem']

while True :
    command = input("what you you want (C, R, U, D)?").upper()
    if command == "C":
        new = input("New item?")
        menu.append(new)
        print(menu)

    elif command == "R":
        for i, item in enumerate(menu):
            print(i+1, item)

    elif command == "U":
        n = int(input("ban muon thay doi so may"))
        new2 = input("ban muon thay doi la gi? ")
        menu[n-1] = new2
        print(menu)
    else :
        a = int(input("ban muon xoa gi ?"))
        menu.pop(a-1)
        print(menu)