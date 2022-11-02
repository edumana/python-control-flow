# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

x = int(input("Input a dog's age in human years: "))

result = 0

if x != 0:
  for x in range(1,x+1):
    print(x)
    if(x<=2):
      result += 10
    elif(x>=3):
      result += x
  
print(f"The dog's age in dog years is {result}")

