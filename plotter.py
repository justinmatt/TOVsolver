from matplotlib import pyplot as plt
import numpy as np

def pressure_profile(P,r):
    plt.title("Pressure profile")
    plt.xlabel("r (km)")
    plt.ylabel("Pressure (N/$m^{2}$")
    plt.xscale('log')
    plt.plot(r,P)
    plt.show()