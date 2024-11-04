"""
Import modules here, if needed
**Restriction: only standard libraries (e.g. 'math') and 'matplotlib' are allowed.
The use of other external libraries (e.g. 'numpy') is *NOT* allowed in this homework.**
"""
import math
import matplotlib.pyplot as plt

"""
Write a python script which creates a plot of the function given by eq. (1) in 'main.ipynb'.

Use the following parameters in your implementation:
- Initial velocity: v0 = 80 km/h
- Initial angle: theta = 45°
- g = 9.81 m/s²

Your script should carry out the following tasks:
- Create a list of x-coordinates with 50 equidistant values in the range (0,d) (see eq.(2) in 'main.ipynb')
- Create a list containing f(x) by evaluating the function (eq. (1)) at each of the 50 x-coordinates
- Print the x and y values to the console according to this format (example values follow):
    x = 0.000 m, y = 0.000 m
    x = 0.509 m, y = 0.504 m
    x = 1.018 m, y = 0.997 m
    ...
- Plot the data in your lists using 'matplotlib'
- Your plot must have expressive labels for the title and axes including physical quantities (e.g. 'distance (m)')
- The plotted graphic MUST be saved as a figure named 'task1.png'.
"""
v0 = 80 / 3.6
theta = math.radians(45)
g = 9.81
d = (v0 ** 2 * math.sin(2*theta))/g
x = [0 + i * (d) / 49 for i in range(50)]
print(x, d, sep=", ")
y = [(-g/(2*(v0**2)*(math.cos(theta)**2)))*(x_**2) + math.tan(theta)*x_ for x_ in x]
for i in range(len(x)):
    print(f"x = {round(x[i],3)}, y = {round(y[i],3)}")
    
plt.plot(x,y, '--mo',label='Trajectory')
plt.legend()
plt.title("Ballistic Motion")
plt.xlabel("Distance [m]")
plt.ylabel("Height [m]")
plt.savefig("task1.png")
plt.show()