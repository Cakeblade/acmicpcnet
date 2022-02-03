import sys
import collections

n = int(sys.stdin.readline())
deck = collections.deque([i for i in range(1, n + 1)])

while len(deck) > 1:
    deck.popleft()
    deck.rotate(-1)
    
print(deck[0])