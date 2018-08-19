yob=int(input("your year of birth? "))
age = 2018 - yob
print("your age:", age)

if age < 10:
    print("baby")
elif age < 18:
    print("teenager")
else:
    print("adult")