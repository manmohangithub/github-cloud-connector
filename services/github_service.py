import requests
from config import GITHUB_TOKEN, BASE_URL
from logger import logger
from cache import get_cache, set_cache

print("TOKEN:", GITHUB_TOKEN)

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_repos(username, page=1):
    cache_key = f"repos_{username}_{page}"
    cached = get_cache(cache_key)
    if cached:
        return cached

    url = f"{BASE_URL}/users/{username}/repos?page={page}"
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        logger.error(res.text)
        return {"error": res.json()}

    data = res.json()
    set_cache(cache_key, data)
    return data


def list_issues(owner, repo, page=1):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues?page={page}"
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return {"error": res.json()}
    return res.json()


def create_issue(data):
    url = f"{BASE_URL}/repos/{data.owner}/{data.repo}/issues"
    payload = {"title": data.title, "body": data.body}

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 201:
        return {"error": res.json()}
    return res.json()


def get_commits(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return {"error": res.json()}
    return res.json()


def create_pull_request(data):
    url = f"{BASE_URL}/repos/{data.owner}/{data.repo}/pulls"

    payload = {
        "title": data.title,
        "head": data.head,
        "base": data.base,
        "body": data.body
    }

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 201:
        return {"error": res.json()}
    return res.json()
