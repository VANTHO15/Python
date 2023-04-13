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


def Read_argument():
    # init parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="write args")
    # Options for tool
    parser.add_argument("-o", "--options", help="prepare generate compile execute report", nargs='+', default=None)
    parser.add_argument("-d", "--debug", help="enable debug", nargs='+', default=None)
    return parser.parse_args()
if __name__ == '__main__':
    Argument = Read_argument()
    # print(Argument.options, Argument.debug)
    logging.info("options = %s  debug = %s",Argument.options[0],Argument.debug[0])