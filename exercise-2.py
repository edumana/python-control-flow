# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

x = ''
while(x != 'quit'):
  x = input ('Please enter a word or phrase: ')
  print(f'what you entered is {len(x)} characters long')

print('Bye!')
  



