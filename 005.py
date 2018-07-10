def compute(n1, n2):
  num = n2
  while(True):
    for i in range(n1, n2+1):
      if(num%i != 0):
        break
    else:
      break
    num += n2
  return num
  
print(compute(1,20))