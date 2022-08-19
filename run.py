import constants
from solver import tov



def main():

    star = tov.TOVsolver #neutron star object

    Properties = star.rk4(mass,N,K,rho0,gamma,Nmax)
    radius = Properties[3]
    Pressure = Properties[0]



if __name__== '__main__':
    main()







