from fastapi import FastAPI
from app.routes import recon

app = FastAPI()

app.include_router(recon.router)

@app.get("/status")
def check_status():
    return {"message": "Ninja is operational 🥷"}
