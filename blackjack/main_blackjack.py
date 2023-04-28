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
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card= random.choice(cards)
  return card
#calculate_score() that takes a List of cards as input and returns the score. 
def calculate_score(cards):
#check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.     
  if 11 in cards and 10 in cards and len(cards)==2:
    sum_cards=0
    #game_ends=True
    return sum_cards
   
  sum_cards=sum(cards)
#check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
  if sum_cards>21 and 11 in cards:
      cards.remove(11)
      cards.append(1)
      sum_cards=sum(cards)
    
  return sum_cards
user_cards = []
computer_cards = []
game_over=False
#Deal the user and computer 2 cards each using deal_card() and append().
for _ in range(2):
  deal_card()
  user_cards=user_cards.append(deal_card())
  computer_cards=computer_cards.append(deal_card())
  
user_score=calculate_score(user_cards)
computer_score=calculate_score(computer_cards)
print(f"Your cards : {user_cards},Score :{user_score}")
print(f"Computer's card 1 : {computer_cards[0]}")

#Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
if user_score==0 or computer_score==0 or user_score>21:
  game_over=True


while(True):
  input_choice=input("Do you want to choose another card, Y/N")
  if(input_choice=='Y'):
    user_cards.append(deal_card())
