from datetime import datetime
from dateutil.relativedelta import relativedelta
from pyfiglet import Figlet
import time

# Current date and time
now = datetime.now()

# Specified date and time in the past
datethen = {
    "year": 2019,
    "month": 11,
    "day": 13
}
timethen = {
    "hour": 17,
    "minute": 35,
    "second": 00
}

# Create datetime object for the past date and time
then = datetime(datethen["year"], datethen["month"], datethen["day"],
                timethen["hour"], timethen["minute"], timethen["second"])

# Calculate the difference
delta = relativedelta(now, then)

# Print the time difference
#print(f"Years: {delta.years}, Months: {delta.months}, Days: {delta.days}, Hours: {delta.hours}, Minutes: {delta.minutes}, Seconds: {delta.seconds}")

# Create Figlet object for ASCII art
f = Figlet(font='slant')

# Print "It's been..." in ASCII art
print(f.renderText("It's been..."))
time.sleep(1)

# Convert integer values to strings before printing with Figlet
print(f.renderText(str(delta.years)))
print(f.renderText("Years"))
time.sleep(1)

print(f.renderText(str(delta.months)))
print(f.renderText("Months"))
time.sleep(1)

print(f.renderText(str(delta.days)))
print(f.renderText("Days"))
time.sleep(1)

print(f.renderText(str(delta.hours)))
print(f.renderText("Hours"))
time.sleep(1)

print(f.renderText(str(delta.minutes)))
print(f.renderText("Minutes"))
time.sleep(1)

print(f.renderText(str(delta.seconds)))
print(f.renderText("Seconds"))
time.sleep(1)
print(f.renderText("since i ment my friend"))

