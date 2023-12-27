# War Game

The War Game is a simple card game implemented in Python where two players compete in rounds to win each other's cards.

## How to Play

1. Run the game by executing the `war_game.py` file.

    ```bash
    python war_game.py
    ```

2. Enter the names of the players when prompted.

3. The game will shuffle a standard deck of cards and distribute them equally to each player.

4. Each player takes turns making a move by entering 'm'. A card is randomly drawn from their deck.

5. The drawn cards are compared, and the player with the higher card wins the round, adding both cards to their deck.

6. In case of a tie, a "War" is declared. The players draw three cards face-down and reveal a fourth card. The player with the higher fourth card wins all the cards in that round.

7. The game continues until one player runs out of cards.

## Commands

- `m`: Make a move (draw a card).
- `play again`: Restart the game.
- `stop`: End the game.

## Example

Your name: Player1
Your name: Player2
Player1: has 18 cards
Player2: has 18 cards

Round 1
Enter 'm' to make a move, 'play again' to restart the game, or 'stop' to end the game: m
Player1 card: 8
Player2 card: 4
Player1 won the round!

...


Game over!

