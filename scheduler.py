import schedule
import time
from main import run_agent
from config import DAILY_TIME

def start_scheduler():
    print(f"Scheduler started — running daily at {DAILY_TIME}")
    print("Press Ctrl+C to stop\n")
    run_agent()
    schedule.every().day.at(DAILY_TIME).do(run_agent)
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    start_scheduler()