# Freecellgame

FreeCell is a solitaire card game played using the standard 52-card deck.
Using python to write card.py, deck.py and notfreecell.py three files which are implemented for
playing a freecell game. Card, Deck and NotFreecell are three classes that was written in
those three files. Card class is used for generating a Card object with certain face value and
suit. Deck class is used for generating a Deck object, which including a list of a number of
Card objects. NotFreecell class is used for generating a freecell game with 52 Card objects
moving around in 12 slots of cascades, cells and foundations. All the game rules are also
written in notfreecell.py file according to a freecell game in website www.123freecell.com.

## In card.py file:

#### a) Card class variables including:
- joker is used for representing no colour and suit for ‘Joker’ Card object,
- black is used for representing black colour,
- red is used for representing red colour,
- spade is used for representing the suit of spade,
- diamond is used for representing the suit of diamond,
- heart is used for representing the suit of heart,
- club is used for representing the suit of club,
- suits is used for representing a list of four suits above,
- faceValueToChar is used for representing a dictionary of matching the face
name with the face value,
- colours is used for representing a dictionary of matching the colour with the
suit,
- opp_colours is used for representing a dictionary of matching the opposite
with colour the colour,
- suit_pics is used for representing a dictionary of matching the layout character
with the suit.
#### b) Card class functions including:
- def __init__(self, the_faceValue, the_suit):
Constructor is used for creating an instance of Card object by assigning a face
value and a suit.
  - i. Instance variables including:
    - self.faceValue is used for storing a face value for a Card object,
    - self.suit is used for storing a suit for a Card object,
    - self.colour is used for storing a colour for a Card object,
    - self.suit_pic is used for storing a layout character for a Card object.
- def __str__(self):
Overloading function is used for the layout representation of a Card object
(e.g., Card (13, ‘S’) prints out K:♠:S).
- def get_face(self):
An accessor is used for getting a face value of a Card object.
- def get_suit(self):
An accessor is used for getting a suit of a Card object.
- def get_colour(self):
An accessor is used for getting a colour of a Card object.
- def flip_colour(self):
An accessor is used for getting an opposite colour of a Card object.
#### c) Other function and statement:
- def main():
Main function is not used for this assignment requirement, however I did test
all the functions that I wrote in a Card object.
- if __name__ == "__main__":
main()
Only executing when the user wants to run the module as a program.

## In deck.py file:
#### a) Card class functions including:
- def __init__(self, the_value_start, the_value_end, the_number_of_suits):
Constructor is used for creating an instance of Deck object with many Card
objects by assigning the start and end value with the suits of Card object.
  - i. Initialising all the instance variables including:
    - self.cards is used for storing a list of Card objects
    - self.value_start is used for storing starting face value of Card object,
    - self.value_end is used for storing ending face value of Card object,
    - self.number_of_suits is used for storing the number of suits existing of
