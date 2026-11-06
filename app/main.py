from fastapi import FastAPI

app = FastAPI(title="Sentinel")

@app.get("/health/live")
def live():
    return {"status" : "ok"}

