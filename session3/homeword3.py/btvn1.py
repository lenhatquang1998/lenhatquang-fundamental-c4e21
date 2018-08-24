menu = ["T-Shirt", "Sweater"]
while True :
    command = input("ban muon gi ( C, R, U, D)?").upper()
    if command == "C":
        new = input("ban muon them gi` ?")
        menu.append(new)
        print(*menu, sep=", ")
    elif command == "R":
            print(*menu, sep=", ")
    elif command == "U":
        n = int(input("ban muon thay doi muc may?"))
        new2 = input("ban muon thay doi thanh gi?")
        menu[n-1] = new2
        print(*menu, sep=", ")
    else :
        m = int(input("ban muon xoa muc may?"))
        menu.pop(m-1)
        print(*menu, sep=", ")