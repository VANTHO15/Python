# lib parser
import argparse
# lib logging
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s %(levelname)s] --> %(module)s: %(message)s'
)
# Liệt kê các file và thư mục 
import glob
import os

def Read_argument():
    # init parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="write args")
    # Options for tool
    parser.add_argument("-o", "--options", help="prepare generate compile execute report", nargs='+', default=None)
    parser.add_argument("-d", "--debug", help="1: enable debug 0: disable debug", nargs='+', default=None)
    return parser.parse_args()
class PathTest():
    TEST_NAME = ""
class RunTool():
    Steps = None
    Mytest= None
    def __init__(self, step, debug):
        if debug == 1:
            self.debug = 1
        else:
            self.debug = 0
        # set step 
        self.Steps = step
        # set Test
        self.Mytest = PathTest()
        print("Init ok ")
    def Start(self):
        x = os.path.join('F:\ThoNV_FrameWork\Z_FileC', "*.c")
        y = glob.glob(x)
        print(y)
        # if self.Mytest == "prepare":
        #     Prepare(test=self.test).run()
        # elif self.Mytest == "generate":
        #     Generate(test=self.test).run()
        # elif self.Mytest == "compile":
        #     Compile(test=self.test).run()
        # elif self.Mytest == "execute":
        #     Execute(test=self.test, debug=self.debug).run()
        # elif self.Mytest == "report":
        #     Report(test=self.test).run()


if __name__ == '__main__':
    Argument = Read_argument()
    # print(Argument.options, Argument.debug)
    logging.info("options = %s  debug = %s",Argument.options[0],Argument.debug[0])
    RunNew = RunTool(Argument.options[0],Argument.debug[0])
    RunNew.Start()
