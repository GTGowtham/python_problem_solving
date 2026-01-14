# practice_fact.py

class CalFact:
    # Recursive method to calculate factorial
    def fact(self, n):
        if n == 0:
            return 1
        else:
            return n * self.fact(n - 1)


if __name__ == "__main__":
    c = CalFact()
    print(c.fact(5))   # prints 120
