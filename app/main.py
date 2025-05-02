from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def check_status():
    return {"message": "Ninja is operational 🥷"}
