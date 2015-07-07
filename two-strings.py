# https://www.hackerrank.com/challenges/two-strings
cases = int(input())
offset = ord('a')
for caseNo in range(cases):
	a = input()
	b = input()
	sa = [False] * 26
	sb = [False] * 26
	for char in a:
		sa[ord(char) - offset] = True
	for char in b:
		sb[ord(char) - offset] = True
	for i in range(26):
		if sa[i] and sb[i]:
			print("YES")
			break
	else:
		print("NO")