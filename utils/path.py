from os import path, makedirs

goinfre   = path.expanduser("~") + "/goinfre"
tool_path = goinfre + "/goinfre-py"
bin       = tool_path + "/bin"
tmp       = tool_path + "/tmp"
bin_files = tool_path + "/libs"


if not path.exists(goinfre):
    print("/goinfre Doesn't exist")
    exit(1)

for pth in [tool_path, bin, tmp, bin_files]:
    makedirs(pth, exist_ok=True)
