for n in range(3, 21):
    print(f'{n}= ', end=" ")
    for a in range(1, n):
        for b in range(a + 1, n):
            if n % (a + b) == 0:
                print(f'{a}{b}', end="")
    print()
