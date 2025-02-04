from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def getHome():
    return "Hello"