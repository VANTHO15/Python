class ThoNV:
    def __init__(self):
        pass
    def run(self):

        with open("ReplaceXML.xml","r") as file:
            XML_data = file.read()
        XML_data = XML_data.replace("NAME_THO","Nguyen Van Tho")
        XML_data = XML_data.replace("TUOI_THO","23")

        with open("New_XML_File.xml", "w+") as file:
            file.write(XML_data) 
if __name__ == '__main__':
    ThoNV().run()

