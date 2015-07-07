# https://www.hackerrank.com/challenges/gem-stones

n = int(input())
chars = set([chr(x) for x in range(ord('a'), ord('z') + 1)])
for i in range(n):
    s = input()
    sChars = set()
    for char in s:
        sChars.add(char)
    chars &= sChars
print(len(chars))