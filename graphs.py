import matplotlib.pyplot as plt
import numpy as np

# O(1) 
def constant():
    return np.ones_like(x)

# O(log(n)) 
def logarithmic():
    return np.log(x)

# O(log(log(n))) 
def loglog():
    return np.log(np.log(x))

# O(x^2) Quadratic function
def quadratic():
    return x ** 2

# O(x * log(x)) 
def xlogx():
    return x * np.log(x)

if __name__ == "__main__":
    x = np.linspace(1, 1000, 1000)  # Start from 1 to avoid log(0) and log(log(0))

    y_constant = constant()
    y_logarithmic = logarithmic()
    y_loglog = loglog()
    y_quadratic = quadratic()
    y_xlogx = xlogx()

    plt.figure(figsize=(10, 6))

    # Uncomment Below For O(1)
    plt.plot(x, y_constant, label='O(1) - Constant', color='r')

    # Uncomment Below For O(log(n))
    # plt.plot(x, y_logarithmic, label='O(log(n)) - Logarithmic', color='g')

    # Uncomment Below For O(log(log(n)))
    # plt.plot(x, y_loglog, label='O(log(log(n))) - Log-Log', color='b')

    # Uncomment Below For O(n^2)
    # plt.plot(x, y_quadratic, label='O(x^2) - Quadratic', color='purple')

    # Uncomment Below For O(nlog(n))
    # plt.plot(x, y_xlogx, label='O(x * log(x)) - x * log(x)', color='orange')

    # Set custom labels for x and y axes
    plt.xlabel('Time')  # Custom x-axis label
    plt.ylabel('Size of Array')  # Custom y-axis label

    # Removing default ticks and setting custom ones if needed
    plt.xticks([])  # Remove x-axis ticks
    plt.yticks([])  # Remove y-axis ticks

    plt.title('Comparison of Different Time Complexity Functions')
    plt.legend()
    plt.grid(False)
    
    plt.show()
