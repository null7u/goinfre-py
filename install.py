#!/bin/python3

import sys

global SUPPR_PACKAGES
SUPPR_PACKAGES= {
    "uv"    : "https://github.com/astral-sh/uv",
    "go"    : "https://github.com/golang/go",
    "nvim"  : "hthttps://github.com/neovim/neovim/",
    "bat"   : "hthttps://github.com/sharkdp/bat",
    "lsd"   : "hthttps://github.com/lsd-rs/lsd",
}

if len(sys.argv) <= 1:
    print("You did not pass any commands")
    exit(0)
cmd_args = [_.lower() for _ in sys.argv[2:]]
cmd = sys.argv[1].lower()



def list_packages()->None:
    # package name, package website or repo
    for pk_name, pk_url in SUPPR_PACKAGES.items():
        print(pk_name, pk_url, sep="\t")


match cmd:
    case "list":
        list_packages()
    case "install":
        print("in the future")
    case _:
        print("command does not exists.")
        exit(1)

