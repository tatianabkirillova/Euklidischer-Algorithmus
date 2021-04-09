steps = 0
m = 0
n = 0


def print_gcd(a, b, r):
    print("\ngcd(" + str(m) + "," + str(n) + ") = (" + str(a[steps - 1]) + "*"
          + str(m) + ") + (" + str(b[steps - 1]) + "*" + str(n) + ")" + " = " + str(r[steps - 1]))


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

    print_gcd(a, b, r)


def get_items():
    a = [0, 1]
    b = [1, 0]
    r = []
    q = []
    scan(r, q)
    iteration_r_q(r, q)
    iteration_a_b(a, q)
    iteration_a_b(b, q)
    print_table(a, b, r, q)


def switch():
    global m
    global n
    t = m
    m = n
    n = t


def scan(r, q):
    global m
    global n
    m = int(input('m = '))
    n = int(input('n = '))
    if m > n:
        switch()

    r.append(n)
    r.append(m)
    q.append(n)
    q.append(m)


def iteration_a_b(a, q):
    for j in range(1, steps - 1):
        new_a = a[j - 1] - q[j+1] * a[j]
        a.append(new_a)


def iteration_r_q(r, q):
    global steps
    i = 0

    while True:
        rest_i = r[i] % r[i + 1]
        quotient_i = r[i] / r[i + 1]
        r.append(int(rest_i))
        q.append(int(quotient_i))
        i += 1
        if rest_i == 0:
            break
    steps = len(q) - 1


def main():
    get_items()


if __name__ == '__main__':
    main()
