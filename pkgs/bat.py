from utils     import github, paths
from ._install import PkgInstall
from ._core    import Pkg







class Bat(Pkg):


    def __init__(self) -> None:
        super().__init__()
        self.name        = "bat"
        self.project_url = "https://github.com/sharkdp/bat"
        self.repo        = "sharkdp/bat"
        self.bin_files   = ["bat",]

        self.unpacking_method = lambda : PkgInstall.unpack_copy_bin(self.archive_name, self.bin_files)


    @property
    def version(self) -> str:
        return self._version_github()


    @property
    def download_url(self):
        return self._download_url_github()


    @property
    def archive_name(self):
        return f"{self.name}-{self.version}-x86_64-unknown-linux-gnu.tar.gz"


