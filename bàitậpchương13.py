#bài 1
def mo_tep_tin():
    name_file = input('nhập tên tệp tin :')
    try:
        with open(name_file,'r',encoding = 'utf-8') as f:
            print('nội dùng tệp tin là : \n',f.read())
    except FileNotFoundError:
        print('tệp tin k tồn tại ')
mo_tep_tin()
#bài 2
def thong_kefile():
    name_file =  input('nhập tên file ở đây ')
    try:
        with open(name_file,'r',encoding= 'utf-8') as f:
            read=  f.read()
            print('nội dung của file là : \n',read,'\n')
            so_dong = read.count('\n')
            print('số line của text là : ',so_dong)
            so_tu = len(read.split())
            print('số work = ',so_tu)
            so_ky_tu = len(read)
            print('số ký tự là : ',so_ky_tu)
    except FileNotFoundError:
        print('tệp tin k tồn tại ')

thong_kefile()
#bài 3
def mo_doc_ghi_file():
    name_file   =  input('nhập tên file :')
    with open(name_file,'w',encoding='utf-8') as f :
        f.write('Rain rain , go away; Come again another day ...')
    a  = open(name_file,'r',encoding='utf-8')
    print('nội dung của file là : ',a.read())

mo_doc_ghi_file()
#bài 4
def them_nd_append():
    name_file = input('Nhập tên tệp tin: ')

    while True:
        print('Chọn hành động:  1. Nhập thêm nội dung  2. In nội dung :')
        i = input()
        if i == '1':
            noi_dung_tep = input('Nhập nội dung: ')
            try:
                with open(name_file, 'a', encoding='utf-8') as f:
                    f.write('\n' + noi_dung_tep)
                print('Nội dung đã được thêm vào tệp tin.')
            except FileNotFoundError:
                print('Không tìm thấy tệp tin.')
        elif i == '2':
            try:
                with open(name_file, 'r', encoding='utf-8') as f:
                    print(f.read())
            except FileNotFoundError:
                print('Không tìm thấy tệp tin.')
            break
        
        else:
            print('Lựa chọn không hợp lệ. Vui lòng nhập lại.')

them_nd_append()
#bài 5
import csv
def read_csv():
    name_file =  input('nhập tên file csv vào đây :') # điển part1.csv
    f = open(name_file)
    list=[]
    for i in csv.reader(f):
        list.append(i)
    f.close()
    return list
print(read_csv())   
#bài 6
def ghi_csv():
   import csv
   name_file = input('Nhập tên file CSV: ')
   line_news = [] 
   while True:
        try:
            with open(name_file, 'a', newline='', encoding='utf-8') as file:
                dong = csv.writer(file)
                if line_news:
                    dong.writerow(line_news)
                    print('Dữ liệu đã được thêm vào tệp tin CSV.')
                    line_news = [] 
                print('Chọn hành động:  1. Nhập thêm nội dung  2. Kết thúc:')
                lua_chon = input()
                if lua_chon == '1':
                    line_new = input('Nhập dữ liệu muốn thêm vào CSV (các giá trị cách nhau bởi dấu phẩy): ')
                    line_news = line_new.split(',')
                elif lua_chon == '2':
                    print('Chương trình đã kết thúc.')
                    f = open(name_file)
                    a = f.read()
                    print('nội dung file là : ',a)
                    break
        except FileNotFoundError:
            print("File không tồn tại.")
ghi_csv()