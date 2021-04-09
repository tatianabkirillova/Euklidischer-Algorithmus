steps = 0


def print_index(i):
    if i == 0:
        print("a ")
    elif i == 1:
        print("b ")
    elif i == 2:
        print("q ")
    elif i == 3:
        print("r ")


def print_table(a, b, r, q):
    table = [a, b, q, r]
    i = 0

    for row in table:
        print_index(i)
        line = " "
        for el in row:
            line = line + str(el) + " "
        print(line)
        i += 1


def get_items():
    a = [0, 1]
    b = [1, 0]
    r = []
    q = []
    m = 0
    n = 0
    scan(m, n, r, q)
    iteration_r_q(m, n, r, q)
    iteration_a_b(a, q)
    iteration_a_b(b, q)
    print_table(a, b, r, q)


def scan(m, n, r, q):
    m = input('m = ')
    n = input('n = ')

    r.append(m)
    r.append(n)
    q.append(m)
    q.append(n)


def iteration_a_b(a, q):
    for j in range(1, steps):
        new_a = a[j - 1] - q[j+1] * a[j]
        a.append(new_a)


def iteration_r_q(m, n, r, q):
    global steps
    i = 0

    while True:
        rest_i = r[i] % r[i + 1]
        quotient_i = r[i] / r[i + 1]
        r.append(rest_i)
        q.append(quotient_i)
        i += 1
        if rest_i == 0:
            break
    steps = len(q) - 2


def main():
    get_items()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Euklidischer-Algorithmus
