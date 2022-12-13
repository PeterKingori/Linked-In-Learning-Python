#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar

# create a plain text calendar
clndr = calendar.TextCalendar(calendar.MONDAY)
calendar_string = clndr.formatmonth(2022, 1, 0, 0)
print(calendar_string)

# create an HTML formatted calendar
html_calendar = calendar.HTMLCalendar(calendar.MONDAY)
html_string_calendar = html_calendar.formatmonth(2022, 1)
print(html_string_calendar)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in clndr.itermonthdays(2022, 12):
    print(i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on:")
for month in range(1, 13):
    cal = calendar.monthcalendar(2023, month)
    week_one = cal[0]
    week_two = cal[1]
    if week_one[calendar.FRIDAY] != 0:
        meeting_day = week_one[calendar.FRIDAY]
    else:
        meeting_day = week_two[calendar.FRIDAY]

    print(calendar.month_name[month], meeting_day)
