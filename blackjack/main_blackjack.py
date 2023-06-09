############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#deal_card() function that uses the List  to return a random card.
import random
from art import logo
import os

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card= random.choice(cards)
  return card
#calculate_score() that takes a List of cards as input and returns the score. 
def calculate_score(cards):
#check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.     
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    #check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
  if sum(cards) >21 and 11 in cards:
      cards.remove(11)
      cards.append(1)
        
  return sum(cards)
#Create a function called compare() and pass in the user_score and computer_score. 
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. 
# If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. 
# If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

def compare(user_score,computer_score):
  
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose "

  if user_score == computer_score:
    return "Draw "
  elif computer_score == 0:
    return "Lose, opponent has Blackjack "
  elif user_score == 0:
    return "Win with a Blackjack!!"
  elif user_score > 21:
    return "You went over. You lose "
  elif computer_score > 21:
    return "Opponent went over. You win!!"
  elif user_score > computer_score:
    return "You win !!"
  else:
    return "You lose"
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over=False
    #Deal the user and computer 2 cards each using deal_card() and append().
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    #The score will need to be rechecked with every new card drawn and the checks need to be repeated until the game ends.
    while not game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards : {user_cards},Score :{user_score}")
        print(f"Computer's card 1 : {computer_cards[0]}")

        #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        if user_score==0 or computer_score==0 or user_score>21:
          game_over=True
        else:
        #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to 
        # add another card to the user_cards List. If no, then the game has ended.
          user_card_choice=input("Do you want to choose another card, Y/N")
          if(user_card_choice.upper()=='Y'):
            user_cards.append(deal_card())
          else:
            game_over=True  
    #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score<17 and computer_score != 0:
            computer_cards.append(deal_card())
            computer_score=calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('cls')
  play_game()
        


    