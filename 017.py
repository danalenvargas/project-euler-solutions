NUMBERS = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
TENS = [6, 6, 5, 5, 5, 7, 6, 6]

def count(num):
  if num == 0:
    return 0
  elif num == 1000:
    return 11
  elif num > 99:
    if num % 100 == 0:
      return NUMBERS[num//100 - 1] + 7
    else:
      return NUMBERS[num//100 - 1] + 10 + count(num % 100)
  elif num > 19:
    return TENS[num//10 - 2] + count(num % 10)
  else:
    return NUMBERS[num - 1]
    
def compute(num):
  sum = 0
  for n in range(1, num+1):
    print(str(n) + " = " + str(count(n)))
    sum += count(n)
  return sum
  
print(compute(1000))