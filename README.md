# GitHub Cloud Connector (Advanced)

## Setup

1. Extract the project
2. Update .env file with your GitHub credentials
3. Install dependencies:
   pip install -r requirements.txt
4. Run:
   uvicorn main:app --reload

## API Docs
http://127.0.0.1:8000/docs

## Features
- PAT Authentication
- OAuth Support
- Fetch Repos
- List Issues
- Create Issue
- Fetch Commits
- Create Pull Requests
- Pagination
- Caching
- Logging
- Docker Support
