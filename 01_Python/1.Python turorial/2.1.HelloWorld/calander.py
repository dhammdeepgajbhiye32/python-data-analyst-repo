import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Create a TextCalendar instance
cal = calendar.month(year, month)
# Print the month's calendar
print(cal)