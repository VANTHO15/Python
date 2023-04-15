s="D/vantho15/chumuc.txt"
d=s.find("/")
c=s.rfind("/")
chuoi=s[d+1:c]
print(chuoi)

# Tách chuỗi

s="101180204;Nguyễn văn Thọ;06092000"
arr=s.split(";")

for i in arr:
    print(i,end=" ")

# Tách chuỗi mà nhiều hangf
print("")

s= """Vantho
đi câu cá
ngoài cầu đông"""
ar=s.splitlines()
for i in ar:
    print(i)

#   nối chuỗi join
st="101180204;Nguyễn văn Thọ;06092000"
a1=st.split(";")
sh=":"
tho=sh.join(a1)
print(tho)

