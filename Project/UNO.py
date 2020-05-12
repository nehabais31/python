'''
UNO text based game

Initial Setup: 2 - 4 players game
               Total cards = 108 : 4 suits [blue, green, yellow, red]
               1card  - 0 index for each suit
               2cards each  - 1-9 & skip , reverse, draw 2 
               4 cards each - wild & wild draw 4
               Each player will get a hand of 7 cards
               Random player is sleected from players list to play first turn
               
Rules: 1. You must play a valid card either of same number or same color or wild card
       2. Reverse card changes the drection of play
       3. Draw 2 card makes the next player to draw 2 cards and skip their turn
       4. Skip card , skips the next player's turn
       5. Wild card : allows the player to change the color of game
       6. Wild Draw 4 : allows the player to change the color as well as makes the next player to draw 4 cards and skips their turn
       7. You can draw a card fom deck if you don't have a valid card to play
       8. Player who replenishes his hand first will win
  
@author : Neha Bais
MET CS-521 Term Project
     
'''

import random
import sys

class UnExpectedValueError(Exception):
    '''
    Class defined for exception handling
    '''
    def __init__(self, data):
        self.data = data
        
    def __str__(self):
        return repr(self.data)
    

class UnoCard:
    '''
    Class for Card, where each card has a color and a type
    '''
    def __init__(self, color, card_type):
        self.card_color = color
        self.card_type = card_type

    def __str__(self):
        return f'{self.card_color} {self.card_type}'

    __repr__ = __str__


class Player:
    '''
    Class for a player in which each player has a name and a hand
    '''
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return f'{self.name} has a hand of {self.hand}'

    __repr__ = __str__


class Deck:
    '''
    Create Deck for the game
    '''
    def __init__(self):
        self.deck = []
        
    def create_deck(self):
        '''
        Create our UNO deck
        '''
        self.card_colors = ['blue', 'red', 'green', 'yellow']
        self.colored_cards = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'draw two', 'skip', 'reverse']
    
    
        # Create cards of each color and type for the deck
        for color in self.card_colors:
            for card_type in self.colored_cards:
                if card_type == '0':
                    # Uno decks only have one 0 card of each color
                    self.deck.append(UnoCard(color, card_type))
                else:
                    # Every other colored card appears twice in an Uno deck
                    self.deck.append(UnoCard(color, card_type))
                    self.deck.append(UnoCard(color, card_type))
   
    
        # Add 4 wild cards and 4 wild draw 4 cards to the deck
        for i in range(4):
            self.deck.append(UnoCard('wild', 'wild'))
            self.deck.append(UnoCard('wild', 'wild draw 4'))
        return self.deck


    def is_deck_empty(self):
        '''
        Check whether the deck is empty or not
        '''
        if self.deck:
            return False
        else:
            return True    
 
    
