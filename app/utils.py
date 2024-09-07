from PIL import Image
import ffmpeg
import io
def get_image(url):
    snapshot = ffmpeg.input(url, rtsp_transport = "tcp", timeout = 5000000)
    image_data, _ = ffmpeg.output(snapshot, 'pipe:', format='image2', vframes=1).run(capture_stdout=True)
    image = Image.open(io.BytesIO(image_data))
    return image