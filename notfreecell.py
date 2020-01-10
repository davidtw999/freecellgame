# This assignment is written by Wei Tan with student ID 29102251.


# Importing string, time library, Card class from card file and Deck class from deck file
import string
import time
from card import Card
from deck import Deck


# Other layout variables for formatting purposes
tabs = '\t\t'
tab = '\t'
red = '\033[31m'
bold = '\033[1m'
black = '\033[30m'


# NotFreecell class is used for the user to play a freecell games.
class NotFreecell:

    # Class variables are defined, which includes number of cascades,
    # number of cells, number of foundations, a dictionary of cascade locations,
    # a dictionary of cell locations and a dictionary of foundation locations.
    num_of_cascs = 8
    num_of_cells = 4
    num_of_fouds = 4
    cascs_loca = {'C1': 0, 'C2': 1, 'C3': 2, 'C4': 3, 'C5': 4, 'C6': 5, 'C7': 6, 'C8': 7}
    cells_loca = {'E1': 0, 'E2': 1, 'E3': 2, 'E4': 3}
    fouds_loca = {'F1': 0, 'F2': 1, 'F3': 2, 'F4': 3}
    empty = "Empty"
    top = -1

    # Creating an instance for a NotFreecell by using Deck class,
    # the major instance variables are the lists of 8 cascades, 4 cells and 4 foundations,
    # others are user's entering command, a card location are stored after the drawing action,
    # a card location are stored after the placing action, and a card location are stored
    # after user select(drawing or placing) a card.
    def __init__(self):
        self.cascs = []
        self.cells = []
        self.fouds = []
        self.start_t = time.time()

        self.enter_command = ''
        self.draw_loca = ''
        self.place_loca = ''
        self.selec_card = ''

        self.set_empLists(self.cascs, self.num_of_cascs)
        self.set_empLists(self.cells, self.num_of_cells)
        self.set_empLists(self.fouds, self.num_of_fouds)

        # Generating random 52 cards without Jokers from Deck class
        # and move them storing into 8 cascades lists.
        theDeck = Deck(1,13,4)
        theDeck.shuffle_cards()
        self.set_cascs(theDeck)


    # Generating the cards of 8 cascades represented as a string.
    def __str__(self):
        cascs_string = ""

        for row in self.cascs:

            for item in row:
                # Using tab for making a better format for a representation of cascades
                cascs_string += str(item) + tab
                # Removing the last tab space of the string
                cascs_string.strip(tab)

            # Ending with switching line command after the last card in each cascade
            cascs_string += '\n'

        return cascs_string


    # Accounting a number of the cards in cascade
    def __len__(self):
        return len(self.cascs)


    # Printing the instructions of all the commands in game.
    def print_game_commands(self):
        print("Enter game commands below:")
        print("Display all the game commands" + tab + "--'HELP'")
        print("Quit the game   " + tabs + tabs + "--'QUIT'")
        print("Game played time" + tabs + tabs + "--'TIME'")
        print("Make a new game " + tabs + tabs + "--'NEWGAME'" )
        print("Cell locations for a move" + tabs + "--'E1', 'E2', 'E3', 'E4'")
        print("Foundation locations for a move" + tab + "--'F1', 'F2', 'F3', 'F4'")
        print("Cascade locations for a move" + tab + "--'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'")
        print('\n')


    # Printing out a line in a freecell game.
    def print_label_line(self):
        label_line = "|-------|-------|-------|-------|-------|-------|-------|-------|"
        print(label_line)


    # Printing the label names for all particular cells and foundations in a freecell game.
    def print_label_x1(self):
        label_xe = ''
        label_xf = ''

        i = 1;

        while( i <= 4):
            label_xe = label_xe  + '|' + bold  + 'E' + str(i) + black + tab
            label_xf = label_xf  + '|' + bold  + 'F' + str(i) + black + tab
            i += 1

        label_x1 = label_xe + label_xf +'|'
        print(label_x1)


    # Printing the actual last card in particular cell or foundation lists in a freecell game
    def print_label_x2(self):

        e_list = self.cells
        f_list = self.fouds

        label_xe = ''
        label_xf = ''

        i = 0;

        while( i <= 3):
            # Getting the suit from certain cell and foundation.
            last_char_e = str(self.peek_list(e_list[i]))[self.top:]
            last_char_f = str(self.peek_list(f_list[i]))[self.top:]
            # Getting the last card from certain cell and foundation.
            top_list_e = str(self.peek_list(e_list[i]))
            top_list_f = str(self.peek_list(f_list[i]))

            # Storing a card with a heart or diamond suit by showing in red colour,
            # a card with a spade or a club suit by showing in black colour.
            if (last_char_e == Card.heart or last_char_e == Card.diamond):
                label_xe = label_xe + '|' + red + bold + top_list_e + black + tab

            elif (last_char_e == Card.spade or last_char_e == Card.club):
                label_xe = label_xe + '|' + bold + top_list_e + black + tab

            else:
                label_xe = label_xe + '|' + top_list_e + tab

            if (last_char_f == Card.heart or last_char_f == Card.diamond):
                label_xf = label_xf + '|' + red + bold + top_list_f + black + tab

            elif (last_char_f == Card.spade or last_char_f == Card.club):
                label_xf = label_xf + '|' + bold + top_list_f + black + tab

            else:
                label_xf = label_xf + '|' + top_list_f + tab

            i += 1

        label_x2 = label_xe + label_xf + '|'
        print(label_x2)


    # Printing out the label names for all particular cascades in a freecell game
    def print_label_x3(self):
        label_x3 = ''

        i = 1;

        while( i <= 8):
            label_x3 = label_x3 + '|'  + bold + 'C' + str(i) + black + tab
            i += 1

        label_x3 = label_x3 + '|'
        print(label_x3)


    # Printing out the transiting cascade lists.
    def print_colms(self, the_cards):
        length_t = len(the_cards)
        label = ''

        i = 0
        j = 0

        while (i < length_t):

            while (j < 8):

                if (the_cards[i][j][self.top:] == Card.heart or the_cards[i][j][self.top:] == Card.diamond):
                    label = label + '|' + red + bold + str(the_cards[i][j]) +black + tab

                elif (the_cards[i][j][self.top:] == Card.spade or the_cards[i][j][self.top:] == Card.club):
                    label = label + '|' + bold + str(the_cards[i][j]) + black + tab

                else:
                    # print(label)
                    # print(str(the_cards[i][j]))
                    label = label + '|' + str(the_cards[i][j])
                    # print(label)
                j += 1

            label = label + '|' + '\n'
            j=0
            i += 1

        print(label)



    # Printing out the game layout of current status in a freecell game
    def print_layout(self):
        self.print_label_line()
        self.print_label_x1()
        self.print_label_x2()
        self.print_label_line()
        self.print_label_x3()

        # Transiting the order of cascades row representation into column representation.
        # Finding out the maximum length through all the cascade lists
        casc_in_column = []
        max_len_list = self.get_maxLenOfList()
        all_cascs_in_column = []

        i = 0
        j = 0

        # Creating list of lists according to the maximum length from above,
        while (i < max_len_list):

            # Transiting all eight items[i][j] into items[j][i]
            while (j < 8):
                # Ignoring the index error out of range when it happens
                # and storing the tab as a new element in a list
                try:
                    casc_in_column.append(str(self.cascs[j][i]))
                except IndexError:
                    casc_in_column.append(tab)
                j += 1

            self.get_lists(casc_in_column, all_cascs_in_column)
            casc_in_column = []

            j = 0
            i += 1

        self.print_colms(all_cascs_in_column)


    # Getting the maximum length of one list from all 8 cascades lists
    def get_maxLenOfList(self):
        max = 0
        length = len(self)

        i = 0

        while(i<length):
            t = len(self.cascs[i])

            if (max < t):
                max = t

            i+=1

        return max


    # The user win the game when all 52 cards placing to the foundations.
    def  win_game(self):
        len_f_list = len(self.fouds)
        count = 0

        i = 0

        while (i < len_f_list):
            count += len(self.fouds[i])
            i += 1

        if (count == 52):
            return True

        return False


    # Using for showing the time when it requires.
    def show_playing_time(self):
        end_time = time.time()
        elapsed = end_time - self.start_t
        print("Game played time: " + time.strftime('%H:%M:%S', time.gmtime(elapsed)))


    # Checking the enterred command whether only exists in main commands
    def quit_or_new(self):
        if self.enter_command == "QUIT":
            self.show_playing_time()
            print("Thanks for playing the game. See you next time. :)")
            quit()

        elif self.enter_command == "NEWGAME":
            self.__init__()
            print("GOOD LUCK FOR THE NEW GAME!")
            return True


    def assist_commands(self):
        if self.enter_command == "HELP":
            self.print_game_commands()
            return True

        if self.enter_command == "TIME":
            self.show_playing_time()
            return True


    # Returning error msg for a card is drawn from empty locations
    def get_draw_noCardMsg(self):
        noCardMsg = "No card in " + self.enter_command + " location, please DRAW again!"
        return noCardMsg


    # To see the last card of the list
    def peek_list(self, cef_list):

        if (self.is_empty(cef_list)):
            return self.empty

        else:
            return cef_list[self.top]


    # Generating a list of 8 cascade lists which include all 52 cards
    def set_cascs(self, the_deck):
        flag = 0

        i = 0
        j = 0

        while (i < self.num_of_cascs):

            # Set a flag used for storing 7 cards in first four cascade lists,
            # and 6 cards in last four cascade lists
            if (flag >= 4):
                j = 1

            while (j < 7):
                self.cascs[i].append(the_deck.draw_card())
                j += 1

            j = 0
            flag += 1
            i += 1


    # Generating a list of empty lists used for storing cards in cascades, cells and foundations.
    def set_empLists(self, item, num_of_lists):
        i = 0
        while (i < num_of_lists):
            item.append([])
            i += 1


    # Adding one card into the list of cards in cascades, or cells, or foundations
    def add_card(self, cef_list, the_card):
        return cef_list.append(the_card)


    # Drawing one card from the list of cards in cascades, or cells, or foundations
    def draw_card(self, cef_list):
        if (not(self.is_empty(cef_list))):
            return cef_list.pop()


    # Using for checking whether the list of cards is empty or not
    def is_empty(self, cef_list):
        return len(cef_list) == 0


    # Checking the entering command whether only exists in valid location
    # in cascades, cells and foundations for moving the card
    def check_location(self, the_locations):
        for item in the_locations:
            if (self.enter_command == item):
                return True
        return False


    # Drawing a card action from any location in cascades, cells or foundations after user's command.
    def draw_a_card_from(self):
        print("Which location do you want to DRAW a card from?")
        self.enter_command = input()

        # Interrupting the game when the user entering the main game command,
        # otherwise the user keep playing the game.
        if (self.quit_or_new() == True):
            return False

        # Drawing a card from cascade locations.
        if (self.check_location(self.cascs_loca)):

            if (not (self.is_empty(self.cascs[self.cascs_loca[self.enter_command]]))):
                self.draw_loca = self.enter_command
                self.selec_card = self.draw_card(self.cascs[self.cascs_loca[self.draw_loca]])
                return True

            else:
                print(self.get_draw_noCardMsg())
                return False

        # Drawing a card from cell locations.
        elif (self.check_location(self.cells_loca)):

            if (not (self.is_empty(self.cells[self.cells_loca[self.enter_command]]))):
                self.draw_loca = self.enter_command
                self.selec_card = self.draw_card(self.cells[self.cells_loca[self.draw_loca]])
                return True

            else:
                print(self.get_draw_noCardMsg())
                return False

        # Drawing a card from foundation locations.
        elif (self.check_location(self.fouds_loca)):

            if (not (self.is_empty(self.fouds[self.fouds_loca[self.enter_command]]))):
                self.draw_loca = self.enter_command
                self.selec_card = self.draw_card(self.fouds[self.fouds_loca[self.draw_loca]])
                return True

            else:
                print(self.get_draw_noCardMsg())
                return False

        if (self.assist_commands() == True):
            return False
        else:
            print("INVALID COMMAND, PLEASE ENTER AGAIN!")
            return False


    # Placing a card action to any location in cascades, cells or foundations after user's command.
    def place_a_card_to(self):

        # Showing the msg to user for placing a card with certain colour card.
        if (self.selec_card.colour == Card.red):
            print("Which location do you want to PLACE " + red + bold + str(self.selec_card) + \
                  black + " from " + self.draw_loca + " to?")

        elif (self.selec_card.colour == Card.black):
            print("Which location do you want to PLACE " + bold + str(self.selec_card) + \
                  black + " from " + self.draw_loca + " to?")

        self.enter_command = input()

        # Interrupting the game when the user entering the main game command,
        # otherwise the user keep playing the game.
        if (self.quit_or_new() == True):
            return True

        # Placing a card to cascade locations.
        if (self.check_location(self.cascs_loca)):
            self.place_loca = self.enter_command

            if(self.check_moveToCas(self.cascs[self.cascs_loca[self.place_loca]])):
                self.add_card(self.cascs[self.cascs_loca[self.place_loca]], self.selec_card)
                return True

            else:
                print("Can't move to " + self.place_loca + ", out of the rule!")
                return False

        # Placing a card to cell locations.
        elif (self.check_location(self.cells_loca)):
            self.place_loca = self.enter_command

            if (self.is_empty(self.cells[self.cells_loca[self.place_loca]])):
                self.add_card(self.cells[self.cells_loca[self.place_loca]], self.selec_card)
                return True

            else:
                print("Can't move to " + self.place_loca + ", out of the rule!")
                return False

        # Placing a card to foundation locations.
        elif (self.check_location(self.fouds_loca)):
            self.place_loca = self.enter_command

            if (self.check_moveToF(self.fouds[self.fouds_loca[self.place_loca]])):
                self.add_card(self.fouds[self.fouds_loca[self.place_loca]], self.selec_card)
                return True

            else:
                print("Can't move to " + self.place_loca + ", out of the rule!")
                return False

        if (self.assist_commands() == True):
            return False
        else:
            print("INVALID COMMAND, PLEASE ENTER AGAIN!")
            return False


    # Checking whether the move for placing card into cascades is valid or not
    def check_moveToCas(self, c_list):

        if (self.place_loca == self.draw_loca):
            return True

        if (self.is_empty(c_list)):
            return True

        if (self.place_loca != self.draw_loca):
            c_card = self.peek_list(c_list)

            if ( c_card.faceValue  == (self.selec_card.faceValue + 1)):

                if (c_card.colour == self.selec_card.flip_colour()):
                    return True

        return False


    # Checking whether the move for placing card into foundations is valid or not
    def check_moveToF(self, f_list):

        if (self.is_empty(f_list)):

            if (self.selec_card.faceValue == 1):
                return True

        else:
            f_card = self.peek_list(f_list)

            if ((f_card.faceValue + 1) == self.selec_card.faceValue ):

                if (f_card.suit == self.selec_card.suit):
                    return True

        return False


    # Generating the list of lists
    def get_lists(self, the_list, lists):
        lists.append(the_list)


# Genearating a freecell instance game for the uesr playing, there is two main actions, which includes
# draing a card and placing a card. The game ends though two actions including quit action
# and win the game action.
def main():
    freecell = NotFreecell()
    freecell.print_layout()
    freecell.print_game_commands()
    print("Game Starts, have fun! :)")

    while (freecell.enter_command != "QUIT"):

        while (not(freecell.draw_a_card_from())):
            freecell.print_layout()

        else:
            freecell.print_layout()

            while(not(freecell.place_a_card_to())):
                freecell.print_layout()

            else:
                freecell.print_layout()

        if (freecell.win_game()):
            freecell.show_playing_time()
            print("Congratulations!!!!!!! You are the legend!")
            quit()


if __name__ == "__main__":
    main()

