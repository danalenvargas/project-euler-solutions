def compute():
  for a in range(1, 998):
    for b in range(1, 998-a):
      c = 1000 - a - b
      if(a**2 + b**2 == c**2):
        return a*b*c
  return False

print(compute())