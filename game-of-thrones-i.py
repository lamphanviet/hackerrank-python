# https://www.hackerrank.com/challenges/game-of-thrones
s = input()
cnt = {}
for char in s:
    if char in cnt:
        cnt[char] += 1
    else:
        cnt[char] = 1
odd = False
for key in cnt:
    if cnt[key] % 2 == 1:
        if odd:
            print("NO")
            break
        odd = True
else:
    print("YES")