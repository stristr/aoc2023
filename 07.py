# 378/323
# 14:47/21:57
from sys import stdin
from functools import cmp_to_key

def parse(line):
    cards, bid = line.split()
    return {
        c: cards.count(c)
        for c in cards
    }, cards, int(bid)

lines = stdin.read().strip().split('\n')
hands = [parse(line) for line in lines]

def strength(deck):
    if len(deck.keys()) == 1: # 5 of a kind
        return 6
    if len(deck.keys()) == 2 and 4 in deck.values(): # 4 of a kind
        return 5
    if len(deck.keys()) == 2 and 3 in deck.values(): # full house
        return 4
    if len(deck.keys()) == 3 and 3 in deck.values(): # 3 of a kind
        return 3
    if len(deck.keys()) == 3 and 2 in deck.values(): # 2 pair
        return 2
    if len(deck.keys()) == 4 and 2 in deck.values(): # pair
        return 1
    return 0

def jokerSubs(deck):
    return [deck] if 'J' not in deck else [
        {
            **{c: v if c != J else v + deck['J'] for c, v in deck.items() if c != 'J'},
            **({J: deck['J']} if J not in deck else {})
        } for J in '23456789TQKA'
    ]

def jokerStrength(deck):
    return max(strength(sub) for sub in jokerSubs(deck))

def compare(left, right, strength, cardValue):
    lCounts, lCards, _ = left
    rCounts, rCards, _ = right
    lStrength, rStrength = strength(lCounts), strength(rCounts)
    if lStrength != rStrength:
        return lStrength - rStrength
    return next((
        lValue - rValue
        for lValue, rValue in zip(
            map(cardValue, lCards),
            map(cardValue, rCards)
        )
        if lValue != rValue
    ), 0)

hands.sort(key=cmp_to_key(lambda l, r: compare(
    l, r, strength=strength, cardValue=lambda c: '23456789TJQKA'.index(c))))
print('a', sum((d + 1) * bid for d, (_, _, bid) in enumerate(hands)))

hands.sort(key=cmp_to_key(lambda l, r: compare(
    l, r, strength=jokerStrength, cardValue=lambda c: 'J23456789TQKA'.index(c))))
print('b', sum((d + 1) * bid for d, (_, _, bid) in enumerate(hands)))
