from struct import unpack
from plotter import pressure_profile
from solver import tov

def star(params):
    obj = tov.TOVsolver
    properties = obj.rk4(params.final_mass,params.max_rad,params.grids,\
        params.adiabatic_coeff,params.rho0,params.gamma,params.max_iterations)

    return properties
