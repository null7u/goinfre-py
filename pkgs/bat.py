from utils import github, paths
import requests as req



class Pkg:
    name       :str
    project_url:str


    def __init__(self) -> None:
        self._version = None


    def download(self) -> None:
        print("installing...", self.name, self.version)
        print("URL:", self.download_url)
        self.download_archive()


    def _version_github(self) -> str:
        if not self._version:
            self._version = github.last_release_tag(self.repo)
        return self._version


    def _download_url_github(self) -> str:
        return f"https://github.com/{self.repo}/releases/download/{self.version}/{self.archive_name}"


    def download_archive(self, headers:dict={}, method="GET") -> None:
        assert method in {"GET", "POST"}
        with open(paths.tmp + f"/{self.archive_name}", "wb") as file:
            with req.request(method, self.download_url, headers=headers, stream=True) as stream:
                stream.raise_for_status()
                for chunk in stream.iter_content(chunk_size=2048):
                    file.write(chunk)




class Bat(Pkg):


    def __init__(self) -> None:
        super().__init__()
        self.name        = "bat"
        self.project_url = "https://github.com/sharkdp/bat"
        self.repo        = "sharkdp/bat"


    @property
    def version(self) -> str:
        return self._version_github()


    @property
    def download_url(self):
        return self._download_url_github()


    @property
    def archive_name(self):
        return f"{self.name}-{self.version}-x86_64-unknown-linux-gnu.tar.gz"


