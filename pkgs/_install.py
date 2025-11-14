import requests as req
import tarfile
import shutil
from utils import paths



class PkgInstall:
    def download_archive(output:str, url:str, headers:dict={}, method:str="GET") -> None:
        assert method in {"GET", "POST"}
        with open(output, "wb") as file:
            with req.request(method, url, headers=headers, stream=True) as stream:
                stream.raise_for_status()
                for chunk in stream.iter_content(chunk_size=2048):
                    file.write(chunk)


    def unpack_copy_bin(archive_name:str, bin_files:list[str]) -> None:
        PkgInstall.unpack(archive_name)
        PkgInstall.copy_bin(archive_name, bin_files)


    def unpack(archive_name:str) -> None:
        tar = tarfile.open(paths.tmp + f"/{archive_name}", "r:gz")
        tar.extractall(path=paths.tmp)
        tar.close()


    def copy_bin(archive_name:str, bin_files:tuple[str]) -> None:
        archive_name = archive_name.removesuffix(".tar.gz")
        path = f"{paths.tmp}/{archive_name}"
        for bin_f in bin_files:
            shutil.copy2(f"{path}/{bin_f}", paths.bin)

