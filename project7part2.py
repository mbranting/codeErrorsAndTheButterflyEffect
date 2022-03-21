# McKenna Branting
# Project 7 Part 2
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

arrivalTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
serviceStartTime = [1, 3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 10, 12.41, 12.82, 13.28, 14.65, 15]
exitTime = [3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 9.58, 12.41, 12.82, 13.28, 14.65, 14.92, 15.27]
timeInQueue = [0, 1.22, 1.98, 3.11, 2.25, 2.01, 1.71, 1.18, 0.4, 0, 1.41, 0.82, 0.28, 0.65, 0]
nCustomersInSystem = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nCustomersInQueue = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

plt.plot(arrivalTime, serviceStartTime)
plt.title("Arrival Time as a function of service start time")
plt.xlabel("Arrival Time")
plt.ylabel("Service Start Time")
plt.show()

plt.plot(arrivalTime, exitTime)
plt.title("Arrival Time as a function of exit time")
plt.xlabel("Arrival Time")
plt.ylabel("Exit Time")
plt.show()

plt.plot(arrivalTime, timeInQueue)
plt.title("Arrival time as a function of time in queue")
plt.xlabel("Arrival Time")
plt.ylabel("Time in queue")
plt.show()

plt.plot(arrivalTime, nCustomersInSystem)
plt.title("Arrival Time as a function of customers in system")
plt.xlabel("Arrival Time")
plt.ylabel("Number of Customers in the System")
plt.show()

plt.plot(arrivalTime, nCustomersInQueue)
plt.title("Arrival Time as a function of customers in queue")
plt.xlabel("Arrival Time")
plt.ylabel("Number of Customers in Queue")
plt.show()
