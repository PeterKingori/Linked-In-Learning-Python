#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print ("Today's date is ", today)

    # print out the date's individual components
    print ("Date Components: ", today.day, today.month, today.year)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    print ("Today's Weekday #: ", today.weekday())
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print ("Which is a " + days[today.weekday()])

    ## DATETIME OBJECTS
    # Get today's date and time from the datetime class
    today = datetime.now()
    print  ("The current date and time is ", today)

    # Get the current time
    current_time = datetime.time(datetime.now())
    print ("The current time is ", current_time)


if __name__ == "__main__":
    main()
  