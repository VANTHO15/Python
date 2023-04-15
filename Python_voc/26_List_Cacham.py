lst=[1,2,3,4,5,6,7,8]
# chèn
lst.insert(2,100)  # chèn 100 vào vị trí thứ 2
print(lst)
# chèn vào cuối
lst.append(1999)
print(lst)
# xóa
lst.remove(6)  # xóa số 6
print(lst)
# đảo danh sách
lst.reverse()
print(lst)
# hàm sắp xếp tăng dần
lst.sort()
print(lst)
# hàm sắp xếp mà nó tách ra 1 hàm mới
haha=sorted(lst)
print(haha)
haha.reverse()
print(haha)
# cắt LIST
arr=[1,2,3,4,5,6,7,8,9]
a=arr[2:7:1]
print(a)

