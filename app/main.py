from fastapi import FastAPI
from fastapi.responses import FileResponse
from utils import get_image
import tempfile

app = FastAPI()

@app.get("/")
def snapshot(url: str):
    image = get_image(url) # PIL Image
    # Save the image to a temporary file
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
        image.save(temp_file.name, format='JPEG')
    # Return the temporary file as a FileResponse
    return FileResponse(temp_file.name, media_type='image/jpeg')
    