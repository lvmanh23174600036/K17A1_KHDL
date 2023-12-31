#BAITAP1
def sign(x) :
    if x < 0 :
        return -1

    if x > 0 :
        return 1

    if x == 0:
        return 0
x = int(input("nhap so x:"))
print(sign(x))
#BAITAP2
def tinh_can(nam):
    can = ["canh",'tân','nhâm','quý','giáp','ất','bính','đinh','mậu','kỉ']
    return can [nam % 10]
def tinh_chi(nam):
    chi = ["thân",'dậu','tuất','hợi','tý','sửu','dần','mão','thìn','tị','ngọ','mùi']
    return chi [nam % 12]
nam_duong_lich = int(input("nhập năm dương lịch:"))
can = tinh_can(nam_duong_lich)
chi = tinh_chi(nam_duong_lich)
nam_am_lich = can + " " + chi
print("năm",nam_duong_lich,"dương lịch tương đương với",nam_am_lich,"năm âm lịch")
#bài tập 3
def bmi(cannang: float,chieucao: float) -> float:
    chi_so_bmi = cannang/ (chieucao ** 2)
    if chi_so_bmi < 18.5:
        print("theo đánh giá bmi cho thấy bạn đang gầy")
    elif 18.5 <= chi_so_bmi <= 24.99:
        print("theo đánh giá bmi cho thấy bạn đang cân đối")
    else:
        print("theo đánh giá bmi cho thấy bạn đang thừa cân")
    return chi_so_bmi
chieucao = float(input("nhập số chiều cao:"))
cannang = float(input("nhập cân nặng:"))
print(bmi(cannang,chieucao))
#bài tập 4
def tinh_S(n,x) :
    s = ((x**2)+1)**n
    return s
n = int(input("nhập số n:"))
x = int(input("nhập số x:"))
print(tinh_S(n,x))
#bài tập 5
def tinh_A(n,x):
    A = (x**2 + x +1)**n + (x**2 - x + 1)**n
    return A
n = int(input("nhập số n:"))
x = int(input("nhập số x:"))
print(tinh_A(n,x))
#bài tập 6
def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
           print("x không phải sô nguyên tố")
           return False
    print("x là số nguyên tố")
    return True
    
x = int(input("nhập sô x:"))
print(la_so_nguyen_to(x))
#bài tập 7 #viết hàm trả về phần nguyên của 2 số nguyên
def remainder(a: int, b: int) -> int:
    return a % b
a = int(input("nhập số a:"))
b = int(input("nhập số b:"))
print(remainder(a,b))
#bài tập 8
def perfect_num(n) :
    total = 0 
    for i in range(1,n):
        if n % i == 0:
            total += i
    if total == n:
            return "là số hoàn hảo"
    else:
            return "không phải số hoàn hảo"
n = int(input("nhập số n:"))
print(perfect_num(n))
#bài tập 9
area = lambda r: 3.14 * r ** 2
perimeter = lambda r : 2*3.14*r
area = lambda a,b : a*b
perimeter = lambda a,b : 2* (a+b)
r = int(input("nhập bán kính:"))
circle_area = area(r)
circle_perimeter = perimeter(r)
print("diện tích của hình tròn là:",circle_area)
print("chu vi của hình tròn là:",circle_perimeter)
a = int(input("nhập chiều dài hình chữ nhật:"))
b = int(input("nhập chiều rộng hình chữ nhật:"))
rectangcle_area = area(a, b)
rectangcle_perimeter = perimeter(a, b)
print("diện tích của hình chữ nhật là:",rectangcle_area)
print("chu vi của hình chữ nhật là:",rectangcle_perimeter)