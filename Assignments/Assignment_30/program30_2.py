# Write a Python program that displays the current date and time
# after every one minute.
# Use the datetime module.
# Expected output:
# Current Date and Time: 25-07-2026 04:30:00 PM

import schedule
import time
import datetime

def DisplayDatetime():
    CurrentTime = datetime.datetime.now()
    CurrentTime = CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p")
    print("Current Date and Time : ",CurrentTime)

def main():
    schedule.every(1).second.do(DisplayDatetime)

    while(True):
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()