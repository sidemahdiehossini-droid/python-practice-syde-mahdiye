n = int(input())

def f(a, b):
    if a > n:
        print("{", end=" ")
        for x in b:
            print(x, end=" ")
        print("}")
        return

    b.append(a)
    f(a + 1, b)

    b.pop()
    f(a + 1, b)

f(1, [])
