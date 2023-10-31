from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI
from server.core.config import *
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger
from server.routes.testing_routes import api_router, root


app = FastAPI(
    title=PROJECT_NAME, VERSION=VERSION, debug=DEBUG
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(api_router, tags=['Api Example'])


@app.on_event("startup")
def init_data():
    try:
        scheduler = BackgroundScheduler()
        trigger = CronTrigger(month='*', day='*', hour='01', minute='*')
        scheduler.add_job(root, trigger=trigger, id='job_id_1', replace_existing=True)
        scheduler.start()
        scheduler.print_jobs()
    except Exception as error:
        logger.error(f"Error: {error}")
