nhap = input("nhap: ").lower()
a = list(nhap)
counts = {}

for i in a:
    if a != " ":
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1

counts = sorted(counts.items())

for count in counts:
    print(count[0], "", count[1])