import random
import replit

#For comparing the scores of user and computer.
def compare(user_score, computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose! With a blackJack"
    elif user_score == 0:
        return "You Win! With a blackJack"
    elif user_score > 21:
        return "You went over. You Lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You loose"
    

#Getting random card from the deck
def deal_card():
    card = random.choice(deck)
    return card

#Calculating the score of both the players
def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)   
    return sum(cards)

deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]


#Play function 
def play_game():

    user_cards = []
    computer_cards = []
    is_gameover = False

    #Giving the initial two cards to both the players
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_gameover == False:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)
        print(f"Your cards: {user_cards}, current score {user_score}")
        print(f"Computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score>21:
            is_gameover = True
        else:
            new_game = input("Do you want another card? Type 'y' for yes and 'n' for no. ")
            if new_game == "y":
                user_cards.append(deal_card())
            else: 
                is_gameover = True

    #Comparing that computer have won the game or got the score.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)

    print(f"User's cards: {user_cards}, and current score is: {user_score}")
    print(f"Computer's cards: {computer_cards}, and computer score is: {computer_score}")

    print(compare(user_score, computer_score))


#Asking weather user wants to play the game or not keep asking until they want
while input("Do you want to play a game of BlackJack? Type 'y' or 'n'. "):
    replit.clear()
    play_game()