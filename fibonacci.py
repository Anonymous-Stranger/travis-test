
def fib(n):
    return fib_helper(0, 1, n)


def fib_helper(f1, f2, n):
    if n <= 0:
        return f1
    return fib_helper(f2, f1 + f2, n - 1)
