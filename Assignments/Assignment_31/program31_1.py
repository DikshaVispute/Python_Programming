# Write a program that accepts:
# • A message from the user
# • A time interval in seconds
# Schedule the program to display the message repeatedly after the specified interval.
# Example input:
# Enter message: Jay Ganesh
# Enter interval in seconds: 5
# Expected output:
# Jay Ganesh
# every five seconds.

# Validate that the interval is greater than zero.

import sys
import schedule
import time

def Display(Mesg):
    print(Mesg)

def main():
    if(len(sys.argv) == 3):

        Message = sys.argv[1]
        Interval = int(sys.argv[2])
    
        if(Interval <= 0):
            print("Invalid time interval")
            print("Time interval should be greater than zero")
            return
        
        schedule.every(Interval).seconds.do(Display,Message)

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()