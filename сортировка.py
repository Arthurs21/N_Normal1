name_f = input()
f = open(name_f)
text = f.read()
text = text.split('\n')
a = text[:-1]
N = len(a)
a = [int(x) for x in a]

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

f = input()