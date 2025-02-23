from celery import Celery
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

celery = Celery("tasks", broker="redis://redis:6379/0")

@celery.task
def process_images(request_id, file_path):
    df = pd.read_csv(file_path)
    
    for _, row in df.iterrows():
        output_urls = []
        for img_url in row["Input Image Urls"].split(","):
            response = requests.get(img_url.strip())
            img = Image.open(BytesIO(response.content))
            output_path = f"/tmp/{request_id}_{row['Serial Number']}.jpg"
            img.save(output_path, quality=50)

            output_urls.append(output_path)  