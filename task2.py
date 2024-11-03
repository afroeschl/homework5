"""
Task2: Implement the following functions according to the
specification provided in the comments below.
"""

"""
Import modules here, if needed
**Restriction: only standard libraries (e.g. 'math') and 'matplotlib' are allowed.
The use of other external libraries (e.g. 'numpy') is *NOT* allowed in this homework.**
"""


def sample(start: float, end: float, N: int) -> list[float]:
    """ Creates a list containing 'N' (>=2) equidistant values between 'start' and 'end'
    in a given interval (inclusive).
    The function returns a list containing the equidistant values in increasing order.
    """
    pass


def eval_range(v0: float, theta: float) -> float:
    """ Computes the horizontally traveled distance (eq. (2) in 'main.ipynb').
        - v0 is the initial velocity already given in units of m/s (v0 > 0) and 
        - theta is the initial angle already given in units of rad (0 < theta < pi/2).
    The function returns the horizontally traveled distance in meters
    """
    pass


def eval_height(v0: float, theta: float, x: float) -> float:
    """ Computes the height of the trajectory (eq. (1) in 'main.ipynb') for a single x-coordinate (given in meters).
    The function returns the calculated height (in meters).
    """
    pass


def eval_height_vectorized(v0: float, theta: float, x: list[float]) -> list[float]:
    """ Computes the height of the trajectory (eq. (1) in 'main.ipynb') for a list of x-coordinates (given in meters).
    The function returns a list containing the heights (in meters) of the trajectory for the provided list of x-coordinates.
    """
    pass


if __name__ == '__main__':
    """ You could call your functions here to perform your own tests. """
    pass