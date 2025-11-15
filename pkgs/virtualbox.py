from utils     import github, paths
from ._install import PkgInstall
from ._core    import Pkg
from os        import listdir






class VirtualBox(Pkg):


    def __init__(self) -> None:
        super().__init__()
        self.name        = "virtualbox"
        self.project_url = "https://www.virtualbox.org/"


        self.download_url = "https://download.virtualbox.org/virtualbox/7.2.4/virtualbox-7.2_7.2.4-170995~Ubuntu~jammy_amd64.deb"
        self.version      = "v7.2.4"
        self.archive_name = self.download_url.split('/')[-1]
        self.unpacking_method = lambda : PkgInstall.debian(self.name, self.archive_name, 'usr', lambda : self.bin_list())


    def bin_list(self) -> list[str]:
        bin_files = listdir(f"{paths.bin_files}/{self.name}/bin")
        return (f"bin/{_}" for _ in bin_files)




