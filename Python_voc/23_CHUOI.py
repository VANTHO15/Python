name= "Nguyen van tho"
haha=" nguyen van    "
tho="#######vantho####"
print(name.upper()) # in hoa
print(name.lower()) # in thường
print(haha.strip()) # xóa khaongr trắng dư thừa
print(tho.strip("#"))
#############################################
print(name.startswith("N"))   # chuỗi name có bắt đầu bằng chũ "N" hay không
print(name.endswith("o"))    # chuỗi name có kết thúc bằng chũ "N" hay không
####################################
print(name.find("v"))  # vị trí đầu tiên của v trong name
print(name.rfind("v"))  # vị trí cuoi của v trong name
############
tho="vanthovanthojoo0ô0000ppoooooo0sjjadjavanthoooooooo00000o"
print(tho.count("vantho"))  # số lần xuất hiện của vantho
print(tho.count("o",4,9))  # đếm từ vị trí 4 đến 9
##########################
x="hello world!"
print(x[2:])  # llo world
print(x[:2])  # he
print(x[:-2])  # hello worl
print(x[-2:])   # d!
print(x[2:-2])  # llo worl
print(x[6:11])


