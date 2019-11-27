#!/usr/bin/env python3

import argparse
from lplib import choice

# 以后要用到
ALL_OPT = {
    "vegetable": None,
    "movement": None,
    "fruit": None,
    "drink": None,
    "game": None
}


def cli_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vegetable", action="store_true", dest="vegetable", help="蔬菜")
    parser.add_argument("-m", "--movement", action="store_true", dest="movement", help="健身动作")
    parser.add_argument("-f", "--fruit", action="store_true", dest="fruit", help="水果")
    parser.add_argument("-d", "--drink", action="store_true", dest="drink", help="水果")
    parser.add_argument("-g", "--game", action="store_true", dest="game", help="游戏")

    return parser


def cli():
    parser = cli_parser()
    args = parser.parse_args()
    lpl_choice = choice.Choice()

    for k, v in args.__dict__.items():
        if v:
            r = lpl_choice.choose(k + 's')
            print(r)


if "__main__" == __name__:
    cli()





