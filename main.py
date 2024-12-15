from functools import lru_cache
from fastapi import FastAPI, UploadFile # type: ignore
from dotenv import load_dotenv # type: ignore
from conversions import getEnvironmentVariable
from os import makedirs, path
import uvicorn # type: ignore

load_dotenv()

app = FastAPI()

PORT = getEnvironmentVariable("PORT", int, 8000)
FILEPATH = getEnvironmentVariable("FILEPATH", str, "uploads/")

# make sure path exists
if not path.exists(FILEPATH):
    makedirs(FILEPATH)
    print(f"Directory '{FILEPATH}' created.")
else:
    print(f"Directory '{FILEPATH}' already exists.")
    

@app.post("/port")
async def port():
    return {"PORT": PORT}

@app.post("/upload/")
async def uploadFile(file: UploadFile):
    try:
        print(FILEPATH)
        filepath = path.join(FILEPATH, file.filename) 
        print(filepath)
        with open(filepath, "wb") as f:
            while chunk := file.file.read(1024*1024):
                f.write(chunk)
        return {"message": "File uploaded successfully", "filename": file.filename}
    
    except Exception as e:
        print(e)
        return {"message": "File could not be  uploaded"}



if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, reload=True) #getting values from environment variables
