import numpy as np
from constants import G,c

def dPdr(r,m,rho,P):
    rs = 2*G*m/c**2

    if r==0:
        return 0
    dPdr = -(G/(r**2))*(rho + P/c**2)*(m+4*np.pi*r**3 * (P/c**2))*(1- (rs/r))**-1
    return dPdr

def rho_update(Mass,m_calculated,rho0):
    diff = Mass-m_calculated
    diff/=max(m_calculated,Mass)
    rho0+=diff*rho0
    return rho0,diff

def TOV(rho0,K,gamma,N,Rmax):
    r0=0
    dr = Rmax/(N-1)
    m0 = (4/3)*np.pi*r0**3*rho0
    P0 = K*rho0**gamma
    P=[]
    r=[]
    m=[]
    rho=[]
    while(P0>0):
        P.append(P0)
        r.append(r0)
        rho.append(rho0)
        m.append(m0)
        
        P0 = P0 + dPdr(r0,m0,rho0,P0)*dr
        if P0<0:
            break
        rho0 = (P0/K)**(1/gamma)
        r0 = r0 + dr
        m0 = m0 + (4/3)*np.pi*(r0**3 - (r0-dr)**3)*rho0
        

    return P,m,rho,r

class TOVsolver(object):
    def __init__(self,Mass,rho0,K,gamma,N=2000,Rmax=50e5,tol=0.001):
        self.Mass = 2e33*Mass #multiplied with solar mass
        self.rho0 = 2.3e14*rho0 #multiplied with nuclear density
        self.K = K
        self.gamma = gamma
        self.N = N
        self.Rmax = Rmax
        self.tol = tol

    def solver(self):
        diff=self.tol+1
        i=0
        while(abs(diff)>self.tol and i<10000):
            i+=1
            P,M,rho,r = TOV(self.rho0,self.K,self.gamma,self.N,self.Rmax)
            self.rho0,diff = rho_update(self.Mass,M[-1],rho[0])
      
        return P,M,rho,r



        