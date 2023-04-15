n=int(input("nhap vao so co dinh: "))
m=int(input("Nguoi dung nhap so: "))
dem=0
while m!=n:
    dem+=1
    if(m<n):
        print("So cua ban nho hon !!!")
    else:
        print("So cua ban lơn hon !!!")
    m=int(input("Nguoi dung nhap so: "))
else:
    print("So lan la : ",dem)