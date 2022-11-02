# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

f_0 = 0
f_1 = 1
f_2 = 1

x = int(input('Up to what term should we calculate the sequence?: '))

if x == 0:
  print('Wrong input')
else:
  def fibonacci(term):
    if(term == 1):
      return(f_1)
    if(term == 2):
      return(f_2)
    else:
      return fibonacci(term-1) + fibonacci(term-2)
      
print(fibonacci(x))




