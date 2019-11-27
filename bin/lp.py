import optparse
from lplib import choice


def cli_parser():
    parser = optparse.OptionParser
    parser.add_option("-v", "--vegetable", help="蔬菜")
    parser.add_option("-m", "--movement", help="健身动作")
    return parser


if "__main__" == __name__:
    # parser = cli_parser()
    # parser.parse_args()
    action = "movements"
    r = choice.Choice().choose(action)
    print(r)