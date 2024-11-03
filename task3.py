"""
Task3: Implement the following function according to the
specification provided in the comments below.
"""

"""
Import modules here, if needed
**Restriction: only standard libraries (e.g. 'math') and 'matplotlib' are allowed.
The use of other external libraries (e.g. 'numpy') is *NOT* allowed in this homework.**
"""


def min_max_distance(lst_v0_theta: list[tuple[float, float]]) -> tuple[float, float]:
    """ Finds the shortest and the longest traveled distance (eq. (2) in 'main.ipynb'), given a list with
    different pairs of initial velocity and angle.

    **Requirement: the functions implemented in task2.py MUST be used!**

    Parameters
    ----------
    lst_v0_theta : list of tuples, each tuple containing:
        First item: the initial velocity v0, here given in km/h
        Second item: the angle theta, here given in degrees

    Returns
    -------
    tuple (float, float)
        First item: shortest traveled distance in meters
        Second item: longest traveled distance in meters
    """
    pass

def plot_trajectories(lst_v0_theta: list[tuple[float, float]], filename: str, N: int) -> None:
    """ Plots the trajectory according to eq. (1) in 'main.ipynb' for each pair of 
    initial velocity and angle provided in 'lst_v0_theta'.

    The plot contains
    - labels and units for the x and y axes
    - legends identifying each trajectory by its parameters (v0, theta).

    **Requirement: the functions implemented in task2.py MUST be used!**

    Parameters
    ----------
    lst_v0_theta : list of tuples, each tuple containing
        First item: the initial velocity v0, here given in km/h
        Second item: the angle theta, here given in degrees
    filename : Name of the file where the plot is saved
    N : Number of equidistant evaluations to use for each trajectory
    """
    pass

if __name__ == '__main__':
    """ You could call your functions here to perform your own tests. """
    pass