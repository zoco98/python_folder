def is_leap_year(year):
    leap_year = False
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False
    
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  days = 0
  if is_leap_year(year) and month==2:
    days = 29
  elif is_leap_year(year) and month!=2:
    days = month_days[month]
  else:
    days = month_days[month-1]
  return days
  
year = int(input("Enter a year:\n "))
month = int(input("Enter a month:\n"))
days = days_in_month(year, month)
print(days)


