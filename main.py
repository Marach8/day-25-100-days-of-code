print('\033[35mCHARACTER STATS GENERATOR\033[0m')
print()

def rollDice(num):
  import random
  number = random.randint(0, num)
  return number

ask = int(input('What is the number of sides of your dice?: '))
print()
print(f'you rolled {rollDice(ask)}')
print()

def rollDice1():
  import random
  num1 = random.randint(1, 6)
  num2 = random.randint(1, 8)
  result = num1 * num2
  return result

while True:
  name = input('\033[34mName you warrior: \033[0m')
  print()
  health_stat = rollDice1()
  print(f'\033[32mTheir health is: {health_stat}hp.\033[0m')
  print()
  
  