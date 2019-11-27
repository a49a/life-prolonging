import optparse

def cli_parser():
    parser = optparse.OptionParser
    parser.add_option("-v", "--vegetable", help="蔬菜")
    parser.add_option("-m", "--movement", help="健身动作")
    return parser