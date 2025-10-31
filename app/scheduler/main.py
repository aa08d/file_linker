from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session

from app.database.crud import delete_expired_media

import atexit


def init_scheduler(session: Session):
    scheduler = BackgroundScheduler()
    scheduler.add_job(delete_expired_media, 'cron', hour=0, minute=0, args=[session])
    scheduler.start()
    print("start")
    
    atexit.register(lambda: scheduler.shutdown())
  