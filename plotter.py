from matplotlib import pyplot as plt
import numpy as np

def pressure_profile(r,P):
    plt.title("Pressure profile")
    plt.xlabel("r (m)")
    plt.ylabel("Pressure (N/$m^{2}$)")
    plt.xscale('log')
    plt.plot(r,P)
    plt.show()

def mass_profile(r,M):
    plt.title("Mass profile")
    plt.xlabel("r (m)")
    plt.ylabel("mass ($g$)")
    plt.xscale('log')
    plt.plot(r,M)
    plt.show()

def density_profile(r,rho):
    plt.title("Density profile")
    plt.xlabel("r (m)")
    plt.ylabel(r'$\rho$(g/$cm^3$)')
    plt.xscale('log')
    plt.plot(r,rho)
    plt.show()
