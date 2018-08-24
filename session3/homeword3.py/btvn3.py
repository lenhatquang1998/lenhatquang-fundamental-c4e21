import random
ten = ['c', 'h', 'a', 'm','p', 'i', 'o', 'n']
random.shuffle(ten)
print(*ten, sep=" ")
chars = input("Your answer: ")
if chars == "champion":
    print("hura")
else :
    print(":(")