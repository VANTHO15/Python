class Car:
    Ten="Xăng"
    TocDo="200"
    def VanToc(self,vantoc):
        print("xe chay van tốc: ",self.TocDo,vantoc)
xe=Car()
print(xe.Ten)
xe.VanToc(300)