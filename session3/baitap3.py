menu = ["pho ga", "pho bo", "bun dau", "com rang"]
for idex, item in enumerate(menu):
    print(idex+1,". ", item, sep="")
print("*"*10)
# n = int(input("ban muon xoa vi tri nao? "))
m = input("ban muon xoa noi dung nao? ")
# menu.pop(n-1)
if m in menu:
    menu.remove(m)
else :
    print("k co")
print("*"*10)
for idex, item in enumerate(menu):
    print(idex+1, ". ", item, sep="")