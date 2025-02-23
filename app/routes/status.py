from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models import ImageProcessingRequest

router = APIRouter()

@router.get("/{request_id}")
async def check_status(request_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ImageProcessingRequest).where(ImageProcessingRequest.request_id == request_id))
    request = result.scalar()

    if not request:
        return {"error": "Invalid Request ID"}
    
    return {"request_id": request_id, "status": request.status}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models import ImageProcessingRequest

router = APIRouter()

@router.get("/{request_id}")
async def check_status(request_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ImageProcessingRequest).where(ImageProcessingRequest.request_id == request_id))
    request = result.scalar()

    if not request:
        raise HTTPException(status_code=404, detail="Invalid Request ID")
    
    return {"request_id": request_id, "status": request.status}