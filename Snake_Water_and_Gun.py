import random

print("\nSNAKE, WATER AND GUN GAME")
print('''Rule: 
      1. Gun beats Snake
      2. Snake beats Water
      3. Water beats Gun
      ''')

round = 1
Player_Score = 0
Device_Score = 0

while True:
  
  print(f"Round: {round} | Current Score: {Player_Score} | Device Score: {Device_Score}\n")
  option = ['Snake', 'Water', 'Gun']

  print(f"{"":<2}Choose an option between the following:")
  for index, value in enumerate(option, start = 1):
    print(f"{"":<3}{index}. {value}")

  user_input = int(input("choice a number between 1-3: "))

  if user_input == 1:
    
    print("\nThe User have choosen the option 1 which is Snake")
    device_choice = random.choice(option)
    print(f"The Device have choosen {device_choice}.")
    
    if device_choice == 'Snake':
      print("It is a Draw.\n")
    elif device_choice == 'Water':
      print("You have Won the round.\n")
      Player_Score += 1
    else:
      print("You have Lost the round.\n")
      Device_Score += 1
    
    round += 1

  elif user_input == 2:
    
    print("\nThe User have choosen the option 2 which is Water")
    device_choice = random.choice(option)
    print(f"The Device have choosen {device_choice}.")
      
    if device_choice == 'Water':
      print("It is a Draw.\n")
    elif device_choice == 'Gun':
      print("You have Won the round.\n")
      Player_Score += 1
    else:
      print("You have Lost the round.\n")
      Device_Score += 1
    
    round += 1

  elif user_input == 3:
    
    print("\nThe User have choosen the option 3 which is Gun")
    device_choice = random.choice(option)
    print(f"The Device have choosen {device_choice}.")
      
    if device_choice == 'Gun':
      print("It is a Draw.\n")
    elif device_choice == 'Snake':
      print("You have Won the round.\n")
      Player_Score += 1
    else:
      print("You have Lost the round.\n")
      Device_Score += 1
      
    round += 1

  else:
    print("Invalid Input, Kindly Enter the correct input between 1-3.")
  
  if Player_Score == 5 or Device_Score == 5:
    if Player_Score == 5:
      print("Congratulations! You have won the game.")
    else:
      print("Sorry! You have lost the game. Better luck next time.")
    break
  
  
  
