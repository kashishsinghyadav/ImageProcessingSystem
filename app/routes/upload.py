import pandas as pd
import uuid
import aiofiles
from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import ImageProcessingRequest
from worker.tasks import process_images

router = APIRouter()

@router.post("/")
async def upload_csv(file: UploadFile, db: AsyncSession = Depends(get_db)):
    request_id = str(uuid.uuid4())

    async with aiofiles.open(f"/tmp/{request_id}.csv", "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    # Store request in DB
    new_request = ImageProcessingRequest(request_id=request_id, status="pending")
    db.add(new_request)
    await db.commit()

    # Trigger Celery Task
    process_images.delay(request_id, f"/tmp/{request_id}.csv")

    return {"request_id": request_id}
