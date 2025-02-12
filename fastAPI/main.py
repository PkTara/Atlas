from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
import sys
from pydantic import BaseModel
import json
import datetime

from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger("uvicorn.error")
# logger.setLevel(logging.DEBUG)

def log(message):
    with open("log.txt", "a") as file:
        file.write(str(datetime.datetime.now()) +   ": " + message + "\n")



with open("wallList.json", 'r') as file:
    wallList = json.load(file)

@app.get("/")
async def root():

    

    return {"message": "Hello World",
             "wallList" : wallList["walls"]

             
             }

images = Path("./wallPhotos/")

@app.get("/getImage/1")
async def get_image():
    imagePath = images + Path("climbing3.jpg")
    if not imagePath.is_file():
        return ({"Path not found!"})
    return FileResponse(imagePath)



@app.get("/getImage/")
async def get_image(id: str=1):
    imagePath = Path("./processing/processed_images/" + id + ".jpg")
    if not imagePath.is_file():
        return ({"Path not found!"})
    return FileResponse(imagePath)



# =========== POSTING =============

class wallInfoData(BaseModel):
    title: str
    grade: str

class formData(BaseModel):
    user_id: int
    username: str
    data: wallInfoData
    # where data will have .title, .grade
    # .. dunno how to mandate it having a .title/.grade

@app.post("/upload/")
async def upload(data: formData):
    # Do something with the received data
    log("upload/")

    # try:
    #     wallInfo = data.data
    # except json.JSONDecodeError as e:
    #     raise HTTPException(status_code=422, detail="invalid JSON")
    #     # return {"message" : "Invalid JSON syntax:" + e}

    wallInfo = data.data

    log(f"Received: {wallInfo.title}")

    wallList.append({
                    "id" : "5",
                    "title" : wallInfo.title,
                    "grade" : wallInfo.grade
                 },)
    
    # Example: Processing and returning a response
    return {"message" : "Data Recieved!"}
