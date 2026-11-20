
from fastapi import FastAPI

app = FastAPI(
    title="TechHabba AI Service",
    description="Cybersecurity AI and ML Service",
    version="1.0.0"
)

@app.get("/")
def home():

    return {
        "application": "TechHabba",
        "status": "RUNNING",
        "message": "AI service is ready"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
