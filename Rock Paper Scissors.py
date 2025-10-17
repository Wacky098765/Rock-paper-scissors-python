from random import randint
from time import sleep
import getpass
plays = 0
wins = 0
losses = 0
draws = 0
game = 0
p1_wins = 0
p2_wins = 0
p1_losses = 0
p2_losses = 0
oneP_or_twoP = input("Do you want to play against a cpu or two player? (cpu, two)")
# decides whether or not user is playing a one player or two player
if oneP_or_twoP == "cpu":
     # creating the gameplay loop
     while game <= 5:
      comp = randint(1,3)
      if comp == 1:
        comp = "r"
      elif comp == 2:
        comp = "p"
      elif comp == 3:
        comp = "s"
      user = input("Enter your choice: Rock (R), Paper (P) or Scissors (S) ")
      user = user.lower()
    # draw scenario
      if comp == user:
        print(f"Computer: {comp} \nUser: {user} \nDraw!")
        draws += 1
        plays += 1
        game += 1
        sleep(2)
    # all loss scenarios
      if comp == "r" and user == "s":
        print(f"Computer: {comp} \nUser: {user} \nLoss!")
        losses += 1
        plays += 1
        game += 1
        sleep(2)
      elif comp == "p" and user == "r":
        print(f"Computer: {comp} \nUser: {user} \nLoss!")
        losses += 1
        plays += 1
        game += 1
        sleep(2)
      elif comp == "s" and user == "p":
        print(f"Computer: {comp} \nUser: {user} \nLoss!")
        losses += 1
        plays += 1
        game += 1
        sleep(2)
    # all win scenarios 
      if user == "r" and comp == "s":
        print(f"Computer: {comp} \nUser: {user} \nWin!")
        wins += 1
        plays += 1
        game += 1
        sleep(2)
      elif user == "p" and comp == "r":
        print(f"Computer: {comp} \nUser: {user} \nWin!")
        wins += 1
        plays += 1
        game += 1
        sleep(2)
      elif user == "s" and comp == "p":
        print(f"Computer: {comp} \nUser: {user} \nWin!")
        wins += 1
        plays += 1
        game += 1
        sleep(2)
      # play again loop
      if game == 5:
        play = input("Do you want to play again? ")
        if play == "yes" or play == "YES" or play == "Y" or play == "y":
            game = 0
        else:
            break
elif oneP_or_twoP == "two":
   while game <= 5:

    user1 = getpass.getpass(prompt= "Player One Your Turn: Rock (R), Paper (P) or Scissors (S) ")
    user1 = user1.lower()
    user2 = getpass.getpass(prompt= "Player Two Your Turn: Rock (R), Paper (P) or Scissors (S) ")
    user2 = user2.lower()
    # player 1 and player 2 draw
    if user1 == user2:
        print(f"Player 1: {user1} \nPlayer 2: {user2} \nDraw!")
        draws += 1
        plays += 1
        game += 1
        sleep(2)
    # player 1 win scenarios, player 2 loss scenarios
    if user1 == "r" and user2 == "s":
        print(f"Player 1: {user1} \nPlayer 2: {user2} \nPlayer 1: Win!")
        p2_losses += 1
        p1_wins += 1
        plays += 1
        game += 1
        sleep(2)
    elif user1 == "p" and user2 == "r":
        print(f"Player 1: {user1} \nPlayer 2: {user2} \nPlayer 1: Win!")
        p2_losses += 1
        p1_wins += 1
        plays += 1
        game += 1
        sleep(2)
    elif user1 == "s" and user2 == "p":
        print(f"Player 1: {user1} \nPlayer 2: {user2} \nPlayer 1: Win!")
        p2_losses += 1
        p1_wins
        plays += 1
        game += 1
        sleep(2)
    # player 2 win scenarios, player 1 loss scenarios
    if user2 == "r" and user1 == "s":
        print(f"Player 1: {user1} \nPlayer 2: {user2} \nPlayer 2: Win!")
        p2_wins += 1
        p1_losses += 1
        plays += 1
        game += 1
        sleep(2)
    elif user2 == "p" and user1 == "r":
        print(f"Player 1: {user1} \nPlayer 2: {user2} \nPlayer 2: Win!")
        p2_wins += 1
        p1_losses += 1
        plays += 1
        game += 1
        sleep(2)
    elif user2 == "s" and user1 == "p":
        print(f"Player 1: {user1} \nPlayer 2: {user2} \nPlayer 2: Win!")
        p2_wins += 1
        p1_losses += 1
        plays += 1
        game += 1
        sleep(2)
    # play again loop
    if game == 5:
        play = input("Do you want to play again? ")
        if play == "yes" or play == "YES" or play == "Y" or play == "y":
            game = 0
        else:
            break
if oneP_or_twoP == "cpu":
    print(f"Game Stats:\nRounds: {plays} \nWins: {wins}\nLosses: {losses}\nDraws: {draws}")
elif oneP_or_twoP == "two":
    print(f"Game Stats: \nRounds: {plays} \nPlayer 1 Wins: {p1_wins} Player 1 Losses: {p1_losses} \nPlayer 2 Wins: {p2_wins} Player 2 Losses: {p2_losses}")
    if p1_wins > p2_wins:
       print("Player 1 Wins!")
    elif p2_wins > p1_wins:
       print("Player 2 Wins!")
    elif p1_wins == p2_wins:
       print("Draw!")
print("Thanks for playing!")