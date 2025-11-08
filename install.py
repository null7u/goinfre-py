#!/bin/python3

import sys
import utils



if len(sys.argv) <= 1:
    print("You did not pass any commands")
    exit(0)
cmd_args = [_.lower() for _ in sys.argv[2:]]
cmd = sys.argv[1].lower()


match cmd:
    case "list":
        utils.list_available_packages()
    case "install":
        all_pkgs_exist, err =  utils.packages_exists(cmd_args)
        if not all_pkgs_exist:
            print(err)
            exit(1)
        #download_packages(cmd_args)
    case _:
        print("command does not exists;")
        exit(1)

