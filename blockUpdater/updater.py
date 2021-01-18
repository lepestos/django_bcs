from apscheduler.schedulers.background import BackgroundScheduler
from . import blockApi


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(blockApi.update_blocks, 'interval', minutes=1)
    scheduler.start()
