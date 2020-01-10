# This assignment is written by Wei Tan with student ID 29102251.


# Importing random library and Card class from card file.
import random
from card import Card

# Deck class is used for generating a deck with a number of cards in one or more suits,
# which are determined by subtracting the maximum value by the minimum value given by user.
class Deck:

    # Creating an instance for a deck, which includes the instance variables of self.cards,
    # self.value_start, self.value_end and self.number_of_suits. Also the_value_start and
    # the_value_end, the_number_of_suits are the local variables.
    def __init__(self, the_value_start, the_value_end, the_number_of_suits):
        self.cards = []
        self.value_start = the_value_start
        self.value_end = the_value_end
        self.number_of_suits = the_number_of_suits


        # Defining the valid inputs for generating the cards in deck. The card value
        # starts with 1 to end the value with 13 within 1 to 4 suits (e.g., deck(1,13,4) for 52 cards).
        # There is a special case for adding 2 Joker cards in the deck by using
        # the number of suits 5 (e.g., deck(1,13,5) for 54 cards).
        if (self.check_valid_inputs() == True):

            # Generating a card list by using random function of four suits in Card class first,
            # and then adding two Joker cards to the card list when the number of suits is five.
            if (self.number_of_suits == 5):
                the_number_of_suits = the_number_of_suits - 1

            rand_suits = self.get_rand_suits(the_number_of_suits)
            self.set_cards(the_value_start, the_value_end, the_number_of_suits, rand_suits)

            # Adding Jokers when it needs
            if (self.check_with_joker() == True):
                self.cards.append(Card(14, Card.joker))
                self.cards.append(Card(14, Card.joker))

        # Printing out error msg.
        else:
            print("Invalid inputs, start and end values in between 1 and 13, number of suits in 1 to 5.")
            print("e.g.,\tdeck(0,0,0) for 0 card, deck(1,1,1) for 1 card.")
            print("\t\tdeck(1,13,4) for 52 cards with no Jokers, deck(1,13,5) for 54 cards with Jokers.")

    # Accounting a number of the cards in a deck
    def __len__(self):
        return len(self.cards)

    # Generating a deck format represented as a string of all Card objects (e.g.,"A-D:R   2-D:R" for 2 cards).
    def __str__(self):
        cards_string = ""

        for item in self.cards:
            # Using tab for making a better format for a representation of deck.
            cards_string += str(item) + '\t'
        # Removing the last tab space of the string.
        cards_string.strip('\t')

        return cards_string

    # Accessors
    # Using for checking whether the list of cards is empty or not.
    def is_empty(self):
        return len(self) == 0


    # Checking whether need to generate Joker cards or not for condition below.
    def check_with_joker(self):

        if (self.number_of_suits == 5):
            return True

        return False


    # Checking whether the inputs of start_value, end_value and number of suits are valid.
    def check_valid_inputs(self):

        if (self.number_of_suits == 0 and self.value_start == 0 and self.value_end == 0):
            return True

        if (self.value_start > self.value_end):
            return False

        if (self.value_start < 1 or self.value_start > 13):
            return False

        if (self.value_end < 1 or self.value_end > 13):
            return False

        if (self.number_of_suits < 1 or self.number_of_suits > 5):
            return False

        return True

    # Mutators
    # Generating a list of suits through by random function.
    def get_rand_suits(self, the_num_of_suits):
        return random.sample(Card.suits, the_num_of_suits)

    # Shuffling all the cards in the deck.
    def shuffle_cards(self):
        random.shuffle(self.cards)

    # Adding one card into the list of cards in the deck.
    def add_card(self, the_card):
        self.cards.append(the_card)

    # Drawing one card from the list of cards in the deck.
    def draw_card(self):

        if (self.is_empty()):
            return None

        else:
            return self.cards.pop()

    # Generating a list of cards from the minimum value to the maximum value in certain suits.
    def set_cards(self, the_value_start, the_value_end, the_number_of_suits, the_suits):
        the_cards = []

        i = 0
        j = the_value_start

        # Two while loop for generating the cards according to those variables.
        while (i < the_number_of_suits):

            while (j <= the_value_end):
                the_cards.append(Card(j, the_suits[i]))
                j += 1
            j = the_value_start
            i += 1

        self.cards = the_cards



# Using for testing all the methods without any purposes in this assignment 2
def main():
    testDeck = Deck(1,13,4)
    print(testDeck)


if __name__ == "__main__":
    main()
