from utils import github


class Pkg:
    name       :str
    project_url:str


    def __init__(self) -> None:
        self._version = None



    def download(self) -> None:
        print("installing...", self.name, self.version)



    def _version_github(self) -> str:
        if not self._version:
            self._version = github.last_release(self.repo)
        return self._version



class Bat(Pkg):


    def __init__(self) -> None:
        super().__init__()
        self.name        = "bat"
        self.project_url = "https://github.com/sharkdp/bat"
        self.repo        = "sharkdp/bat"



    @property
    def version(self) -> str:
        return self._version_github()
