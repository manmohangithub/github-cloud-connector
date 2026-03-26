# GitHub Cloud Connector

## Overview
This project is a backend service that integrates with GitHub APIs. It authenticates using a Personal Access Token (PAT) and provides REST endpoints to perform operations like fetching repositories, listing issues, creating issues, fetching commits, and creating pull requests.

## Tech Stack
- Python
- FastAPI
- GitHub REST API

## Setup Instructions
1. Clone the repository
2. Navigate to the project folder
3. Create a `.env` file in the root directory and add:
   GITHUB_TOKEN=your_token_here

4. Install dependencies:
   pip install -r requirements.txt

5. Run the application:
   python -m uvicorn main:app --reload

## API Endpoints
- GET /repos/{username} → Fetch repositories of a user
- GET /issues/{owner}/{repo} → List issues of a repository
- POST /issue → Create an issue
- GET /commits/{owner}/{repo} → Fetch commits of a repository
- POST /pull-request → Create a pull request

## API Documentation
After running the server, open:
http://127.0.0.1:8000/docs

## Notes
- Authentication is handled using a GitHub Personal Access Token (PAT)
- The `.env` file is not included in the repository for security reasons
