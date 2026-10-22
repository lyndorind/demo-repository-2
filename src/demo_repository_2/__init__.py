import uvicorn
from .main import app

__version__ = "0.0.1"

def main():
    uvicorn.run("demo_repository_2:app", host="0.0.0.0", port=8000, workers=1)
