import requests as req
import json



def last_release_tag(github_repo:str) -> str:
    url  = f"https://api.github.com/repos/{github_repo}/releases/latest"
    resp = req.get(url)
    if resp.status_code == 403:
        print(json.loads(resp.text).get("message"))
        exit(1)
    version = json.loads(resp.text).get("tag_name", None)
    return version


