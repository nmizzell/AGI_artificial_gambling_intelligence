import pandas as pd

moves = ['H','D','S','R'] #removed P (split)

data = pd.read_excel('./blackjack cleaner.xlsx', sheet_name='blackjack_sample_500k')

print(data.head())

# model_1_data = []
# model_2_data = []
# model_3_data = []

# #Test train split 1
# #Test Train split 2
# #Test Train split 3

# model_1 = []
# model_2 = []
# model_3 = []


# def get_random_card():

#     card = ['A','K','10','10','10']

#     return card

# def predict_move_1(player_card_1, player_card_2, dealer_card, move):

#     outcome = 'loss'

#     #predict the outcome of the game with the defined parameters

#     #if the outcome is win, return win, else return loss

#     return 'outcome'

# def predict_move_2(player_card_1, player_card_2, dealer_card_1, player_card_3, move):

#     return True

# def predict_move_3(player_card_1, player_card_2, dealer_card_1, player_card_3, player_card_4, move):

#     return True

# def dealer_moves(dealer_card_1, dealer_card_2):
    
#     #Hit or stay
#     #Hit when card_values <=16 or (A and 6)


#     return True


# for turn in range(1,3+1):

#     #every turn, evaluate each of the possible moves for win / loss, using the correct model.
#     if turn == 1:

#         winning_moves_1 = []

#         #generate initial state of card game:
#         #2 player cards
#         #1 dealer up card
#         player_card_1 = 'K'
#         player_card_2 = 'A'
#         dealer_card = 'A'

        
#         for move in moves:

#             outcome = predict_move_1()

#             if outcome == 'win':
#                 winning_moves_1.append(move)
        
#         print(f'Your Cards: {player_card_1}, {player_card_2}')
#         print(f"Dealer's Card: {dealer_card}")
#         print('Winning Moves: ',winning_moves_1)

#         #if player loses, or if the player stays or doubles, the delater takes their turn

#     elif turn == 2:
    
#     elif turn == 3:

#     else:
#         print('turn out of bounds')

