# finding factorial of numbers
def factorial(y):
  count = 1
  for item in range(1, y+1):
    count = count * item 
  return count
    
print factorial(8)