# InternshipCode

import numpy as np
import math

S0 = [100,100,100,100,100,100,100,100,100,100]
E0 = [0,0,0,0,0,0,0,0,0,0]
PreSym = [0,0,0,1,0,0,0,0,0,0]
Asym = [0,0,0,0,0,0,0,0,0,0]
Mild =[0,0,0,0,0,0,0,0,0,0]
Seve =[0,0,0,0,0,0,0,0,0,0]
Hosp =[0,0,0,0,0,0,0,0,0,0]
ICU =[0,0,0,0,0,0,0,0,0,0]
Recov =[0,0,0,0,0,0,0,0,0,0]
Deceas = [0,0,0,0,0,0,0,0,0,0]

h = 1/24
γ = 
σ =
θ = 
ψ = 
ϕ1 = 
ω = 
τ1 = 
τ2 =
δ1 =
δ2 =
δ3 =
δ4 =

Casym = np.matrix([[0.01, 0.04, 0.07, 0.08, 0.04, 0.05, 0.05, 0.04, 0.16, 0.97],
                 [0.11, 0.04, 0.31, 0.26, 0.3, 0.37, 0.33, 0.32, 1, 1.37],
                 [0.24, 0.3, 0.31, 0.55, 1, 0.63, 0.92, 1.5, 0.56, 0.61],
                 [0.59, 0.37, 0.65, 1.35, 1.48, 1.44, 1.96, 1.19, 0.74, 1.03],
                 [1.06,0.93,2.95,3.22,3.36,3.82,1.89,1.08,1.09,1.27],
                 [1.36,2.83,3.51,4.9,5.56,3.72,2.15,1.89,0.99,1.06],
                 [2.4,2.32,3.57,5.53,4.38,3.18,1.75,0.94,0.75,1.91],
                 [1.03,2.44,6.06,3.35,2.95,2.74,0.8,0.49,0.85,1.64],
                 [1.23,10.38,2.25,2.01,2.19,0.79,0.42,0.44,0.11,0.88],
                 [7.71,1.2,0.93,2.03,1.03,0.89,0.65,0.34,0.27,0.28]])

Csym = np.matrix([[0.01, 0.04, 0.07, 0.08, 0.04, 0.05, 0.05, 0.04, 0.16, 0.97],
                 [0.11, 0.04, 0.31, 0.26, 0.3, 0.37, 0.33, 0.32, 1, 1.37],
                 [0.24, 0.3, 0.31, 0.55, 1, 0.63, 0.92, 1.5, 0.56, 0.61],
                 [0.59, 0.37, 0.65, 1.35, 1.48, 1.44, 1.96, 1.19, 0.74, 1.03],
                 [1.06,0.93,2.95,3.22,3.36,3.82,1.89,1.08,1.09,1.27],
                 [1.36,2.83,3.51,4.9,5.56,3.72,2.15,1.89,0.99,1.06],
                 [2.4,2.32,3.57,5.53,4.38,3.18,1.75,0.94,0.75,1.91],
                 [1.03,2.44,6.06,3.35,2.95,2.74,0.8,0.49,0.85,1.64],
                 [1.23,10.38,2.25,2.01,2.19,0.79,0.42,0.44,0.11,0.88],
                 [7.71,1.2,0.93,2.03,1.03,0.89,0.65,0.34,0.27,0.28]])

def pstar ():
    for k in range (0,10):
        pstar = []
        for i in range (0,10):
            pt = 0
            A=-h*Casym[k,i]*(PreSym[i]+Asym[i]*+Csym*(Mild[i]+Seve[i])
            p_t = 1-math.exp(A)
            pt += p_t
            return pt
        pstar += [p_t]
            
def binomial ():
    for j in range (0,10):
        E1 = [] 
        Enew = binomial(S0[j],pstar[j]) 
        E1 += [Enew]
        
        IPreSym1 = []
        IPreSymNew = np.random.binomial(E0[j],1-math.exp(-hγ))
        IPreSym1 += [IPreSymNew]
        
        IAsym1 = []
        IAsymNew = np.random.binomial(PreSym[],1-math.exp(-h*p[j]*σ)) #p??#
        IAsym1 += [IAsymNew]
 
        IMild1 = []
        IMildNew = np.random.binomial(Seve[j]-IAsym1[j],1-math.exp(-h*(1-p[j]))*θ)
        IMild1 += [IMildNew]
        
        ISeve1 = []
        ISeveNew = np.random.binomial(Mild[j],1-math.exp(-h*ψ[j]))
        ISeve1 += [ISeveNew]
        
        IHosp1 = []
        IHospNew = np.random.binomial(Seve[j],1-math.exp(-h*ϕ1[j]*ω[j]))
        IHosp1 += [IHospNew]
        
        IICU1 = []
        IICUNew = np.random.binomial(Seve[j]-IHosp1[j],1-math.exp(-h*(1-ϕ1[j])*ω[j]))
        IICU1 += [IICU1]
        
        Rasym1 = []
        RasymNew = np.random.binomial(Asym[j], 1-math.exp(-h*δ1))
        Rasym1 += [RasymNew]
        
        Rmild1 = []
        RmildNew = np.random.binomial(Mild[j]-ISeveNew[j],1-math.exp(-h*δ2[j]))
        Rmild1 += [RmildNew]
        
        RHosp1 = []
        RHospNew = np.random.binomial(Hosp[j],1-math.exp(-h*δ3[j]))
        RHosp1 += [RHospNew]
        
        RICU1 = []
        RICUNew = np.random.binomial(ICU[j],1-math.exp(-h*δ4[j]))
        RICU1 += [RICUNew]
        
        DHosp1 = []
        DHospNew = np.random.binomial(Hosp[j]-RHospNew[j],1-math.exp(-h*τ1[j]))
        DHosp1 += [DHospNew]
        
        DICU1 = []
        DICUNew = np.random.binomial(ICU[j]-RICUNew[j],1-math.exp(-h*τ2[j]))
        DICU1 += [DICUNew]
        
        return E1, IPreSym1,IAsym1, IMild1, ISeve1, IHosp1, IICU1, Rasym1,Rmild1, RHosp1, RICU1, DHosp1, DICU1
