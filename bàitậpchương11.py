#bài 1
a = [1,2,3]
b = [1,[2,3]]
c = []
d = [1,2,3][1:]
print("chiều dài của danh sách list a là:",len(a))
print("chiều dài của danh sách list b là:",len(b))
print("chiều dài của danh sách list c là:",len(c))
print("chiều dài của danh sách list d là:",len(d))

#bài 2
doia = ['steven','nenna','lẽx','alexander','bruce']
doib = ['david','jack','bill','tom','rike','daniel']
doic = ['alexander','adam','payan','kevin','sign','nike']
print("thằng đội trưởng tệ nhất là:",doic[1])

#bài 3
danh_sach_dong_vat = ['kiến','gấu','chó','voi','cá','dê','hama']
print("danh sách các loài đông vật:",danh_sach_dong_vat)
print("số lượng các loại động vật:",len(danh_sach_dong_vat))
tim_kiem = input("tôi muốn tìm:")
find = tim_kiem in danh_sach_dong_vat
if find == True:
    print(tim_kiem,"có trong danh sách động vật")
if find == False:
    print(tim_kiem,"không có trong danh sách động vật")

#bài 4
list = []
while True:
    gia_tri = int(input("nhập giá trị:"))
    list.append(gia_tri)
    nhap_tiep = int(input("tiếp tục nhập giá trị(nhập 0 để dừng,nhập 1 để tiếp tục):"))
    if nhap_tiep == 1:
     print(gia_tri)
    if nhap_tiep == 0:
        break
print(list)
print("tổng của list là:",sum(list))
x = int(input("giá trị x cần tìm là:"))
print(x,"xuất hiện",list.count(x),"lần trong list")
max_list = max(list)
if x > max_list:
   print(x,"lớn hơn tất cả các giá trị của list")
else:
   print(x,"không lớn hơn tất cả các giá trị của list")
for num in list :
   if num > x:
      print("các số lớn hơn",x,"là:",num)

#bài 5
list5 = []
while True:
   gia_tri = int(input("nhập giá trị:"))
   list5.append(gia_tri)
   nhap_tiep = int(input("tiếp tục nhập giá trị?(nhập 0 để dừng lại, nhập 1 để tiếp tục):"))
   if nhap_tiep == 1:
      print(gia_tri)
   if nhap_tiep == 0:
      break
print("list5=",list5)
x = []
for num in list5:
    la_so_nguyen_to = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        x.append(num)
print("các số nguyên tố trong list5 là:",x)
so_trung_binh_cong = (sum(list5)/len(list5))
print("số trung bình cộng của list5 là:",so_trung_binh_cong)
print("giá trị lớn nhất của list5 là:",max(list5))
print("giá trị bé nhất của list5 là:",min(list5))
list5.sort()
print("sắp xếp theo thứ tự từ bé đến lớn:",list5)

#bài 6
chieu_cao = [74,74,72,73,69,69,71,76,71]
chieu_cao_met = []
for i in chieu_cao:
    inch_sang_met = round(i*0.0254,2)
    chieu_cao_met.append(inch_sang_met)
print("3 chiều cao đầu tiên là:",chieu_cao_met[:3])
print("3 chiều cao cuối cùng là:",chieu_cao_met[-3:])
chieu_cao_tb = sum(chieu_cao_met) / len(chieu_cao_met)
chieu_cao_lon_nhat = max(chieu_cao_met)
chieu_cao_be_nhat = min(chieu_cao_met)
print("chiều cao trung bình của danh sách là:",chieu_cao_tb)
print("chiều cao lớn nhất của danh sách là:",chieu_cao_lon_nhat)
print("chiều cao bé nhất của danh sách là:",chieu_cao_be_nhat)
print("chiều cao tăng dần là:",sorted(chieu_cao_met))
print("chiều cao giảm dần là:",sorted(chieu_cao_met,reverse = True))

#bài 7

L = [2, 34, 3, 2, 2, 4]
def elementwise_greater_than(L, thresh):
    result = []
    for i in L:
        if i > thresh:
            result.append(True)
        else:
            result.append(False)
    return result

thresh = 2
print(elementwise_greater_than(L, thresh))

#bài 8
nums = []
while True :
    nhap_gia_tri = eval(input("nhập giá trị vào danh sách:"))
    if nhap_gia_tri == 0:
        break
    nums.append(nhap_gia_tri)
print(nums)
def has_lucky_num(nums):
    for i in nums:
        if i % 7 == 0:
            return True
print(has_lucky_num(nums))

#bài 9
arrivals = ['Adela', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
party_late = 0

for guest in arrivals:
    if arrivals.index(guest) >= len(arrivals) / 2:
        party_late += 1

if party_late >= 3:
    print(True)
else:
    print(False)

print(party_late(arrivals, name='gilbert'))
