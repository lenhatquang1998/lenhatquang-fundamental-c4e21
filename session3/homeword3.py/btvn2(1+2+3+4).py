size = [5, 7, 300, 90, 24, 50, 75]
print("hello, my name is Nhat Quang and these are my ship sizes",size)         # phan 1
print("bay gio con cuu lon nhat cua toi co kich thuoc", max(size), "hay thit no'")        #phan 2
size[size.index(max(size))] = 8                                                 # phan 3
print("sau khi thit, dan cuu cua toi la`:", size)
for i in range(len(size)):                                        # phan 4
    size[i] = size[i] + 50
print("sau mot thang dan cuu cua toi la:", size)