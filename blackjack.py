############### Blackjack Project #####################
import random
from art import logo


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(list_of_cards):
    """Take a list of cards and return the score calculated from the cards"""
    score = sum(list_of_cards)
    if score == 21:
      return 0
    if 11 in list_of_cards and score > 21:
       list_of_cards.remove(11)
       list_of_cards.append(1)
       score = sum(list_of_cards)
    return score


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose "

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "User looses, dealer has blackjack"
    elif user_score == 0:
        return "User wins with blackjack"
    elif user_score > 21:
        return "User looses, score over 21"
    elif computer_score > 21:
        return "User wins, dealer went over 21"
    elif user_score > computer_score:
        return "User wins with higher score"
    else:
        return "Dealer wins"


def game():
    print(logo)


    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())

    while not game_over:
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f" Your cards are: {user_cards}, current score: {user_score}")
      print(f" Computer's first card is {computer_cards[0]}")

      if computer_score == 0 or user_score == 0 or user_score > 21:
        game_over = True
      else:
        deal = input("Do you want to deal a card? y or n ")

        if deal == "y":
          user_cards.append(deal_card())
        else:
          game_over = True

    while computer_score < 17 and computer_score != 0:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

  while input("Do you want to play a game of blackjack? y or n: ") == "y":
    game()