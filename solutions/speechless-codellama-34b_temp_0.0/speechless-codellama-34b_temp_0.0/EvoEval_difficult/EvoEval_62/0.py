def derivative(xs: list, x: float):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial at the given value of x
    """
    derivative = []
    for i in range(1, len(xs)):
        derivative.append(xs[i] * i)
    derivative = [d * x for d in derivative]
    return derivative