#https://www.hackerrank.com/challenges/anagram

cases = int(input())
offset = ord('a')
for caseNo in range(cases):
	s = input()
	n = len(s)
	if n % 2 == 1:
		print("-1")
	else:
		cnt = [0] * 26
		for i in range(n // 2):
			cnt[ord(s[i]) - offset] += 1
		for i in range(n // 2, n):
			cnt[ord(s[i]) - offset] -= 1
		total = 0
		for val in cnt:
			total += abs(val)
		print(total // 2)
