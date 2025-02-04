
import random

values=suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():


  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value =values[rank]
  def __str__(self):
    return self.rank + " of " + self.suit



class Deck() :
  def __init__(self):
    self.all_cards=[]
    for suit in suits:
      for rank in ranks:
        created_card=(Card(suit,rank))
        self.all_cards.append(created_card)
  def shuffle(self):
    random.shuffle(self.all_cards)
  def deal_one(self):
    return self.all_cards.pop()

class Player ():
  def __init__(self,name):
    self.name=name
    self.all_cards=[]
  def remove_cards(self):
    return self.all_cards.pop(0)

  def add_cards(self,new_cards):
    if type(new_cards)==type([]):
      self.all_cards.extend(new_cards)
    else:
      self.all_cards.append(new_cards)
  def __str__(self):
    return f'Player {self.name} has {len(self.all_cards)} cards.'

from types import new_class
player1 = Player("one")
player2 = Player("two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
  player1.add_cards(new_deck.deal_one())
  player2.add_cards(new_deck.deal_one())

game_on=True

round_on=0


while game_on==True:
  round_on+=1
  print(f'Round {round_on}')

  if len(player1.all_cards)==0:
    print('Player One, out of cards! Game Over')
    game_on=False
    break
  if len(player2.all_cards)==0:
    print('Player Two, out of cards! Game Over')
    game_on=False
    break

  player_one_card=[]
  player_two_card=[]

  player_one_card.append(player1.remove_cards())
  player_two_card.append(player2.remove_cards())

at_war=True

while at_war==True:
  if player_one_card[-1].value>player_two_card[-1].value:
    player1.add_cards(player_one_card)
    player1.add_cards(player_two_card)
    at_war=False

  elif player_one_card[-1].value<player_two_card[-1].value:
    player2.add_cards(player_one_card)
    player2.add_cards(player_two_card)
    at_war=False

  else :
    print("WAR!")

    if len(player_one_card.all_cards<5):
      print("Player One unable to declare war")
      print("Player Two Wins!")
      game_on=False
      break

    elif len(player_two_card.all_cards<5):
      print("Player two unable to declare war")
      print("Player One Wins!")
      game_on=False
      break

    else:
      for num in range (5):
        player_one_card.append(player_one_card.remove_cards())
        player_two_card.append(player_two_card.remove_cards())