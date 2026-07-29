# Create a function named:
# DisplayMessage(message)
# Schedule the function using:
# schedule.every(5).seconds.do(DisplayMessage, message)
# The message should be accepted from the user.

import sys
import schedule
import time

def DisplayMessage(Mesg):
    print(Mesg)

def main():
    if(len(sys.argv) == 2):

        Message = sys.argv[1]
        
        schedule.every(5).seconds.do(DisplayMessage,Message)

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()