name = {
    "ngoc": "ny cua manh",
    "manh": "con trai quang",
    "le": "chi manh",
}
while True:
    key = input("ban muon tra cuu gi ?")
    if key in name:
        print(name[key])
    else :
        print("k biet:")
        a = input("ban muon bo sung k ? yes or no ")
        if a == "yes":
            new = input("moi ban nhap du lieu: ")
            new2 = input("gia thich? ")
            name[new] = new2
            print("them du lieu thanh cong")
        elif a == "no":
            print("ok")