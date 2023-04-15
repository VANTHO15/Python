from baitapxulifileSanpham import *

masp=input("nhap mã sản phẩm: ")
tensp=input("nhap tên sp: ")
dongia=input("nhap đơ giá: ")
line=masp+";"+tensp+";"+dongia

luufile("database.txt",line)