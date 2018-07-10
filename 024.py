import math

def decimalToFactorial(num):
  num = num - 1
  limit = 1
  ans = []
  if num == 0:
    ans.append(num)
    return ans
    
  while(True):
    if(num+1 <= math.factorial(limit + 1)):
      break
    limit += 1
      
  for i in range(limit, -1, -1):
    ans.append(num//math.factorial(i))
    num = num % math.factorial(i)
  return ans

def permutationByFactoradicIndex(num, elements):
  ans = ""
  if(len(num) > len(elements)):
    return "out of range"
  else:
    if(len(elements) > len(num)):
      for i in range(len(elements) - len(num)):
        ans += str(elements.pop(0))
    for i in range(len(num)):
      ans += str(elements.pop(num.pop(0)))
  return ans    

print(permutationByFactoradicIndex(decimalToFactorial(1000000), list(range(10))))