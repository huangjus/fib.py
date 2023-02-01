def fib(position):
    """
    Returns the number at a given position in the Fibonacci sequence.

    position: The position in the Fibonacci sequence to return.

    Returns:
    num2: The number at the given position in the Fibonacci sequence.
    """

    if position <= 0:
        return None
    elif position == 1 or position == 2:
        return 1
    else:
        num1, num2 = 1, 1
        for i in range(2, position):
            num1, num2 = num2, num1 + num2
        return num2
