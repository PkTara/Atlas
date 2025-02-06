
import os
from rectangleHolds import process

unprocessed_path =  "./unprocessed_images/"
processed_path = "./processed_images/"

id = 1
for filename in os.listdir(unprocessed_path):
    id += 1

for filename in os.listdir(unprocessed_path):
    print(filename)
    file_path = os.path.join(unprocessed_path, filename)
    if os.path.isfile(file_path):
        print(f"Processing file: {filename}")
        process(unprocessed_path + filename, processed_path  + str(id) + ".jpg")
    id +=1

    
