# https://www.hackerrank.com/challenges/pangrams
s = input()
exists = set()

for char in s:
    exists.add(char.lower())

for i in range(ord('a'), ord('z') + 1):
    if not chr(i) in exists:
        print("not pangram")
        break
else:
    print("pangram")
    