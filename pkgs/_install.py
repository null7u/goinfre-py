import requests as req
import tarfile
import shutil
import subprocess
import lzma
from typing import Callable 
from os         import symlink, path
from utils      import paths



class PkgInstall:
    def download_archive(output:str, url:str, headers:dict={}, method:str="GET") -> None:
        assert method in {"GET", "POST"}
        with open(output, "wb") as file:
            with req.request(method, url, headers=headers, stream=True) as stream:
                stream.raise_for_status()
                for chunk in stream.iter_content(chunk_size=2048):
                    file.write(chunk)


    def _unpack_tar_gz(archive_path:str) -> None:
        tar = tarfile.open(archive_path, "r:gz")
        tar.extractall(path=paths.tmp)
        tar.close()


    def _unpack_tar_xz(archive_path:str) -> None:
        tar = tarfile.open(archive_path, "r:xz")
        tar.extractall(path=paths.tmp)
        tar.close()


    def unpack(archive_name:str) -> None:
        ar = paths.tmp + f"/{archive_name}"
        if archive_name.endswith(".tar.gz"):
            PkgInstall._unpack_tar_gz(ar)
        elif archive_name.endswith(".xz"):
            PkgInstall._unpack_tar_xz(ar)


    def unpack_copy_bin(archive_name:str, bin_files:list[str]) -> None:
        PkgInstall.unpack(archive_name)
        PkgInstall.copy_bin(archive_name, bin_files)


    def copy_bin(archive_name:str, bin_files:tuple[str]) -> None:
        archive_name = archive_name.removesuffix(".tar.gz")
        path = f"{paths.tmp}/{archive_name}"
        for bin_f in bin_files:
            shutil.copy2(f"{path}/{bin_f}", paths.bin)

    def link(name:str, bin_files:tuple[str]) -> None:
        for bf in bin_files:
            src    = f"{paths.bin_files}/{name}/{bf}"
            output = f"{paths.bin}/{bf.split('/')[-1]}"
            symlink(src, output)


    # debian packages:
    def debian(name:str, archive_name:str, to_cpy:str, bin_list_gen:Callable) -> None:
        path = f"{paths.tmp}/{archive_name}"
        PkgInstall.unpack_debian(path)
        PkgInstall.unpack("data.tar.xz")
        shutil.move(f"{paths.tmp}/{to_cpy}", f"{paths.bin_files}/{name}")
        PkgInstall.link(name, bin_list_gen())


    def unpack_debian(archive_path:str) -> None:
        subprocess.run(['ar', 'x', archive_path], cwd=paths.tmp)


