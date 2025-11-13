import requests as req
import json



def last_release(github_repo:str) -> str:
    url  = f"https://api.github.com/repos/{github_repo}/releases/latest"
    resp = req.get(url)
    version = json.loads(resp.text).get("tag_name", None)
    return version


