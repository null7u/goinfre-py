from utils     import github, paths
from ._install import PkgInstall
from ._core    import Pkg







class VirtualBox(Pkg):


    def __init__(self) -> None:
        super().__init__()
        self.name        = "virtualbox"
        self.project_url = "https://www.virtualbox.org/"
        self.bin_files   = ["bin/virtualbox",]


        self.download_url = "https://download.virtualbox.org/virtualbox/7.2.4/virtualbox-7.2_7.2.4-170995~Ubuntu~jammy_amd64.deb"
        self.version      = "v7.2.4"
        self.archive_name = self.download_url.split('/')[-1]
        self.unpacking_method = lambda : PkgInstall.debian(self.name, self.archive_name, self.bin_files)




