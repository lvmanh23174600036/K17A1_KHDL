#BÀI TẬP 8.1
print("BÀI TẬP 8.1")
a=int(input("nhập số a:"))
b=int(input("nhập số b:"))
c=int(input("nhập số c:"))
d=int(input("nhập số d:"))
so_be_nhat=min(a,b,c,d)
so_lon_nhat=max(a,b,c,d)
print("min:",so_be_nhat)
print("max:",so_lon_nhat)
#BÀI TẬP 8.2
print("BÀI TẬP 8.2")
x=int(input("nhập số x:"))
gia_tri_tuyet_doi=abs(x)
print("giá trị tuyệt đối của x:",gia_tri_tuyet_doi)
#BÀI TẬP 8.3
print("BÀI TẬP 8.3")
def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print(f"Nghiệm của phương trình là: x = {x}")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
giai_phuong_trinh_bac_nhat(a, b)
#BÀI TẬP 8.4
print("BÀI TẬP 8.4")
a=float(input("Nhập độ dài cạnh a: "))
b=float(input("Nhập độ dài cạnh b: "))
c=float(input("Nhập độ dài cạnh c: "))
p = (a + b + c)
import math
S = math.sqrt(p * (p - a) * (p - b) * (p -c))
print("Diện tích tam giác là: ", S)
#BÀI TẬP 8.5
print("BÀI TẬP 8.5")
nam=int(input("Nhập năm: "))
if nam%4 == 0 and nam%100 > 0 or nam%400 == 0:
	print(nam,"là năm nhuận.")
else:
	print(nam,"không phải là năm nhuận.")
#BÀI TẬP 8.6
print("BÀI TẬP 8.6")
def tinh_cuoc_taxi(loai_xe, so_km, thoi_gian_cho):
    if loai_xe == 4:
        gia_mo_cua = 11000
        gia_dau_km = 12100
        gia_tiep_theo = 10000
    elif loai_xe == 7:
        gia_mo_cua = 13000
        gia_dau_km = 14100
        gia_tiep_theo = 12000
    else:
        return "Loại xe không hợp lệ. Vui lòng nhập lại."
    cuoc_taxi = gia_mo_cua + (so_km - 0.8) * (gia_dau_km if so_km <= 20 else gia_tiep_theo)
    tien_cho = max(0, thoi_gian_cho - 5) * 800
    tong_tien = cuoc_taxi + tien_cho
    return tong_tien
loai_xe1, so_km1, thoi_gian_cho1 = (4, 10, 3)
loai_xe2, so_km2, thoi_gian_cho2 = (7,30 ,10)

tong_tien1= tinh_cuoc_taxi(loai_xe1 ,so_km1 ,thoi_gian_cho1 )
tong_tien2= tinh_cuoc_taxi(loai_xe2 ,so_km2 ,thoi_gian_cho2 )

print("Tổng tiền chuyến đi xe 4 chỗ:", tong_tien1)
print("Tổng tiền chuyến đi xe 7 chỗ:", tong_tien2)
#BÀI TẬP 8.7
print("BÀI KHÓ QUÁ Ạ T_T ")
print("BÀI TẬP 8.7")
def tinh_tien_dien(so_kwh):
    gia_bac_1 = 1678
    gia_bac_2 = 1734  
    gia_bac_3 = 2014  
    gia_bac_4 = 2536   

    if so_kwh <=50:
        tien_dien = so_kwh * gia_bac_1
    elif so_kwh <=100:
        tien_dien = (50 * gia_bac_1) + ((so_kwh-50) *gia_bac_2)
    elif so_kwh <=200:
        tien_dien =(50*gia_bac_1)+(50*gia_bac_2)+((so_kwh-100)*gia_bac_3)
    else:
         tien_dien =(50*gia_bac_1)+(50*gia_bac+2)+(100*giabacb3)+((so-kw-200)*giabacb4)

     return round(tien_dien,2): 