class Game:
    '''
    Main Game play 
    '''
    def __init__(self):
        self.deck = []          # Cards that have not been played
        self.players_list = []  #List to store all players that are playing
        self.discard_pile = []  # Cards that have been played, where the last card in the list is the one on top of the pile
        self.play_direction = 'clockwise'


    def reverse_play_direction(self):
        '''
        Reverse the directon of play when reverse card is played
        '''
        global play_direction
        if self.play_direction == 'clockwise':
            self.play_direction = 'counterclockwise'
        else:
            self.play_direction = 'clockwise'
        print('\n\nChanging directions!')


    def draw_card(self, Player):
        '''
        Draw a card for player when player dos not have a valid card to play
        '''
    
        # If the deck is empty: add all the cards from the discard pile (except the last one) back to the deck
        if Deck.is_deck_empty(self):
            for self.discard_card_index in range(0, len(self.discard_pile) - 2):
                self.deck.append(self.discard_pile.pop(self.discard_card_index))
    
        # Get the index of the card to be drawn
        card_index = random.randint(0, len(self.deck) - 1)
    
        # Get the card at that index and add it to the hand
        card = self.deck.pop(card_index)
        Player.hand.append(card)
        return card


    def create_hand(self):
        '''
        Create a starting hand of 7 cards for player
        '''
        hand = []
    
        # Draw 7 cards for a starting hand
        for draw_card in range(7):
            # Get the index of the card to be drawn
            card_index = random.randint(0, len(self.deck) - 1)
    
            # Get the card at that index and add it to the hand
            card = self.deck.pop(card_index)
            hand.append(card)
        return hand


    def create_players(self):
        '''
        Create Players for the game and initilize each player with a playing hand of 7 cards
        Number of players allowed can be between 2 and 4
        '''
    
        # Get the number of players playing
        valid_players = False
    
        while not valid_players:
            try:
                number_of_players = input('Number of players? (2 - 4): ')
                if number_of_players.isnumeric() and 2 <= int(number_of_players) <= 4:
                    number_of_players = int(number_of_players)
                    valid_players = True
                else:
                    raise UnExpectedValueError('Sorry, Please enter a valid input (2 - 4)\n')
            except UnExpectedValueError as e:
                print('InputError: ', e.data)
                 
    
        # Create a Player for each player with a starting hand
        for player in range(number_of_players):
            # Get the name of the player
            valid_name = False
            while not valid_name:
                try:
                    player_name = input(f'Enter the name for player {player + 1}: ')
                    if not player_name.isspace() and player_name != '':
                        valid_name = True
                    else:
                        raise UnExpectedValueError('You cannot leave the name blank\n')
                except UnExpectedValueError as e:
                    print('InputError: ', e.data)
            
            # Create a hand for the player
            hand = self.create_hand()
        
            # Create a Player and add it to the players_list
            self.players_list.append(Player(player_name, hand))
    
        return self.players_list


    def create_start_dis_pile(self):
        '''
        To create the discard pile. The first card must be a Number card not special card
        '''
        invalid_types = ['wild', 'wild draw 4', 'draw two', 'skip', 'reverse']
        valid_starter = False
    
        # Select a random card from the deck until you get one that is a number
        while not valid_starter:
            # Get the index of the card to be drawn
            card_index = random.randint(0, len(self.deck) - 1)
    
            # Get the card at that index
            card = self.deck[card_index]
    
            # Check if that card is a valid card to start on
            if card.card_type not in invalid_types:
                valid_starter = True
                self.discard_pile.append(self.deck.pop(card_index))
        return self.discard_pile


    def is_valid_move(self, card):
        '''
        Check whether a valid move is made.
        Valid move is when a player plays a card with same color or type
        as the card that is on top of discard pile, or the card is a wild card
        '''
        if card.card_type == self.discard_pile[-1].card_type or card.card_color == self.discard_pile[-1].card_color or card.card_color == 'wild':
            return True
        else:
            return False


    def play_card(self, player_index, card_index):
        '''
        Function to play a card
        '''
    
        # Take the played card out of the player's hand and add it to the discard pile
        played_card = self.players_list[player_index].hand.pop(card_index)
        self.discard_pile.append(played_card)
    
        return self.discard_pile


    def play_turn(self, current_player_index):
        '''
        Function to go through a player's turn
        '''
    
        print(f'\n\n\t\t\t\t\t\t***  {self.players_list[current_player_index].name}\'s turn. ***')
        print('The top card is: \t\t', self.discard_pile[-1])
    
        hand_statement = f'{self.players_list[current_player_index].name}\'s cards:'
        card_number = 1
    
        for card in self.players_list[current_player_index].hand:
            hand_statement += f'   {card_number}.) {card}'
            card_number += 1
        print(hand_statement)
    
        valid_input = False
        cards_in_players_hand = len(self.players_list[current_player_index].hand)
    
        while not valid_input:
            decision = input('Enter the number of the card you want to play, or type \'d\' to draw a card.')
        
            # If the user wants to draw a card:
            if decision == 'd':
                print(f'{self.players_list[current_player_index].name} will draw a card.')
            
                # Draw a card and see if it can be played
                card_drawn = self.draw_card(self.players_list[current_player_index])
            
                # If the card drawn can be played, play it
                if self.is_valid_move(card_drawn):
                    print(f'{self.players_list[current_player_index].name} drew a {card_drawn} that can be played!')
                    self.play_card(current_player_index, -1)
                    card_type = self.discard_pile[-1].card_type
                    return card_type
            
                # If it can't be played, just add it to hand
                return None
        
            # If the user wants to play a card:
            elif decision.isnumeric():
                if 1 <= int(decision) <= cards_in_players_hand:
                    # Check if the move is valid
                    if self.is_valid_move(self.players_list[current_player_index].hand[int(decision) - 1]):
                        self.play_card(current_player_index, int(decision) - 1)
                        # Get the type of the card that was just played to see if there are extra actions to be done now
                        # like +2, skip, etc.
                        card_type = self.discard_pile[-1].card_type
                        return card_type
                    print('Sorry, that move is not valid. If you have no valid moves please draw a card.')


    def change_color(self):
        '''
        Function to change the color of current play when wild card is played
        '''
    
        valid_input = False
        valid_inputs = ['blue', 'yellow', 'green', 'red']
        
        while not valid_input:
            new_color = input('Wild card played! What is the color for next turn?: ')
            if new_color.lower() in valid_inputs:
                valid_input = True
            else:
                print('Please select a valid color (blue, yellow, green, red)')
        self.discard_pile[-1].card_color = new_color


    def advance_turn(self, current_player_index):
        '''
        This function will advance the turn
        '''
    
        index = current_player_index
        number_of_players = len(self.players_list)
        if self.play_direction == 'clockwise':
            index += 1
            if index > (number_of_players - 1):
                index = 0
        elif self.play_direction == 'counterclockwise':
            index -= 1
            if index < 0:
                index = (number_of_players - 1)
        return index


    def play_uno(self):
        '''
        This function will play the game
        '''
    
        Deck.create_deck(self)
        self.create_players()
        self.create_start_dis_pile()
        self.game_won = False
    
        # The index of the player who's turn it is
        current_player_index = random.randint(0, len(self.players_list) - 1)
    
        # Play until the game is won (a player has no cards)
        while not self.game_won:
            played_card_type = self.play_turn(current_player_index)
        
            # If a wild card is played, change the color of the top card
            if played_card_type == 'wild':
                self.change_color()
        
            # If a skip card is played, advance the turn twice to skip the next player
            if played_card_type == 'skip':
                current_player_index = self.advance_turn(current_player_index)
                print(f'\n\nSkipping {self.players_list[current_player_index].name}\'s turn!')
        
            # If a reverse card is played, reverse the direction of play
            if played_card_type == 'reverse':
                self.reverse_play_direction()
        
            # If a draw two card is played, have the next player draw 2 cards, then skip their turn
            if played_card_type == 'draw two':
                current_player_index = self.advance_turn(current_player_index)
                print(f'\n\n{self.players_list[current_player_index].name} draws two cards and loses their turn!')
                self.draw_card(self.players_list[current_player_index])
                self.draw_card(self.players_list[current_player_index])
        
            # If a wild draw 4 card is played, change the color, have the next player draw 4 cards, then skip their turn
            if played_card_type == 'wild draw 4':
                self.change_color()
                current_player_index = self.advance_turn(current_player_index)
                print(f'\n\n{self.players_list[current_player_index].name} draws four cards and loses their turn!')
                for i in range(4):
                    self.draw_card(self.players_list[current_player_index])
        
            # Advance the turn once
            current_player_index = self.advance_turn(current_player_index)
        
            # The game is won when a player runs out of cards. Check if there is a winner:
            for player in self.players_list:
                if len(player.hand) == 0:
                    self.game_won = True
                    print(f'\n\n*** Congratulations, {player.name} has won the game! ***')


    def initialize_game(self):
        '''
        Initial screen for game
        '''
        print("*********************************************************************")
        print('*                                                                   *')
        print('*                 **     **  ***        **   ******                 *')
        print('*                 **     **  **  *      **  *      *                *')
        print('*                 **     **  **    *    **  *      *                *')
        print("*                 **     **  **      *  **  *      *                *")
        print('*                   * * *    **        ***   ******                 *')
        print('*                                                                   *')
        print('*     P: Play                                            Q: Quit    *')
        print('*                                                                   *')
        print('*********************************************************************')
            
        
        #Asks the player to input Play or Quit option
        valid_input = False
        while not valid_input:
            try:
                playerInput = input('\nPlease enter P to play or Q to quit: ')
                if playerInput.lower() == 'p' or playerInput.lower() == 'q':
                    valid_input = True
                else:
                    raise UnExpectedValueError('Sorry, Please enter a valid input (p or q)')
            except UnExpectedValueError as e:
                print('InputError: ', e.data)
            
            if playerInput.lower() == 'p' :
                continue
            elif playerInput.lower() == 'q':
                print('\nBye Bye !!!!')
                sys.exit()    
            

if __name__  == '__main__' :
    game = Game()
    
    # Printing the doc string
    print(game.initialize_game.__doc__)
    
    game.initialize_game()
    game.play_uno()
