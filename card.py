# This assignment is written by Wei Tan with student ID 29102251.


# Card class is used for generating a card with certain face value
# from 1 to 13 of the suits in spade, club, diamond, heart and Jokers.
class Card:

    # Class variables are shared by all instances,
    # and these are two colours(red and black),
    # four suits(spade, diamond, heart, club),
    # a list which includes four suits,
    # a dictionary of matching the face value from 1 to 14 to face name,
    # a dictionary of matching the suits to the colours,
    # a dictionary of matching the colours to the opposite colours,
    # a dictionary of matching the pictures to the suits.
    # Using character 'X' for representing the colour and the suit of Joker card
    # because it has no colour and suit
    joker = 'X'
    black = 'B'
    red = 'R'
    spade = 'S'
    diamond = 'D'
    heart = 'H'
    club = 'C'
    suits = [spade, diamond, heart, club]
    faceValueToChar = {1:'A', 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',
                       11:'J', 12:'Q', 13:'K', 14:'JK'}
    colours = {spade: black, diamond: red, heart : red, club: black, joker: joker}
    opp_colours = {black: red, red: black, joker: joker}
    suit_pics = {spade: '♠', diamond: '♦', heart: '♥', club: '♣', joker: joker}


    # Creating an instance for a card by entering a face value and a suit.
    # Instances variables are unique to each instance,
    # and these are the face value, the suit, the colour
    # and the picture represented of the suit of a card.
    def __init__(self, the_faceValue, the_suit):
        self.faceValue = the_faceValue
        self.suit = the_suit
        self.colour = self.colours[the_suit]
        self.suit_pic = self.suit_pics[the_suit]


    # Generating a card format represented as a string of "facevalue-suit:colour"(e.g., "1-S:B").
    def __str__(self):
        return str(self.faceValueToChar[self.faceValue]) + ':' + str(self.suit_pic) + ':' + str(self.suit)


    # Four accessors are get the face value, the suit, the colour, the opposite colour of the card.
    def get_face(self):
        return self.faceValue


    def get_suit(self):
        return self.suit


    def get_colour(self):
        return self.colour


    def flip_colour(self):
        opp_colour = self.opp_colours[self.colour]
        return opp_colour


# Using for testing all the methods without any purposes in this assignment 2
def main():

    testCard = Card(13,'S')
    print(testCard.suits)
    print(testCard)
    print(type(testCard))
    print(testCard.get_face())
    print(testCard.get_suit())
    print(testCard.get_colour())
    print(testCard.flip_colour())


if __name__ == "__main__":
    main()



