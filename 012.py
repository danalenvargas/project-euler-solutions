import math

def countDivisors(n):
  count = 0
  if n > 1:
    for i in range(1, math.ceil(math.sqrt(n))):
      if n%i == 0:
        if n/i == i:
          count += 1
        else:
          count += 2
  else:
    return 1
  return count

def compute(dNum):
  count = 1
  num = 1
  while True:
    if countDivisors(num) > dNum:
      return num
    count += 1
    num += count
    
  
print (compute(500))