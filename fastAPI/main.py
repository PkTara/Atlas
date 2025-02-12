from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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


def log(message):
    with open("log.txt", "a") as file:
        file.write(str(datetime.datetime.now()) +   ": " + message + "\n")



with open("wallList.json", 'r') as file:
    wallList = json.load(file)
    no_walls = wallList["no_walls"]

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

    wallInfo = data.data

    log(f"Received: {wallInfo.title}")

    log("Attempting to write!")

    # wallList["walls"].append(f'''{{
    #                 "id" : {no_walls},
    #                 "title" : {wallInfo.title},
    #                 "grade" : {wallInfo.grade}
    #                 }}''')
    # no_walls += 1
    wallList["no_walls"] += 1
    wallList["walls"].append({
        "id" : no_walls,
        "title" : wallInfo.title,
        "grade" : wallInfo.grade
    })
    with open("wallList.json", 'w') as file:
        file.write(json.dumps(wallList))
    
    # Example: Processing and returning a response
    return {"message" : "Data Recieved!"}
