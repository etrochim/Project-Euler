#!/usr/bin/env python

from collections import defaultdict

valueTable = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14 }

class Card:
  def __init__(self, cardString):
    self.value = valueTable[cardString[0]]
    self.suit = cardString[1]

  def __str__(self):
    return "%d%s" % (self.value, self.suit)
  

class Hand:
  def __str__(self):
    return ' '.join([str(x) for x in self.cards])

  def __init__(self, handArray):
    self.cards = []
    for card in handArray:
      self.cards.append(Card(card))
    self.cards = sorted(self.cards, cmp=lambda c1,c2: cmp(c1.value, c2.value))
    
  def flush(self):
    if all(x.suit == self.cards[0].suit for x in self.cards[1:]):
      return self.cards[-1].value
    else:
      return 0

  def royalFlush(self):
    return [10, 11, 12, 13, 14] == [x.value for x in self.cards] and self.flush()

  def straight(self):
    if [x.value for x in self.cards] == range(self.cards[0].value, self.cards[0].value + 5):
      return self.cards[-1].value
    else:
      return 0

  def straightFlush(self):
    if(self.straight() and self.flush()):
      return self.cards[-1].value
    else:
      return 0

  def highCard(self, off = -1):
    return self.cards[off].value

  def fullHouse(self):
    val = self.xOfAKind(3)
    if val and self.xOfAKind(2):
      return val

  def twoPair(self):
    val = defaultdict(int)
    for card in self.cards:
      val[card.value] = val[card.value] + 1
    l = sorted([y for y in val.keys() if val[y] == 2])
    if len(l) == 2:
      return l.pop()
    else:
      return 0

  def xOfAKind(self, x):
    val = defaultdict(int)
    for card in self.cards:
      val[card.value] = val[card.value] + 1
    l = sorted([y for y in val.keys() if val[y] == x])
    if len(l):
      return l.pop()
    else:
      return 0

  def compare(self, hand):
    val = cmp(self.royalFlush(), hand.royalFlush())
    if val: return val

    val = cmp(self.straightFlush(), hand.straightFlush())
    if val: return val

    val = cmp(self.xOfAKind(4), hand.xOfAKind(4))
    if val: return val

    val = cmp(self.fullHouse(), hand.fullHouse())
    if val: return val

    val = cmp(self.flush(), hand.flush())
    if val: return val

    val = cmp(self.straight(), hand.straight())
    if val: return val

    val = cmp(self.xOfAKind(3), hand.xOfAKind(3))
    if val: return val

    val = cmp(self.twoPair(), hand.twoPair())
    if val: return val

    val = cmp(self.xOfAKind(2), hand.xOfAKind(2))
    if val: return val

    for x in range(1,6):
      val = cmp(self.highCard(-x), hand.highCard(-x))
      if val: return val

    raise Exception('Failed to compare')

f = open('problem54.txt', 'r')
won = 0
for line in f:
  line = line.rstrip()
  cards = line.split();
  p1 = Hand(cards[0:5])
  p2 = Hand(cards[5:10])
  if p1.compare(p2) > 0:
    won = won + 1

print "Player 1 won %s games" % won
