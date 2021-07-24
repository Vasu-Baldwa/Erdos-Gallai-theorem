# Havel-Hakimi Algorithm
# https://en.wikipedia.org/wiki/Havel%E2%80%93Hakimi_algorithm


def HavelHakimi(a):
    while True:
        # if all ints == 0
        if a[0] == 0 and a[len(a)-1] == 0:
            print("Good Graph")
            return True
        element1 = a[0]
        a = a[1:]
        # Not enough elements remaining for the subtraction step (No simple graph exists).
        if element1 > len(a):
            print("Not enough elements remaining for the subtraction step")
            return False
        # Subtraction step
        for i in range(element1):
            a[i] -= 1
            # Negative number after subtraction
            if a[i] < 0:
                print("Negative number after subtraction")
                print("a[i]: " + str(a[i]))
                return False


test = [6, 6, 5, 4, 3, 3, 1]
print(HavelHakimi(test))
