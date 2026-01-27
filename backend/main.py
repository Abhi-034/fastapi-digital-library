from fastapi import FastAPI

app = FastAPI(title="Digital Library API")

@app.get("/")
def root():
    return {"message": "Digital Library API is running"}