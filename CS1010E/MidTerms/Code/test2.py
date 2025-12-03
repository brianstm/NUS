s = 0
for i in range(10):
    print("i: ", i)
    if (i % 2 == 0):
        print("2: ", i)
        i = i + 1
        print("2 after: ", i)
    if (i % 3 == 0):
        print("3: ", i)
        i = i - 1
        print("3 after: ", i)
    else:
        i = 0
    print("i after: ", i)
    s = s + i
    print("s: ", s, "\n")
print(s)
