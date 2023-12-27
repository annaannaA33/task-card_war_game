import random
import sys

class Player:
    def __init__(self, name, half_of_deck):
        self._name = name
        self._half_of_deck = half_of_deck

    def move(self):
        
        players_move = input("Enter 'm' to make a move, 'play again' to restart the game, or 'stop' to end the game: ")
        if players_move == 'm':
            the_card = random.choice(self._half_of_deck)
            self._half_of_deck.remove(the_card)
            return the_card
        if players_move == 'play again':
            game.start_game()
        if players_move == 'stop':
            sys.exit("Good Bye")
        
        
    def print_deck(self):
        print(f"{self._name}'s deck: {self._half_of_deck}")    

class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.current_round = 1

    def start_game(self):
        name_player1 = input("Your name: ")
        name_player2 = input("Your name: ")

        deck = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(deck)

        half_of_deck = len(deck) // 2
        half_player1 = deck[:half_of_deck]
        half_player2 = deck[half_of_deck:]

        self.player1 = Player(name_player1, half_player1)
        self.player2 = Player(name_player2, half_player2)

        print(f"{self.player1._name}: {len(self.player1._half_of_deck)} card")
        print(f"{self.player2._name}: {len(self.player2._half_of_deck)} card")

    def make_round(self):
        print(f"\nRound {self.current_round}")
        self.current_round += 1

        card_player1 = self.player1.move()
        card_player2 = self.player2.move()

        print(f"{self.player1._name} card: {card_player1}")
        print(f"{self.player2._name} card: {card_player2}")

        if card_player1 == card_player2:
            print("War!!!")
            self.deal_war()
        elif card_player1 > card_player2:
            self.player1._half_of_deck.extend([card_player1, card_player2])  
            print(f"{self.player1._name} won the round!")
        else:
            self.player2._half_of_deck.extend([card_player1, card_player2])
            print(f"{self.player2._name} won the round!")

    def deal_war(self):
        pass

    def check_the_winner(self):
        return not self.player1._half_of_deck or not self.player2._half_of_deck

if __name__ == "__main__":
    game = Game()
    game.start_game()

    while not game.check_the_winner():
        game.make_round()
        game.player1.print_deck()
        game.player2.print_deck()

    print("Game over!") 