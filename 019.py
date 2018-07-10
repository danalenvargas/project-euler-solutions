monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def compute():
  lastDay = 1
  count = 0
  for year in range(1901, 2001):
    for month in range(12):
      if lastDay == 6:
        count += 1
      if month == 1 and (year) % 4 ==0 and ((year) % 100 != 0 or (year) % 400 == 0):
        lastDay = (lastDay + 29) % 7
      else:
        lastDay = (lastDay + monthDays[month]) % 7
  return count
  
print(compute())