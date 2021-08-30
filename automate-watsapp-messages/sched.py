from app import sendMessage
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler




sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(sendMessage, 'interval', seconds=2)

sched.start()