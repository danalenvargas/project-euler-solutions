chains = [0] * (10**6)

def colatz(num):
  if num == 1:
    return 1
  elif num < len(chains) - 1 and chains[num] != 0:
    return chains[num]
  elif num%2 == 0:
    return (1 + colatz(num//2))
  else:
    return (1 + colatz(num*3 + 1))

def compute(limit):
  ans = 0
  maxCount = 0
  for i in range(1, limit):
    chains[i] = colatz(i)
  
    if chains[i] > maxCount:
      maxCount = chains[i]
      ans = i
  return ans
  
print(compute(1000000))
    