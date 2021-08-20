# NOTE: most of these functions can be implemented
# using recursion, but Python has limitation on recursion
# dept and recursion has a better implementation (perf) in functional prog.
# lang than Python.


class ValidationError(Exception):
    pass


def assert_integer(number: int):
    if not isinstance(number, int):
        raise ValidationError("Type not supported.")


def fibbonaci(position: int) -> int:
    """Returns position of fiboniacci number.

    Usage:
    import solver
    solver.fibbonaci_with_position(10)
    """
    assert_integer(position)

    # get starting position cases
    if position == 0:
        return 0
    elif position in [1, 2]:
        return 1

    current_number = 1
    previous_number = 1
    current_position = 1
    resulted_number = 0
    # will finish in O(n)-time
    # O(1) is the space complexity
    while current_position < position:
        resulted_number = current_number + previous_number
        current_number = previous_number
        previous_number = resulted_number
        current_position += 1
    return current_number


def fibbonaci_recursive(position: int) -> int:
    """Returns position of fiboniacci number (recursive).

    Usage:
    import solver
    solver.fibbonaci_with_position_recursive(10)
    """
    assert_integer(position)

    if position == 0:
        return 0
    elif position == 1:
        return 1
    return (fibbonaci_recursive(position - 1) +
            fibbonaci_recursive(position - 2))


def ackermann_recursive(n: int, m: int) -> int:
    assert_integer(n)
    assert_integer(m)

    # NOTE: I lost my mind to make this iterative
    # but my solution is not correct, if the iterative
    # is required I can spend more time o that
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann_recursive(m - 1, 1)
    return ackermann_recursive(m - 1, ackermann_recursive(m, n - 1))


def factorial(number: int) -> int:
    """Calculates factorial of a number.

    Usage:

    import solver
    solver.factorial(10)
    """
    # NOTE: can use import math; math.factorial(10),
    # but why not code for fun. :)
    assert_integer(number)

    result = 1
    for descending_number in range(1, number+1):
        result *= descending_number
    return result


def factorial_recursive(number: int) -> int:
    """Calculates factorial of a number (recursive).

    Usage:

    import solver
    solver.factorial(10)
    """
    assert_integer(number)

    if number == 1:
        return 1
    return number * factorial_recursive(number-1)
