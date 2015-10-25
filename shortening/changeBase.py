def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]

#s = "0x0a470c00025f424a"
#i = int(s)
i = 740573857905066570
base62Num = numberToBase(i, 62)

print base62Num
print ord('Z')-29
print ord('z')-87

s=""

for i in range(0, len(base62Num)):
	if base62Num[i] >= 10 and base62Num[i] <= 35:
		s += str(unichr(base62Num[i]+87))
	elif base62Num[i] >= 36 and base62Num[i] <= 61:
		s += str(unichr(base62Num[i]+29))
	else:
		s += str(base62Num[i])

print s
