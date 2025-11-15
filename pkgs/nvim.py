from utils     import github, paths
from ._install import PkgInstall
from ._core    import Pkg







class Nvim(Pkg):


    def __init__(self) -> None:
        super().__init__()
        self.name        = "nvim"
        self.project_url = "https://github.com/neovim/neovim"
        self.repo        = "neovim/neovim"
        self.bin_files   = ["bin/nvim",]

        self.unpacking_method = lambda : PkgInstall.unpack_move_link(self.archive_name, self.name, lambda :['bin/nvim', ])


    @property
    def version(self) -> str:
        return self._version_github()


    @property
    def download_url(self):
        return self._download_url_github()


    @property
    def archive_name(self):
        return f"{self.name}-linux-x86_64.tar.gz"