so_kwh = float(input("Nhập số lượng kWh sử dụng: "))
tien_dien = tinh_tien_dien(so_kwh)
print("Tiền điện cần thanh toán là:", tien_dien, "VNĐ")
#BÀI TẬP 8.8
print("BÀI TẬP 8.8")
def tinh_tien_thue_phong(loai_phong, so_dem):
    gia_1_dem = {
        "Standard": 1260000,
        "Superior Garden View": 1550000,
        "Superior Ocean View": 1830000, 
        "Garden View Bungalow": 1830000,
        "Pool View Bungalow": 2120000,
        "Family Room": 2120000,
        "Beach Front Bungalow": 2540000,
        "VIP sea View": 4800000
    }

    if so_dem == 1:
        return gia_1_dem[loai_phong]
    elif so_dem == 2 or so_dem == 3:
        return gia_1_dem[loai_phong] * so_dem * (1 - 0.25)
    else:
        return gia_1_dem[loai_phong] * so_dem * (1 - 0.30)
loai_phong = "Standard"
so_dem = 5
tien_thue_phong = tinh_tien_thue_phong(loai_phong, so_dem)
print("Tiền thuê phòng:", tien_thue_phong)
#BÀI TẬP 8.9
print("BÀI TẬP 8.9")
n=int(input("Nhập n: "))
for i in range(0,n):
	print(n-i)
#BÀI TẬP 8.10
print("BÀI TẬP 8.10")
n = input("Nhập n: ")
x = input("Nhập x: ")
S = (x*x + 1)^n 
print("S = (x*x + 1)^n =", S)
#BÀI TẬP 8.11
print("BÀI TẬP 8.11")
n = input("Nhập n: ")
x = input("Nhập x: ")
A = (x*x + x + 1)^n + (x*x - x + 1)^n
print("A = (x*x + x + 1)^n + (x*x - x + 1)^n","=", A)

#BÀI TẬP 8.12
print("BÀI TẬP 8.12")
a = input("Nhập số: ")
if a%1 == a and a%a == 0: 
	print(a,"là số nguyên tố")
else:
	print(a,"không phải là số nguyên tố")

#BÀI TẬP 8.13
print("BÀI TẬP 8.13")



#BÀI TẬP 8.14
print("BÀI TẬP 8.14")
def tinh_tong(n):
    tong = 0
    for i in range(n):
        so_nguyen = int(input("Nhập số nguyên thứ {}: ".format(i+1)))
        tong += so_nguyen
    return tong

n = int(input("Nhập số lượng số nguyên: "))
ket_qua = tinh_tong(n)
print("Tổng của các số nguyên là:", ket_qua)

#BÀI TẬP 8.15
print("BÀI TẬP 8.15")
while True:
    num = int(input("Nhập một số nguyên (nhập 0 để kết thúc): "))
    
    if num == 0:
        break
    
    total= num

print("Tổng các số đã nhập là:", total)

#BÀI TẬP 8.16
print("BÀI TẬP 8.16")
def UCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
ucln = UCLN(a, b)

print("UCLN của", a, "và", b, "là:", ucln)

#BÀI TẬP 8.17
print("BÀI TẬP 8.17")
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
# Tìm bcLN của a và b
bcln = gcd(a, b)

print("BCLN của", a, "và", b, "là:", bcln)

#BÀI TẬP 8.18
print("BÀI TẬP 8.18")
def is_perfect_number(num):
    if num <= 0:
        return False
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num:
        return True
    else:
        return False

num = int(input("Nhập một số nguyên dương: "))
if is_perfect_number(num):
    print(num, "là một số hoàn hảo.")
else:
    print(num, "không phải là một số hoàn hảo.")

#BÀI TẬP 8.19
print("BÀI TẬP 8.19")
def reverse_and_filter_odd(n):
    numbers = list(range(1, n+1))
    reversed_numbers = numbers[::-1]
    odd_numbers = [num for num in reversed_numbers if num % 2 != 0]
    return odd_numbers

n = int(input("Nhập số lượng phần tử trong dãy: "))
reversed_odd_numbers = reverse_and_filter_odd(n)
print("Dãy số lẻ sau khi đảo ngược là:", reversed_odd_numbers)

#BÀI TẬP 8.20
print("BÀI TẬP 8.20")
import math

def approximate_exp(x):
    n = 1
    approximation = 1 + x**2 / n
    
    while abs(math.exp(x) - approximation) > 1e-4:
        n += 1
        approximation = 1 + x**2 / n
    
    return approximation

x = 1
approximation = approximate_exp(x)
print(f"e ≈ {approximation:.5f}")


