from datetime import datetime, timedelta

from uuid6 import uuid7
from sqlalchemy import Column, UUID, String, DateTime, Date

from .base import Base


class Media(Base):
    __tablename__ = "medias"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    expire = Column(Date)
    link = Column(String(250))
    created_at = Column(
        DateTime,
        default=lambda: datetime.utcnow() + timedelta(hours=3)
    )
