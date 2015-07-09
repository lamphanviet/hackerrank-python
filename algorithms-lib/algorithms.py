def next_permutation(s):
	return compute_permutation(s, lambda x, y: x <= y)

def prev_permutation(s):
	return compute_permutation(s, lambda x, y: x >= y)

def compute_permutation(s, comparator):
	if type(s) != list:
		raise Exception("permutation's parameter must be a list")
	n = len(s)
	i = n - 1
	while i > 0 and comparator(s[i], s[i - 1]):
		i -= 1
	if i <= 0:
		return False
	j = n - 1
	while comparator(s[j], s[i - 1]):
		j -= 1
	s[i - 1], s[j] = s[j], s[i - 1]

	s[i : ]  = s[n - 1: i - 1 : -1]
	return True