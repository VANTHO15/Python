import argparse
def Read_argument():
    # parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="write args")
    # Options for tool
    parser.add_argument("-o", "--options", help="prepare generate compile execute report", nargs='+', default=None)
    parser.add_argument("-d", "--debug", help="enable debug", nargs='+', default=None)
    return parser.parse_args()
if __name__ == '__main__':
    Argument = Read_argument()
    print(Argument.options, Argument.debug )
    if Argument.options[0] == "prepare":
        print("prepare")
    elif Argument.debug[0] == "1":
        print("debug") 