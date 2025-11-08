



global SUPPR_PACKAGES
# supported package.
SUPPR_PACKAGES = {
    "uv"    : "https://github.com/astral-sh/uv",
    "go"    : "https://github.com/golang/go",
    "nvim"  : "hthttps://github.com/neovim/neovim/",
    "bat"   : "hthttps://github.com/sharkdp/bat",
    "lsd"   : "hthttps://github.com/lsd-rs/lsd",
}



def packages_exists(packages:list[str]) -> tuple[bool, str]:
    suppr_packages = set(SUPPR_PACKAGES.keys())
    if not packages:
        return False, "No packages was passed after install;"
    for pkg in packages:
        if not pkg in suppr_packages:
            return False, f"{pkg} does not exists;"
    return True, ""



def list_available_packages()->None:
    # package name, package website or repo
    for pk_name, pk_url in SUPPR_PACKAGES.items():
        print(pk_name, pk_url, sep="\t")

