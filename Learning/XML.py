import xml.etree.ElementTree as ET

# <BeginThoNV test="ThoNV">
#     <Truong NameTruong="BK Da Nang" DiaChi="54 NLB">
#         <Lop Lop1="1">18CDT1</Lop>
#         <Lop Lop1="2">18CDT2</Lop>
#         <ChucDanh>Lop Truong</ChucDanh>
#     </Truong>
#     <ThongTin Tien="86 ty">
#         <Ten>ThoNV</Ten>
#         <Tuoi>23</Tuoi>
#     </ThongTin>
# </BeginThoNV>

class ThoNV:
    def __init__(self):
        pass
    def run(self):
        tree = ET.parse('Test.xml')
        root = tree.getroot()
        #get
        print(root.tag)
        print(root.attrib)
        print(root[0][1].text)
        for child in root:
            print(child.tag, child.attrib)

        # find
        # Top-level elements
        print(root.findall(".")) # select current node
        print(root.findall("ThongTin")) # select tag
        print(root.findall("./Truong/Lop"))
        print(root.findall("./*")) # select all child element
        print(root.findall(".//Truong")) # chọn tất cả các node Truong trong toàn bộ cây.
        print(root.findall("./Truong/Lop/[@Lop1='2']")[0].text) # Chọn các node có Lop = 2 , dấu = hoặc !=
        print(root.findall("./Truong/Lop/[.='18CDT1']"))  # chọn các node có text = "18CDT1", dấu = hoặc !=
        print(root.findall("./Truong/[Lop='18CDT1']"))  # Chọn node Truong child trong nó có tag Lop có text = "18CDT1"
        print(root.findall("./Truong/[1]"))   # Chọn thằng Truong thứ 2 trong list tất cả Truong tìm được, 1 là vị trí đâì tiên, last() là vị trí cuối cùng

        #Modify
        for ThongTin in root.findall('ThongTin'):
            ThongTin.set('Tien','136 ty')
        root[0][1].text = "Lop Truong"
        tree.write('Test.xml')  # Phải có để update tree

        #remove
        for ThongTin in root.findall('ThongTin'):
            for Tuoi in ThongTin.findall("Tuoi"):
                ThongTin.remove(Tuoi)
        tree.write('Test.xml')  # Phải có để update tree

if __name__ == '__main__':
    ThoNV().run()

