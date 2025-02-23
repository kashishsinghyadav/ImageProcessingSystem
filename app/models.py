from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ImageProcessingRequest(Base):
    __tablename__ = "image_processing_requests"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(String, unique=True, index=True)
    product_name = Column(String)
    input_image_urls = Column(Text)  
    output_image_urls = Column(Text, nullable=True)  
    status = Column(String, default="pending")  
    
