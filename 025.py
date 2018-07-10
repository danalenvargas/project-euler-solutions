def compute(digits):
  n1 = 1
  n2 = 1
  count = 2
  while(n2 < 10**(digits-1)):
    count += 1
    newN = n1 + n2
    n1 = n2
    n2 = newN
  return count
  
print(compute(1000))