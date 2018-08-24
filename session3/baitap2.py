menu = ["com rang", "bun bo", "bun dau"]
for idex, item in enumerate (menu):
    print(idex+1, ". ", item, sep="")
print("*"*10)
n = int(input("vi tri ban muon thay doi:"))
new = input("ban muon thay bang gi:" )
menu[n-1] = new
print("*"*10)
for idex, item in enumerate(menu):
    print(idex+1, ". ", item, sep="")