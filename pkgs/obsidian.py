from utils     import github, paths
from ._install import PkgInstall
from ._core    import Pkg







class Obsidian(Pkg):


    def __init__(self) -> None:
        super().__init__()
        self.name        = "obsidian"
        self.project_url = "https://obsidian.md/"


        self.version      = "v1.10.3"
        self.download_url = f"https://github.com/obsidianmd/obsidian-releases/releases/download/{self.version}/obsidian_{self.version[1:]}_amd64.deb"
        self.archive_name = self.download_url.split('/')[-1]
        self.unpacking_method = lambda : PkgInstall.debian(
            self.name,
            self.archive_name,
            'opt',
            lambda : [f"Obsidian/{self.name}", ]
        )




