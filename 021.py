import math

divSums = [0] * 10000

def getDivSum(num):
  if num != 1 and divSums[num] == 0:
    sum = 1
    for i in range(2, math.floor(math.sqrt(num)) + 1):
      if num%i == 0:
        if num/i == i:
          sum += i
        else:
          sum += i + num//i
    divSums[num] = sum
  return divSums[num]
    
def compute():
  sum = 0
  for i in range(2, 10000):
    if getDivSum(i) < 10000 and i == getDivSum(divSums[i]) and i != divSums[i]:
      sum += i
  return sum
  
print(compute())