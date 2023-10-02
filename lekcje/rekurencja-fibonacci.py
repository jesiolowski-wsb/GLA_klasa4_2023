# napisz funkcję wyliczającą wartość elementu na pozycji 'n' ciągu fibonacciego
# wykorzystaj rekurencję
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(f"fib(0): {fib(0)}")
print(f"fib(1): {fib(1)}")
print(f"fib(2): {fib(2)} (1+0)")
print(f"fib(3): {fib(3)} (1+1)")
print(f"fib(4): {fib(4)} (2+1)")
print(f"fib(5): {fib(5)} (3+2)")
print(f"fib(6): {fib(6)} (5+3)")
print(f"fib(7): {fib(7)} (8+5)")
print(f"fib(8): {fib(8)} (13+8)")
print(f"fib(9): {fib(9)} (21+13)")
print(f"fib(10): {fib(10)} (34+21)")

