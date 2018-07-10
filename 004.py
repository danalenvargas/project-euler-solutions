def getLargestPalindrome():
  max = 0
  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i*j
      if product > max and str(product) == str(product)[::-1]:
        max = product
  return max
    
print (getLargestPalindrome())