from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Tn Another World bieng Highhhhhzz"}

