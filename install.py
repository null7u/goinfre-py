#!/bin/python3

import sys
import clt



if len(sys.argv) <= 1:
    print("You did not pass any commands")
    exit(0)
cmd_args = [_.lower() for _ in sys.argv[2:]]
cmd = sys.argv[1].lower()

def download_test(packgs:list[str]) -> None:
    packgs = (clt.SUPPR_PACKAGES[p] for p in packgs)
    for p in packgs:
        p.download()


match cmd:
    case "list":
        clt.list_available_packages()
    case "install":
        all_pkgs_exist, err =  clt.packages_exists(cmd_args)
        if not all_pkgs_exist:
            print(err)
            exit(1)
        download_test(cmd_args)
        #download_packages(cmd_args)
    case _:
        print("command does not exists;")
        exit(1)

