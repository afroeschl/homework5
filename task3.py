"""
Task3: Implement the following function according to the
specification provided in the comments below.
"""

"""
Import modules here, if needed
**Restriction: only standard libraries (e.g. 'math') and 'matplotlib' are allowed.
The use of other external libraries (e.g. 'numpy') is *NOT* allowed in this homework.**
"""
import task2
import math
import matplotlib.pyplot as plt

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
    distances = []
    for v, t in lst_v0_theta:
        distances.append(task2.eval_range(v/3.6, math.radians(t)))
    distances.sort()
    min_distance = distances[0]
    distances.reverse()
    return min_distance, distances[0]
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

    for i,(v,t) in enumerate(lst_v0_theta):
        v = v/3.6
        t = math.radians(t)
        x = task2.sample(0, task2.eval_range(v,t), N)
        y = task2.eval_height_vectorized(v,t,x)
        plt.plot(x, y, "--", marker = 'o', label=(f"Trajectory {i}"))

    plt.legend()
    plt.title("Ballistic Motion")
    plt.xlabel("Distance [m]")
    plt.ylabel("Height [m]")
    plt.savefig(filename)
    plt.show()
    pass

if __name__ == '__main__':
    """ You could call your functions here to perform your own tests. """
    lst_v0_theta_1 = [(72, 20), (72, 30), (72, 45), (72, 60), (72, 75)]
    print(min_max_distance(lst_v0_theta_1))
    lst_v0_theta_2 = [(36, 45), (54, 45), (72, 45), (90, 45), (108, 45)]
    print(min_max_distance(lst_v0_theta_2))
    plot_trajectories(lst_v0_theta_1, "task3.png", 50)
    pass