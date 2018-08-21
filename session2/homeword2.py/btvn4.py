x=int(input("ban cao bao nhieu (cm)?:"))
y=int(input("ban nang bao nhieu kg ?"))
a = x/100
BMI = y/(a**2)
if BMI < 16:
    print("giam can nang")
elif 16 <= BMI <= 18.5 :
    print("thieu can")
elif 18 < BMI < 25:
    print("binh thuong")
elif 25 <= BMI <= 30:
    print("beo phi")
else :
    print("beo phi")