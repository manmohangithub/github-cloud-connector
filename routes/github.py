from fastapi import APIRouter
from services.github_service import *
from models.schemas import IssueCreate, PullRequestCreate

router = APIRouter()

@router.get("/repos/{username}")
def repos(username: str, page: int = 1):
    return get_repos(username, page)

@router.get("/issues/{owner}/{repo}")
def issues(owner: str, repo: str, page: int = 1):
    return list_issues(owner, repo, page)

@router.post("/issue")
def issue(data: IssueCreate):
    return create_issue(data)

@router.get("/commits/{owner}/{repo}")
def commits(owner: str, repo: str):
    return get_commits(owner, repo)

@router.post("/pull-request")
def pr(data: PullRequestCreate):
    return create_pull_request(data)
