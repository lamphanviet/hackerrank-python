# https://www.hackerrank.com/challenges/bigger-is-greater
import itertools

cases = int(input())
for caseNo in range(cases):
	s = input()
	processed = False
	for perms in itertools.permutations(s):
		if processed:
			ns = ''.join(perms)
			print(ns)
			if ns != s and s < ns:
				print(ns)
			else:
				print("no answer")
			break
		processed = True