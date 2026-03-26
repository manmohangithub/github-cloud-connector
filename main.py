from fastapi import FastAPI
from routes.github import router
from auth.oauth import router as oauth_router

app = FastAPI(title="Advanced GitHub Connector")

app.include_router(router)
app.include_router(oauth_router, prefix="/auth")

@app.on_event("startup")
def startup_event():
    print("\n🚀 Server started successfully!")
    print("📄 Swagger Docs: http://127.0.0.1:8000/docs\n")