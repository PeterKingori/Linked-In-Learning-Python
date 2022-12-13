#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
date_now = datetime.now()
print("Today's date is", date_now)

# print today's date one year from now
one_year_time_delta = date_now + timedelta(days=365)
print("The date one year from now will be", str(one_year_time_delta))

# create a timedelta that uses more than one argument
week_time_delta = date_now + timedelta(weeks=2, days=3)
print("In two weeks and 3 days it will be", str(week_time_delta))

# calculate the date 1 week ago, formatted as a string
past_time_delta = datetime.now() - timedelta(weeks=1)
formatted_date = past_time_delta.strftime("%A %B %d, %Y")
print("One week ago it was", formatted_date)

### How many days until April Fools' Day?
todays_date = date.today()
april_fools_day = date(todays_date.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if april_fools_day < todays_date:
    print("April Fools' Day has already passed:", ((todays_date - april_fools_day).days), "days ago.")
    april_fools_day = april_fools_day.replace(year=todays_date.year + 1)

# Now calculate the amount of time until April Fool's Day  
time_to_april_fools = april_fools_day - todays_date
print("It is", time_to_april_fools.days, " days until the next April Fools' Day.")
