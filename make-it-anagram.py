# https://www.hackerrank.com/challenges/make-it-anagram
a = input()
b = input()
cnt = [0] * 26
offset = ord('a')
for char in a:
	cnt[ord(char) - offset] += 1
for char in b:
	cnt[ord(char) - offset] -= 1
total = 0
for value in cnt:
	total += abs(value)
print(total)