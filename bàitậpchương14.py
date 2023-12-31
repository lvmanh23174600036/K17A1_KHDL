#bài 1
while True:
 try:
  a=int(input("giá trị cạnh thứ nhất:"))
  b=int(input("giá trị cạnh thứ hai:"))
  c=int(input("giá trị cạnh thứ ba:"))
  if a<=0 or b<=0 or c<=0:
     raise TypeError ("Vui lòng nhập giá trị lớn hơn 0!!!")
  if a+b<=c or a+c<=b or b+c<=a:
     raise TypeError ("Vui lòng nhập lại giá trị!!!")        
 except ValueError as f:
    print("Vui lòng nhập giá trị là số nguyên dương!!!")
 except TypeError as q:
     print(q)
 else:
     q=int(a+b+c)/2
     import math
     s=math.sqrt(q*(q-a)*(q-b)*(q-c))
     print("diện tích tam giác:",s)
     break
#bài 2
b=[]
while True:
    try:
      a=int(input("nhập số"))
      b.append(a)  
      if a<=0:
            raise TypeError ("Lỗi số âm!!!")
      if len(b)>=4 and b[-1]==b[-2] and b[-1]==b[-3] and b[-1]==b[-4]:
            raise TypeError ("Lỗi nhập lặp số!!!")
      if len(b)>=5 and b[-1]%2==0 and b[-2]%2==0 and b[-3]%2==0 and b[-4]%2==0 and b[-5]%2==0:
            raise TypeError ("Lỗi nhập chẵn!!!")
    except ValueError :
        print("Lỗi nhập số!!!")
        b.pop(-1)
    except TypeError as f:
        print(f)
        b.pop(-1)