from ._install import PkgInstall
from utils    import github, paths

class Pkg:
    name       :str
    project_url:str


    def __init__(self) -> None:
        self._version = None


    def download(self) -> None:
        print("installing...", self.name, self.version)
        print("URL:", self.download_url)
        PkgInstall.download_archive(
            paths.tmp + f"/{self.archive_name}",
            self.download_url, 
        )
        #self.unpacking_method()

    def _version_github(self) -> str:
        if not self._version:
            self._version = github.last_release_tag(self.repo)
        return self._version


    def _download_url_github(self) -> str:
        return f"https://github.com/{self.repo}/releases/download/{self.version}/{self.archive_name}"



