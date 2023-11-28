import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

from ipynb.fs.full.agi import rf_model_1
from ipynb.fs.full.agi import rf_model_2
from ipynb.fs.full.agi import rf_model_3

moves = ['H','D','S','R'] #removed P (split)
player_cards = []
dealer_cards = []
game_winner = 'unknown'

# data = pd.read_excel('./blackjack cleaner.xlsx', sheet_name='blackjack_sample_500k')

# data.head()

# model_1_data = []
# model_2_data = []
# model_3_data = []

# #Test train split 1
# #Test Train split 2
# #Test Train split 3

# model_1 = []
# model_2 = []
# model_3 = []


def get_random_card():

    #ace == 11
    #k, q, j == 10
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card = np.random.choice(cards)

    return card

def predict_move_1(player_card_1, player_card_2, dealer_card, move_1):

    outcome = 'loss'

    if(rf_model_1.predict(player_card_1, player_card_2, dealer_card, move_1)) == 1:
        outcome = 'win'

    #predict the outcome of the game with the defined parameters

    #if the outcome is win, return win, else return loss

    return outcome

def predict_move_2(player_card_1, player_card_2, dealer_card_1, player_card_3, move_1, move_2):

    outcome = 'loss'
    if(rf_model_2.predict(player_card_1, player_card_2, dealer_card_1, player_card_3, move_1, move_2)) == 1:
        outcome = 'win'

    return outcome

def predict_move_3(player_card_1, player_card_2, dealer_card_1, player_card_3, player_card_4, move_1, move_2, move_3):

    outcome = 'loss'
    if(rf_model_3.predict(player_card_1, player_card_2, dealer_card_1, player_card_3, player_card_4, move_1, move_2, move_3)) == 1:
        outcome = 'win'

    return outcome

def dealer_moves():
    
    #Hit or stay
    proceed = True

    while proceed == True:

        dealer_value = sum(dealer_cards)

        if dealer_value <= 16:
            #hit less than or equal to 16
            dealer_cards.append(get_random_card())
        else:
            #stay > 16
            proceed = False

    

    #Hit when card_values <=16 or (A and 6) else stay

    return True

def select_winner(dealer_total, player_total):
    winner = 'Dealer'

    if abs(21 - player_total) < abs(21 - dealer_total):
        winner = 'Player'

    return winner


for turn in range(1,4+1):

    #every turn, evaluate each of the possible moves for win / loss, using the correct model.
    if turn == 1:

        winning_moves_1 = []

        #generate initial state of card game:
        #2 player cards
        #1 dealer up card
        player_card_1 = get_random_card()
        player_card_2 = get_random_card()
        dealer_card   = get_random_card()
        dealer_card_2 = get_random_card() #not revealed until player is done

        #append the cards to a list to keep track of scores
        player_cards.append(player_card_1)
        player_cards.append(player_card_2)
        dealer_cards.append(dealer_card)
        dealer_cards.append(dealer_card_2)

        
        for move in moves:

            outcome = predict_move_1(player_card_1, player_card_2, dealer_card ,move)

            if outcome == 'win':
                winning_moves_1.append(move)
        
        print(f'Your Cards: {player_card_1}, {player_card_2}')
        print(f"Dealer's Card: {dealer_card}")
        print('Winning Moves: ',winning_moves_1)

        #player choses a move.
        move_1 = input('Enter Your Move (H = Hold, S = Stand, D = Double, R = Surrender): ')
        print(f'Player move = {move_1}')

        #if player stays or doubles, the dealer takes their turn
        if(move_1 == 'S' or move_1 == 'D'):
            break
            #dealter's turn, break out of turns

    elif turn == 2:

        winning_moves_2 = []

        #get new cards, if pplayer's count is> 21 then end game as loss
        #dealer does not get new cards until player is done

        player_card_3 = get_random_card()
        player_cards.append(player_card_3)

        player_value = sum(player_cards)

        if(player_value > 21):
            game_winner = 'dealer'
            print('player loss')
            break #exit moves loop upon player loss

        for move in moves:

            outcome = predict_move_2(player_card_1, player_card_2, player_card_3, dealer_card, move_1=move_1, move_2=move)

            if outcome == 'win':
                winning_moves_2.append(move)
        
        print(f'Your Cards: {player_card_1}, {player_card_2}, {player_card_3}')
        print(f"Dealer's Card: {dealer_card}")
        print('Winning Moves: ',winning_moves_2)

        move_2 = input('Enter Your Move (H = Hold, S = Stand, D = Double, R = Surrender): ')
        print(f'Player move = {move_2}')

        if(move_2 == 'S' or move_2 == 'D'):
            break
            #dealter's turn, break out of turns
    
    elif turn == 3:
        #get new cards, if pplayer's count is> 21 then end game as loss

        winning_moves_3 = []

        player_card_4 = get_random_card()
        player_cards.append(player_card_4)

        player_value = sum(player_cards)

        if(player_value > 21):
            game_winner = 'dealer'
            print('player loss')
            break #exit moves loop upon player loss

        for move in moves:

            outcome = predict_move_3(player_card_1, player_card_2, player_card_3, player_card_4, dealer_card, move_1=move_1, move_2=move_2, move_3=move)

            if outcome == 'win':
                winning_moves_3.append(move)
        
        print(f'Your Cards: {player_card_1}, {player_card_2}, {player_card_3}, {player_card_4}')
        print(f"Dealer's Card: {dealer_card}")
        print('Winning Moves: ',winning_moves_3)

        move_3 = input('Enter Your Move (H = Hold, S = Stand, D = Double, R = Surrender): ')
        print(f'Player move = {move_3}')

        if(move_3 == 'S' or move_2 == 'D'):
            break
            #dealter's turn, break out of turns

    elif turn == 4:
        print('Joe Pesci Opened the door With your head')
    
    else:
        print('turn out of bounds')

#code only runs if the loop is broken, if the game contunes for more than 3 moves, 
#joe pesci opens the door with your head

if(game_winner == 'unknown'):

    dealer_moves()

    dealer_total = sum(dealer_cards)
    player_total = sum(player_cards)

    #if dealer > 21 then player wins
    if(dealer_total > 21):
        game_winner = 'player'
    else:
        game_winner = select_winner(dealer_total, player_total)

    print(f'Winner = {game_winner}')

else:
    pass




