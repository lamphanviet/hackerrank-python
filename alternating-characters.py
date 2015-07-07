# https://www.hackerrank.com/challenges/alternating-characters

cases = int(input())
for caseNo in range(cases):
    s = input()
    total = 0
    prev = -1
    for char in s:
        if char == prev:
            total += 1
        prev = char
    print(total)
