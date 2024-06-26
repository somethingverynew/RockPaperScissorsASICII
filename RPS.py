import random
from typing import Counter

options = ('rock', 'paper', 'scissors')

running = True

print()

wins = 0
losses = 0
ties = 0

rock_art = """
ROCK!!!
                       ░░░░░░░░░░░░░         
                ░░░░░░░░░░░░░░░░░░░░░░       
            ░░░▒▒▒▒▒▒▒▒░▒░▒▒░░░░░░░▒▒▒▒░     
          ░░▒░░░▒▒▒▒▒▒░░░░░░░░░░░▒▒▒░░▒▒▒░   
         ░░░▒▒░░▒▒▒▒▒░▒░░░░░▒░░░░▒▒▒▒▒▒▒▒▒▒  
       ░░░░░░░▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▓▓▒  
     ░░░░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒  
   ░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▒▒▓▓▒░ 
  ░▒▒░░░░░░░▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▓▓▓▓░ 
 ░▒▒▒▒░░▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▒░
 ▒▒▒▒▒▒▒▒░░░▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒
░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒▓▓███▓▓▓█▒ 
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒░      
    ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒░               
          ░░▒▒▒▒▒▒▒▒▒▒░                      
"""
paper_art = """
PAPER!!!

░░░░░░░░▒▒▒▒░░░░░░░░░░░░▒░▒░░▒░░░   
░░░▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒░░▒░░▒▒▒░   
 ▒░░░░░░▒▒▒▒▒░░░▒▒▒▒▒▒▒░░░▒░░▒░▒░   
 ░░▒▒░░░░▒░░░░░░░░░░░░░░░░▒░░▒░▒    
 ▒░░░░░░░░░░▒▒▒░░░░░░░░░░░▒░░▒░▒    
░▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▒░░░░▒▓░   
░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒    
░░▒▒▒▒▒▒░░░░░░░░░░░▒▒▒▒░░░░░░▒▒▒░   
░░░░▒░▒░░░░░░░░░░░░▒▒▒░░ ░░▒▒▒▒▒░   
░░ ▒▒▒░░░░░░░░░▒░▒▒▒▒░░ ░░░░▒▒▒▒░   
 ░░▒▒░░░▒▒▒▒▒▒░░░░░░░░ ▒▒░░░▒▒▒▒▒   
░░▒░░▒▒▒▒▒▒▒▒▒▒▒▒░▒░░░▒▒░░░▒▒▒▒▒░   
░▒▒░▒▒▒▒▒▒▒░░░▒░░▒░░░░▒▒▒░▒▒▒▒▒▒▒   
░▒░░░▒▒▒▒░░░░░ ░░▒▒▒▒▒▒░░░▒▒▒▒▒▒░   
 ░░░░░▒▒░░░░░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒░▒    
 ░░░░░░▒░░░▒▒▒░░░░░░░░░░░▒▒▒▒▒░░░   
 ░░░░░░▒░░▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒    
░░░░░░░░▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░    
░▒▒▒▒▒▒▒▒░░░▒▒▒▒▒▒▒▒▒▒░░  ░░░░░░░   
"""
scissors_art = """         
SCISSORS!!!
 
        ▒█         ▒█         
        ▓░█       ░▒▒▒        
        ▓░░▒      ▓░▓░        
        ░▓░▓░    ▓░░▒         
         ▒░░▓   ░▒░▓░         
         ░█░░▓ ░▓░▒▓          
          ░▒░░▒▓░░▓           
           ▓░░▓▒░▒▒           
            ▓░░▒░▒            
            ░▒▒▒█░            
            ▒░▒░░▒            
           ▓▓▓▒▒▒▓▓           
          █▓▓▓▒▒▓▓▓█          
     ░░▒▒▓▓▓▓█  █▓▓▓▓▒▒▒░░    
  ▒▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▒  
 ▓▓▓▒░ ░▓▓▓▓▒    ▒▓▓▓▓░  ▒▓▓▓ 
░▓▓▒    ▓▓▓▓      ▓▓▓▓    ▒▓▓▒
▒▓▓░    ▓▓█░      ░█▓▓░   ░▓▓▒
░▓▓▓▒░▒▓▓▓░         ▓▓▓▓▒▓▓▓█░
  ▒█▓▓▓▓▓            ▒▓▓▓▓█░  
"""
print("Welcome to Rock, Paper, Scissors!")

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
      player = input('Select either (rock, paper, or scissors): ')
      if player not in options:
        print("Invalid entry.")

    if player == "rock":
      print("You chose:\n" + rock_art)
    if computer == "rock":
      print("Computer chose:\n" + rock_art)

    if player == "paper":
      print("You chose:\n" + paper_art)
    if computer == "paper":
      print("Computer chose:\n" + paper_art)

    if player == "scissors":
      print("You chose:\n" + scissors_art)
    if computer == "scissors":
      print("Computer chose:\n" + scissors_art)

    if player == computer:
      print("It's a tie!")    
      ties += 1
    elif player == "rock" and computer == "scissors" or \
    player == "paper" and computer == "rock" or \
    player == "scissors" and computer == "paper":
      print("You win!")
      wins += 1
    else:
      print("You lose!")
      losses += 1 
    print (f"wins: {wins} losses: {losses} ties: {ties}")
  
    play_again = input("Would you like to play again? (yes/no): ")
    while play_again.lower() not in ['yes', 'no']:
      print("Invalid entry.")
      play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() != "yes":

      running = False

print("""
░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░
░░████████████░░░█████████████████░░░░░""")
print("Thank you for playing!")
print("Have a wonderful day!")