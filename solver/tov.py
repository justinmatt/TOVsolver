import numpy as np

def dPdr(P,rho,m,r):
    G=6.67e-8 #cgs units
    c=3.0e10 #cm/s
    #m=(4/3)*np.pi*r**3*rho
    rs = 2*G*m/c**2
    #eps=10e-5
    if r==0:
        return 0 #to handle the problem of r=0
    else:
        dPdr = -(G/(r**2))*(rho + P/c**2)*(m+4*np.pi*r**3 * (P/c**2))*(1- (rs/r))**-1
        return dPdr
    
def dmdr(r,rho):
    return 4*np.pi*r**2*rho

class TOVsolver:
    def rk4(Mass,Rmax,N,K,rho0,gamma,Nmax=10000):
        r0=0
        mi=0
        dr = Rmax/(N-1)
        P0 = K*(rho0)**gamma
        P=[P0]
        M=[mi]
        rho=[rho0]
        r=[r0]
        
        i=0
        while(P0>0.0 and i<Nmax): #conditions for looping was changed
                r0+=dr
                
                mi=mi+(4/3) * np.pi * (r0**3 - (r0-dr)** 3) * rho0
                #mi = mi + dmdr(r0-dr,rho0)*dr
                k1 = dPdr(P0,rho0,mi,r0)
                
                k2 = dPdr(P0+k1*(dr/2),rho0,mi,r0+(dr/2))
                
                k3 = dPdr(P0+k2*(dr/2),rho0,mi,r0+(dr/2))
                
                k4 = dPdr(P0+k3*dr,rho0,mi,r0+dr)
                
                
                #mi = mi+dmdr(r0,rho0)*dr

                P0=P0+(dr/6)*(k1+2*k2+2*k3+k4)
                if P0<0.0:
                    break
                    
                rho0=(P0/K)**(1/gamma)
                P.append(P0)
                M.append(mi)
                rho.append(rho0)
                r.append(r0)
                #P,M,rho,r=P0,mi,rho0,r0
                
                i+=1
                
        return  P,M,rho,r


    def euler(Mass,Rmax,N,K,rho0,gamma,Nmax=10000):
        r0=0
        mi=0
        dr = Rmax/(N-1)
        P0 = K*(rho0)**gamma
        P=[P0]
        M=[mi]
        rho=[rho0]
        r=[r0]
        
        i=0
        while(P0>0.0 and i<Nmax): #conditions for looping was changed
                r0+=dr
                
                mi=mi+(4/3) * np.pi * (r0**3 - (r0-dr)** 3) * rho0
                #mi = mi + dmdr(r0-dr,rho0)*dr
                k1 = dPdr(P0,rho0,mi,r0)
                
            
                
                
                #mi = mi+dmdr(r0,rho0)*dr

                P0=P0+(dr)*(k1)
                if P0<0.0:
                    break
                    
                rho0=(P0/K)**(1/gamma)
                P.append(P0)
                M.append(mi)
                rho.append(rho0)
                r.append(r0)
                #P,M,rho,r=P0,mi,rho0,r0
                
                i+=1
        return  P,M,rho,r

        