Card object.
  - ii. Main pseudo code:<br>
    - if (self.check_valid_inputs() == True):<br>
      - To pass to next if statement when the inputs are valid.<br>
      - if (self.number_of_suits == 5):<br>
        - To update the local variable the_number_of_suits equal to 4 for use in the next statement.<br>
        - Then generating a list of random suits by using the number of suits.<br>
        - To generate a list of Card objects in Deck according to the starting face value, the ending face value, the number of suits and a list of random suits. <br>
      - if (self.check_with_joker() == True):<br>
        - To add two Joker Cards into a list of cards in Deck object.<br>
      - else:<br>
        - To show the error messages for the user.<br>
  - iii. Main logic structure:
  ![logic structure deck](https://github.com/davidtw999/freecellgame/blob/master/logic1.png)

- def __len__(self):
Overloading function is used for accounting how many cards in the deck.
- def __str__(self):
Overloading function is used for the layout representation of a Deck object list
with Card object.
(e.g., Deck(1, 1, 4) prints out random order of A:♦:D A:♥:H A:♣:C A:♠:S).
- def is_empty(self):
An accessor is used for getting True when the length of the list is equal to 0,
otherwise return False.
- def check_with_joker(self):
An accessor is used for getting True when the number of suits is 5, otherwise
return False.
- def check_valid_inputs(self):
An accessor is used for getting True when the start and end value is between 1
to 13, the number of suits is between 1 to 5, the end value must be bigger or
equal to the start value, and special case for empty deck with the start value 0,
the end value 0, and the suits 0, otherwise return False.
- def get_rand_suits(self, the_num_of_suits):
A mutator is used for generating a list of random suits from 1 to 4 number of
suits.
- def shuffle_cards(self):
A mutator is used for shuffling a list of Card objects in a random order.
- def add_card(self, the_card):
A mutator is used for adding one Card object into a card list of Deck object.
- def draw_card(self):
A mutator is used for removing one Card object from a card list of Deck
object, and also it returns this Card object.
- def set_cards(self, the_value_start, the_value_end, the_number_of_suits,
the_suits):
An mutator is used for generating a list of cards for Deck through by assigning
the starting value, the ending value, the number of suits and a list of suits. The
card value must be in range of 1 and 13, with the suits in range of spade,
diamond, heart and club suits.
(e.g., set_cards(1, 1, 4, [‘S’, ‘D’, ‘H’, ‘C’] update a list of cards in Deck object
with random order of [A:♥:H A:♦:D A:♣:C A:♠:S] ).
- def main():
main() function is not used for this assignment requirement, however I did test
all the functions that I wrote in a Card object.
- if __name__ == "__main__":
__name__ == “__main__” only executing when the user wants to run the
module as a program.
#### b) Other function and statement:
- def main():
Main function is not used for this assignment requirement, however I did test
all the functions that I wrote in a Card object.
- if __name__ == "__main__":
main()
Only executing when the user wants to run the module as a program.

## In notfreecell.py file:
#### a) Card class variables including:
- num_of_cascs is used for representing 8 cascades
- num_of_cells is used for representing 4 cells
- num_of_fouds is used for representing 4 foundations
- cascs_loca is used for representing a dictionary of matching cascade names to
the index of cascade lists
- cells_loca is used for representing a dictionary of matching cell names to the
index of cell lists
- fouds_loca is used for representing a dictionary of matching foundation names
to the index of foundation lists
- empty is used for representing string “Empty” to show the empty locations
- top = -1 is used for getting the last element from the list.
#### b) NotFreecell class functions including:
- def __init__(self):
Constructor is used for creating an instance of NotFreecell object with 52 Card
objects generated from Deck object.
  - i. Initialising all the instance variables including:
    - self.cascs is used for storing a cascade list,
    - self.cells is used for storing a cell list,
    - self.fouds is used for storing a foundation list,
    - self.start_t is used for storing a starting time,
    - self.enter_command is used for storing the user entering game
command,
    - self.draw_loca is used for storing a draw action from a card stored
location，
    - self.place_loca is used for storing a place action to a card stored
location，
    - self.selec_card is used for storing a draw or place action for a card
stored location，
    - self.set_empLists(self.cascs, self.num_of_cascs) is used for updating a
cascade list storing 8 empty lists，
    - self.set_empLists(self.cells, self.num_of_cells) is used for updating a
cell list storing 4 empty lists，
    - self.set_empLists(self.fouds, self.num_of_fouds) is used for updating a
foundation list storing 4 empty lists.
- def __str__(self):
Overloading function is used for storing all the cards in 8 cascade lists as
string representation.
- def __len__(self):
Overloading function is used for accounting a number of cards in cascades.
- def print_game_commands(self):
A function is used for showing all the gaming commands for the user to play.
- def print_label_line(self):
A function is used for printing a line for the game layout.
- def print_label_x1(self):
A function is used for printing 4 cell and 4 foundation location names for the
game layout.
- def print_label_x2(self):
A function is used for printing a last Card object stored in each cell and
foundation list.
- def print_label_x3(self):
A function is used for printing 8 cascade location names for the game layout.
- def print_colms(self, the_cards):
A function is used for printing all the cards in cascade list by transited order.
- def print_layout(self):
A function is used for printing entire game layout including the functions
above.
- def get_maxLenOfList(self):
A function is used for getting a maximum length of list through by all the lists.
- def win_game(self):
A function is used for checking the winning condition for the game. The user
wins the game when all 52 cards placing to the foundation locations.
- def show_playing_time(self):
A function is used for showing the game played time when the user’s input is
“TIME”
- def quit_or_new(self):
A function is used for checking the game maybe renew or quit.
- def assist_commands(self):
A function is used for showing some game information when the user
requires.
- def get_draw_noCardMsg(self):
A function is used for returning an error message for a card drawn from empty
locations.
- def peek_list(self, cef_list):
A function is used for showing the last card of the list.
- def set_cascs(self, the_deck):
A function is used for initialising all the 52 cards into four 7 cards list and four
6 cards list.
- def set_empLists(self, item, num_of_lists):
A function is used for creating a list of empty lists used for storing cards in
cascades, cells and foundations.
- def add_card(self, cef_list, the_card):
A function is used for adding one card into a list of cards in cascades, or cells,
or foundations.
- def draw_card(self, cef_list):
A function is used for drawing one card from a list of cards in cascades, or
cells, or foundations.
- def is_empty(self, cef_list):
A function is used for checking whether the list of cards is empty or not.
- def check_location(self, the_locations):
A function is used for checking whether the user’s input is valid, which only
exists in valid location of cascades, or cells, or foundations.
- def draw_a_card_from(self):
A function is used for drawing a card action from any location in cascades, or
cells or foundations after user’s input.
  - i. Main logic structure:
![draw_a_card_from](https://github.com/davidtw999/freecellgame/blob/master/logic2.png)
- def place_a_card_to(self):
A function is used for placing a card action to any location in cascades, or
cells or foundations after user’s input.
  - i. Main logic structure:
![place_a_card_to](https://github.com/davidtw999/freecellgame/blob/master/logic3.png)
- def check_moveToCas(self, c_list):
A function is used for checking whether the game move for placing a card into
cascades is valid or not.
- def check_moveToF(self, f_list):
A function is used for checking whether the game move for placing a card into
foundations is valid or not.
- def get_lists(self, the_list, lists):
A function is used for generating the list of lists.
#### c) Other function and statements:
- def main():
  - i. Main pseudo code:
    - While (QUIT a game == False)
      - do
      - While (Not(Finish “Draw a card” process))
      - Else:
        - do
        - While (Not(Finish “Place a card” process)
        - do
      - If (Win a game == True)
        - quit game
  - ii. Main logic structure:
![main to play](https://github.com/davidtw999/freecellgame/blob/master/logic4.png)
## Gameplay instruction
#### Running environment:
Python 3.6
#### Run game:
python notfreecell.py
#### Game commands:
There are 3 types of gaming commands as below:<br>
'HELP' and 'TIME' are the assistant type commands for the user wants to know the game
playing time or all the gaming commands.<br>
'QUIT' and 'NEWGAME' are the main type commands for the user wants to quit a game or
renew a game.<br>
'E1', 'E2', 'E3', 'E4','F1', 'F2', 'F3', 'F4', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8' are game
playing commands for moving a card into different locations.

#### Game rules:
The rules are much similar to the freecell game online. The game starts with 52 cards placing
in 8 different cascade locations, which includes 7 cards in C1 to C4 and 6 cards in C5 to C8,
and no card is in all the cell and foundation locations. There are two actions for playing this
game, which includes “Draw a card” and “Place a card”.<br>
Firstly, the player can only draw one card each time from any locations. In cascade locations,
the player can only draw one bottom card in each deck. In cell and foundation locations, the
player can only draw one card shown in the location. This action ends up when the player
takes a card in his/her hand.<br>
Secondly, the player can only place the card from where he/she takes from “Draw a card”
action to any valid locations. There four conditions are allowed in this action. Frist, the card
can be placed back to the locations where the card is drawn from. Second, the card can be
placed to any empty cell locations. Third, the card can be placed to foundation locations in
the order from ‘A’ to ‘K’ with the same suit. Fourth, the card can be placed to other cascade
locations, when the bottom card value and colour in specific cascade location matches the
card value increased by one and opposite colour where the player has in his/her hand.<br>
After all the cards are placed in all the foundation locations, the player wins the game.
