import random
import os 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_1 = []
dealer = []


def random_cards(deck):   
    card = random.choice(deck)
    return card
  
def first_round(list):
    first_card = int(random_cards(cards))
    second_card = int(random_cards(cards))
    list.extend([first_card, second_card])
    return list

def next_card(list):
    third_card = random_cards(cards)
    list.append(third_card)
    return list

def sum_score (list):
   result = 0
   for n in list:
       result += n
       if result == 21:
           return 0
       if 11 in list and result > 21:
           list.remove(11)
           list.append(1)
   return result

def compare (score1, score2):
    if score1 == score2:
        return "It's a draw."
    elif score2 == 0:
        return "You lose. Opponent has blackjack."
    elif score1 == 0:
        return "You win. You have blackjack."
    elif score2 > 21:
        return "Opponent went over. You win."
    elif score1 > 21:
        return "You went over. You lose."
    elif score1 > score2:
        return "You win."
    else:
        return "You lose."
    

print("Welcome to Blackjack. Let's play.")
input("Do you want to play? Type 'y' or 'n': ")

is_game_over = False
#Player 
first_round(player_1)
# dealer
first_round(dealer)
    
while not is_game_over: 
    player_score = sum_score(player_1)
    print(f"Your cards: {player_1}, current score: {player_score}")
    dealer_score = sum_score(dealer)
    print(f"Computer's first card: {dealer[0]}")
    
    if player_score == 0 or dealer_score == 0 or player_score > 21:
        is_game_over = True
    else:
        next_round = input("Type 'y' to get another card, 'n' to pass:\n")
        if next_round == 'y':
            next_card(player_1)
        else: 
            is_game_over = True

while sum_score(dealer) != 0 and sum_score(dealer) < 17:
    next_card(dealer)
    dealer_score = sum_score(dealer)

print(f"Your final hand: {player_1}, final score: {player_score}")
print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")
print(compare(player_score, dealer_score))


