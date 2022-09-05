import constants
from solver import tov
import argparse
from plotter import density_profile, mass_profile, pressure_profile



def main():

    parser = argparse.ArgumentParser(description="give parameters to solve TOV equation")

    parser.add_argument("-m","--final_mass",type=float,help="total mass of the star")
    parser.add_argument("-p0","--rho0",default=1.0,type=float,help="central density (units of nuclear density)")
    parser.add_argument("-K","--adiabatic_coeff",type=float, help="adiabatic coefficient of the state equation")
    parser.add_argument("-y","--gamma",default=2.75,type=float,help="polytropic index")
    parser.add_argument("-N","--grids",default=2000,type=int,help="number of grids for computing")
    parser.add_argument("-R","--max_rad",default=50e5,type=float,help="maxiumum radius of the star")
    parser.add_argument("-t","--tol",default=0.001,type=float,help="tolerance")
    args = parser.parse_args()

    star = tov.TOVsolver(args.final_mass,args.rho0,args.adiabatic_coeff,args.gamma,args.grids,args.max_rad,args.tol)

    Pressure,Mass,density,radius = star.solver()
    #plots
    pressure_profile(radius,Pressure)
    mass_profile(radius,Mass)
    density_profile(radius,density)

if __name__== '__main__':
    main()







