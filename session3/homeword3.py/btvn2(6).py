size = [5, 7, 300, 90, 24, 50, 75]
print("hello, my name is Nhat Quang and these are my ship sizes",size)   
n = int(input("ban muon thay dan cuu cua ban sau may thang?:"))
for i in range(1, n):
    print("THANG", i)
    for i in range(len(size)):                                      
        size[i] = size[i] + 50
    print("dan cuu cua toi la:", size)
    print("bay gio con cuu lon nhat cua toi co kich thuoc", max(size), "hay thit no'")
    size[size.index(max(size))] = 8                                      
    print("sau khi thit, dan cuu cua toi la`:", size)
print("THANG",n)
for i in range(len(size)):                                      
        size[i] = size[i] + 50
print("dan cuu cua toi la:", size)
tong = sum(size)
print("dan cua toi co tong kich thuoc:", tong)
tien = tong*2
print("i would get", tong, "*", "2$ =", tien, "$")
