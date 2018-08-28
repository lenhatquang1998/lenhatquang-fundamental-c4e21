prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
name = ["banana", "apple", "orange", "pear"]
for i in name:   
    print(i)
    print("prices:", prices[i])
    print("stock:", stock[i])
    print()

total = 0
for j in name:
    tich = prices[j]*stock[j]
    print(j, "tich:", tich)
    total += tich
print("tong tien kiem duoc:", total, "$")

   