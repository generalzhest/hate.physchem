s = input()
n = s.count('h')
s = s.replace('h', 'H', n - 1)
s = s.replace('H', 'h', 1)
print(s)