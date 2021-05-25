import random
playing = True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
1

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.hasAce = 0

    def add_card(self, card):
        self.hand.append(card)
        self.score += values[card.rank]
        if card.rank == 'A':
            self.hasAce = 1

    def adjust_ace(self):
        while self.score > 21 and self.hasAce:
            self.score -= 10
            self.hasAce = 0


class Dealer(Hand):
    def __init__(self):
        Hand.__init__(self)


class Player(Hand):
    def __init__(self, wallet = 5000):
        Hand.__init__(self)
        self.wallet = wallet


def play_again():
    while True:
        try:
            answer = input("Do you want to start a new match: Y/N ")
        except:
            print("Please enter a valid answer")
        else:
            if answer[0].lower() == 'y':
                player1.hand = []
                computer.hand = []
                player1.score = 0
                computer.score = 0
                return True
            else:
                return False


def take_bet():
    while True:
        try:
            bet = int(input("How much do you want to bet:"))
        except:
            print("Please enter a valid amount")
        else:
            if bet > player1.wallet:
                print("Sorry your bet can't exceed")
            else:
                return bet


def show_some():
    print("\nDealer's Hand: <card hidden>")
    print(computer.hand[1])
    print("\nPlayer's Hand:" , *player1.hand, sep='\n')



def show_all():
    print("\nDealer's Hand:", *computer.hand, sep='\n')
    print("Dealer's Hand =",computer.score)
    print("\nPlayer's Hand:", *player1.hand, sep='\n')
    print("Player's Hand =", player1.score)


def hit_stand(deck):
    global playing
    while True:
        answer = input("Do you want to hit or stand: ").lower()
        if answer[0].lower() == "h":
            player1.add_card(deck.deal())
            player1.adjust_ace()
        elif answer[0].lower() == "s":
            print("Dealer's turn")
            playing = False
        else:
            print("Please enter a valid answer")
            continue
        break


def player_bust(bet):
    print("Dealer win. You busted.")
    player1.wallet -= bet


def dealer_bust(bet):
    print("You win. Dealer busted.")
    player1.wallet += bet


def player_win(bet):
    print("You win.")
    player1.wallet += bet


def dealer_win(bet):
    print("Dealer win.")
    player1.wallet -= bet


if __name__ == "__main__":
    print("Welcome to BlackJack")
    print("Let's play")
    player1 = Player()
    computer = Dealer()
    while True:
        deck = Deck()
        deck.shuffle()
        bet = take_bet()
        for i in range(0, 2):
            player1.add_card(deck.deal())
            computer.add_card(deck.deal())
        show_some()
        while playing:
            hit_stand(deck)
            show_some()
            if(player1.score > 21):
                player_bust(bet)
                break
        if player1.score <= 21:
            while computer.score < 17:
                computer.add_card(deck.deal())
                computer.adjust_ace()
            show_all()
            if computer.score > 21:
                dealer_bust(bet)
            elif computer.score > player1.score:
                dealer_win(bet)
            elif player1.score > computer.score:
                player_win(bet)
            else:
                print("Tie")
        if not play_again():
            print("Thank for playing")
            break

