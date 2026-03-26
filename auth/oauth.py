from fastapi import APIRouter
import requests
from config import CLIENT_ID, CLIENT_SECRET

router = APIRouter()

@router.get("/login")
def login():
    return {
        "url": f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}"
    }

@router.get("/callback")
def callback(code: str):
    url = "https://github.com/login/oauth/access_token"

    res = requests.post(url, data={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code
    }, headers={"Accept": "application/json"})

    return res.json()
