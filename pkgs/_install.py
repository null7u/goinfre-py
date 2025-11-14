import requests as req





class PkgInstall:
    def download_archive(output:str, url:str, headers:dict={}, method:str="GET") -> None:
        assert method in {"GET", "POST"}
        with open(output, "wb") as file:
            with req.request(method, url, headers=headers, stream=True) as stream:
                stream.raise_for_status()
                for chunk in stream.iter_content(chunk_size=2048):
                    file.write(chunk)
