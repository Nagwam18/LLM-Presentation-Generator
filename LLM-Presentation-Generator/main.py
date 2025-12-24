# main.py
import uvicorn
from app import fastapi_app

if __name__ == "__main__":
    print("🚀 Starting LLM Presentation Generator...")
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)
