class Nguoi:
    def __init__(self,ten,tuoi):
        self.ten=ten
        self.tuoi=tuoi
    def info(self):
        print("ten la",self.ten,"Tuoi la",self.tuoi)
class Hs(Nguoi):
    def __init__(self,ten,tuoi,lop):
        Nguoi.__init__(self,ten,tuoi)
        self.lop=lop
    def tenlop(self):
        print("lop ",self.lop)

Hsa=Hs("Nguyen van Tho",20,"18CDT1")
Hsa.tenlop()
Hsa.info()