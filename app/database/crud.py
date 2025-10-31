from uuid import UUID

from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Media


def create_media(
    session: Session, 
    uuid: UUID,
    link:str,
    expire: date,
) -> Media:
    media = Media(id=uuid, expire=expire, link=link)
    session.add(media)
    session.commit()
    return media


def get_media(session: Session) -> list[Media]:
    stmt = select(Media)
    result = session.execute(stmt)
    medias = result.scalars().all()
    return medias


def delete_expired_media(session: Session) -> None:
    today = datetime.utcnow().date()
    stmt = delete(Media).where(Media.expire < today)
    session.execute(stmt)
    session.commit()
