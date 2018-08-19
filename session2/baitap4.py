print("pt co dang: ax2+bx+c=0")
a=int(input("moi nhap so a:"))
b=int(input("moi nhap so b:"))
c=int(input("moi nhap so c:"))
denta=b**2-4*a*c
if denta > 0:
    x1=(-b+denta*1/2)/2*a
    x2=(-b-denta*1/2)/2*a
    print("co 2 nhiem phan biet",x1,x2)
elif denta == 0:
    x=(-b)/2*a
    print("co mot nghiem duy nhat",x)
else :
    print("pt vo nghiem")