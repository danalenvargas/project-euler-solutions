def compute(pos):
  count = 0
  num = 1
  primeList = []
  while(count < pos):
    num += 1
    for i in primeList:
      if num%i == 0:
        break
    else:
      count+=1
      primeList.append(num)
  return num

print(compute(10001))
  