############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# both dealer and player draw two cards.
## create list data type for dealer and user to store card values

dealer_cards = []
player_cards = []

for participant in [dealer_cards, player_cards]:
    for draw in range(2):
        participant.append(random.choice(cards))

# print(dealer_cards)
# print(player_cards)

# 1 card from the dealer is revealed

print("Dealer: " + str(dealer_cards[1]))
dealer_total = dealer_cards[0] + dealer_cards[1]

# both cards from the user are revealed

print("Player: " + str(player_cards[0]) + " " + str(player_cards[1]))
player_total = player_cards[0] + player_cards[1]

# is current value for user 21

if player_total > 21:
    print("Player Bust!")

# check to see if dealer is also 21, if so draw, if no user auto wins

# if value is not 21, ask if user want to draw another card (y, n)

# if no, confirm probablity for dealer to see if they can draw another card

# compare values to determine the winner

# if yes to draw another user card, draw a random card and follow logic from from above.

# ask if the user wants to play again

# if yes, clear and reset the game

# if no, thank player for playing and exit program.