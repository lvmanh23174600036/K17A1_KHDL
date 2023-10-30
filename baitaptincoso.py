#BÀI TẬP 1.1
print("bài tập 1.1")
print("**    **    ********    **        **        ******")
print("**    **    **          **        **        **  **")
print("********    ********    **        **        **  **")  
print("**    **    **          **        **        **  **")
print("**    **    ********    *******   *******   ******")
#BÀI TẬP 1.2
print("bài tập 1.2") 
x=10
y=5
c=x+y
d=x-y
e=x*y
f=x/y
print('Tổng của' , x, '+', y, '=', c)
print('Hiệu của', x, '-', y, '=', d)
print("tích của", x,"x",y, "=",e )
print("Thương của",x,"/",y,"=",f )
#BÀI TẬP 1.3
print("bài tập 1.3")
ten_hang="sữa hộp Vina milk"
so_luong=5
don_gia=25000
tien_phai_tra=so_luong*don_gia
print("tên hàng:",ten_hang)
print("số lượng:",so_luong)
print("đơn giá:",don_gia)
tien_phai_tra = so_luong*don_gia
print("tiền phải trả:",tien_phai_tra,"vnđ")
#BÀI TẬP 1.4
print("bài tập 1.4")
import math
a=int(input("Nhập cạnh tam giác thứ nhất:"));
b=int(input("Nhập cạnh tam giác thứ hai:"));
c=int(input("Nhập cạnh tam giác thứ ba:"));
cv=a+b+c
p=cv/2
dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Chu vi = ", cv)
print("Diện tích = ", dt)
