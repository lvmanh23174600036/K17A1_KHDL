import math
#bài 1
a = max(3,2,2,4,5,7,4,3,54,2,432,3)
b = min(3,2,2,4,5,7,4,3,54,2,432,3)
print("giá trị lớn nhất là:",a)
print("giá trị nhỏ nhất là:",b)

#bài 2
x = eval(input("nhập số x:"))
gia_tri_tuyet_doi = abs(x)
print("giá trị tuyệt đối của x là:",gia_tri_tuyet_doi)

#bài 3
x = eval(input("nhập giá trị x:"))
n = eval(input("nhập giá trị n:"))
s = (pow(x,2)+1)*n
print("kết quả của s là:",s)

#bài 4
x = eval(input("nhập số x:"))
n = eval(input("nhập số n:"))
A = pow((pow(x,2) +1),n) + pow((pow(x,2)- 1),n)
print("kết quả của a là:",A)

#bài 5
def zip_code(x):
    if len(x) != 6:
        return False
    else:
        return True
x = eval(input("nhập số x:"))
print(zip_code(x)) 

#bài 6
a = eval(input("nhập giá trị a:"))
b = eval(input("nhập giá trị b:"))
c = eval(input("nhập giá trị c:"))
import math
delta = b**2 - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm.")
elif delta == 0:
    x = -b / (2*a)
    print(f"Phương trình có nghiệm kép x = {x}.")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}.")

#bài 7
s = "   a b c d e f duck   "
s_sub = "d"
s_find = "duck"
s_replace = "dog"
print(s.center(0," "))
print("số lần s_sub xuất hiện trong s là:",s.count(s_sub,1,20))
print("hàm thay thế vào s là:",s.replace("duck",s_replace))

#bài 8
ngay = eval(input("nhập ngày:"))
thang = eval(input("nhập tháng:"))
nam = eval(input("nhập năm:"))
print("ngày tháng năm vừa nhập:",ngay,"-",thang,"-",nam)
if (nam %4 == 0 and nam % 100 !=0) or nam % 400 == 0:
        print(nam,"là năm nhuận")
else :
        print(nam,"không phải năm nhuận")