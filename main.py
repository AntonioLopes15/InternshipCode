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
γ = 0.729
σ = 0.159
θ = 0.475
µ = [0.001,0.005,0.005,0.024,0.037,0.068,0.183,0.325,0.446,0.611]
ψ = [0.021168,0.006048,0.012096,0.009828,0.017388,0.021924,0.031752,0.055944,0.033264,0.055944]
ϕ0 = [0.972,0.992,0.984,0.987,0.977,0.971,0.958,0.926,0.956,0.926]
ϕ1 = [1,1,0.85,0.85,0.76,0.76,0.73,0.69,0.74,0.74]
ω = [0.167,0.095,0.099,0.162,0.338,0.275,0.343,0.378,0.334,0.302]
τ1 = [0.000185,0.000925,0.00092,0.0044,0.0068,0.0126,0.034,0.060,0.083,0.113]
τ2 = [0.000185,0.000925,0.00092,0.0044,0.0068,0.0126,0.034,0.060,0.083,0.113]
δ1 = 0.240
δ2 = [0.735,0.7499,0.744,0.746,0.739,0.734,0.724,0.700,0.723,0.700]
δ3 = [0.184815,0.184075,0.184075,0.18056,0.17815,0.17242,0.151145,0.124875,0.10249,0.071965]
δ4 = [0.184815,0.184075,0.184075,0.18056,0.17815,0.17242,0.151145,0.124875,0.10249,0.071965]


Casym = ([[0.01, 0.04, 0.07, 0.08, 0.04, 0.05, 0.05, 0.04, 0.16, 0.97],
                 [0.11, 0.04, 0.31, 0.26, 0.3, 0.37, 0.33, 0.32, 1, 1.37],
                 [0.24, 0.3, 0.31, 0.55, 1, 0.63, 0.92, 1.5, 0.56, 0.61],
                 [0.59, 0.37, 0.65, 1.35, 1.48, 1.44, 1.96, 1.19, 0.74, 1.03],
                 [1.06,0.93,2.95,3.22,3.36,3.82,1.89,1.08,1.09,1.27],
                 [1.36,2.83,3.51,4.9,5.56,3.72,2.15,1.89,0.99,1.06],
                 [2.4,2.32,3.57,5.53,4.38,3.18,1.75,0.94,0.75,1.91],
                 [1.03,2.44,6.06,3.35,2.95,2.74,0.8,0.49,0.85,1.64],
                 [1.23,10.38,2.25,2.01,2.19,0.79,0.42,0.44,0.11,0.88],
                 [7.71,1.2,0.93,2.03,1.03,0.89,0.65,0.34,0.27,0.28]])

Csym = ([[0.01, 0.04, 0.07, 0.08, 0.04, 0.05, 0.05, 0.04, 0.16, 0.97],[0.11, 0.04, 0.31, 0.26, 0.3, 0.37, 0.33, 0.32, 1, 1.37],[0.24, 0.3, 0.31, 0.55, 1, 0.63, 0.92, 1.5, 0.56, 0.61],
                 [0.59, 0.37, 0.65, 1.35, 1.48, 1.44, 1.96, 1.19, 0.74, 1.03],
                 [1.06,0.93,2.95,3.22,3.36,3.82,1.89,1.08,1.09,1.27],
                 [1.36,2.83,3.51,4.9,5.56,3.72,2.15,1.89,0.99,1.06],
                 [2.4,2.32,3.57,5.53,4.38,3.18,1.75,0.94,0.75,1.91],
                 [1.03,2.44,6.06,3.35,2.95,2.74,0.8,0.49,0.85,1.64],
                 [1.23,10.38,2.25,2.01,2.19,0.79,0.42,0.44,0.11,0.88],
                 [7.71,1.2,0.93,2.03,1.03,0.89,0.65,0.34,0.27,0.28]])

pstar = []    


Sfinal = [0,0,0,0,0,0,0,0,0,0]
E1 = []
IPreSym1 = []
IAsym1 = []
IMild1 = []
ISeve1 = []
IHosp1 = []
IICU1 = []
Rasym1 = []
Rmild1 = []
RHosp1 = []
RICU1 = []
DHosp1 = []
DICU1 = [] 
p = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]

S2 = [0,0,0,0,0,0,0,0,0,0]
E2 = [0,0,0,0,0,0,0,0,0,0]  
PreSym2 = [0,0,0,0,0,0,0,0,0,0]
Asym2 = [0,0,0,0,0,0,0,0,0,0]
Mild2 = [0,0,0,0,0,0,0,0,0,0]
Seve2 = [0,0,0,0,0,0,0,0,0,0]
Hosp2 = [0,0,0,0,0,0,0,0,0,0]
ICU2 = [0,0,0,0,0,0,0,0,0,0]
Recov2 = [0,0,0,0,0,0,0,0,0,0]
Deceas2 = [0,0,0,0,0,0,0,0,0,0]


for t in range (1000):
        for j in range (10):
            if S0[j] >=0 :          ###pstar
                                    A1 = 0
                                    for i in range (10):
                                        A = ((Casym[j][i])*(PreSym[i]+Asym[i]))+(Csym[j][i]*(Mild[i]+Seve[i]))
                                        A1 += A
                                    p_t = 1-(math.exp(-(h+t)*A1))
                                    pstar += [p_t]
                                    
                                    ###Inicio das binomiais
                                    Enew = np.random.binomial(S0[j],pstar[j]) 
                                    E1 += [Enew]
                                     
                                    IPreSymNew = np.random.binomial(E0[j],1-math.exp(-h*γ))
                                    IPreSym1 += [IPreSymNew]
                                    
                                    IAsymNew = np.random.binomial(PreSym[j],1-math.exp(-h*p[j]*σ))
                                    IAsym1 += [IAsymNew]
                             
                                    IMildNew = np.random.binomial(PreSym[j]-IAsym1[j],1-math.exp(-h*(1-p[j]))*θ)
                                    IMild1 += [IMildNew]
                                    
                                    ISeveNew = np.random.binomial(Mild[j],1-math.exp(-h*ψ[j]))
                                    ISeve1 += [ISeveNew]
                                    
                                    IHospNew = np.random.binomial(Seve[j],1-math.exp(-h*ϕ1[j]*ω[j]))
                                    IHosp1 += [IHospNew]
                                    
                                    IICUNew = np.random.binomial(Seve[j]-IHosp1[j],1-math.exp(-h*(1-ϕ1[j])*ω[j]))
                                    IICU1 += [IICUNew]
                                    
                                    RasymNew = np.random.binomial(Asym[j], 1-math.exp(-h*δ1))
                                    Rasym1 += [RasymNew]
                                    
                                    RmildNew = np.random.binomial(Mild[j]-ISeve1[j],1-math.exp(-h*δ2[j]))
                                    Rmild1 += [RmildNew]
                                    
                                    RHospNew = np.random.binomial(Hosp[j],1-math.exp(-h*δ3[j]))
                                    RHosp1 += [RHospNew]
                                    
                                    RICUNew = np.random.binomial(ICU[j],1-math.exp(-h*δ4[j]))
                                    RICU1 += [RICUNew]
                                    
                                    DHospNew = np.random.binomial(Hosp[j]-RHosp1[j],1-math.exp(-h*τ1[j]))
                                    DHosp1 += [DHospNew]
                                    
                                    DICUNew = np.random.binomial(ICU[j]-RICU1[j],1-math.exp(-h*τ2[j]))
                                    DICU1 += [DICUNew]
                                    
                                    ###Inicio do passo seguinte 
                                    S2New = []
                                    S2New = S0[j]-E1[j]
                                    S2[j] += S2New
                                    
                                    E2New = []
                                    E2New = E0[j]+E1[j]-IPreSym1[j]
                                    E2[j] += E2New
                                    
                                    IPreSym2New = []
                                    IPreSym2New = PreSym[j]+IPreSym1[j]-IAsym1[j]-IMild1[j]
                                    PreSym2[j] += IPreSym2New
                                    
                                    IAsym2New = []
                                    IAsym2New = Asym[j]+IAsym1[j]-Rasym1[j]
                                    Asym2[j] += IAsym2New
                                    
                                    IMild2New = []
                                    IMild2New = Mild[j] + IMild1[j] - ISeve1[j] - Rmild1[j]
                                    Mild2[j] += IMild2New
                                    
                                    ISeve2New = []
                                    ISeve2New = Seve[j]+ISeve1[j]-IHosp1[j]-IICU1[j]
                                    Seve2[j] = ISeve2New
                                    
                                    IHosp2New = []
                                    IHosp2New = Hosp[j]+IHosp1[j]-DHosp1[j]-RHosp1[j]
                                    Hosp2[j] = IHosp2New
                                    
                                    IICU2New = []
                                    IICU2New = ICU[j]+IICU1[j]-DICU1[j]-RICU1[j]
                                    ICU2[j] = IICU2New
                                    
                                    Recov2New = []
                                    Recov2New = Recov[j]+Rasym1[j]+Rmild1[j]+RHosp1[j]+RICU1[j]
                                    Recov2[j] = Recov2New
                                    
                                    Deceas2New = []
                                    Deceas2New = Deceas[j] + DHosp1[j] + DICU1[j]
                                    Deceas2[j] = Deceas2New
                                    
                                    
        S0 = S2
        E0 = E2
        PreSym = PreSym2
        Asym = Asym2
        Mild = Mild2
        Seve = Seve2
        Hosp = Hosp2
        ICU = ICU2
        Recov = Recov2
        Deceas = Deceas2 
        
        
        pstar = []
        E1 = []
        IPreSym1 = []
        IAsym1 = []
        IMild1 = []
        ISeve1 = []
        IHosp1 = []
        IICU1 = []
        Rasym1 = []
        Rmild1 = []
        RHosp1 = []
        RICU1 = []
        DHosp1 = []
        DICU1 = []
        
        
        S2 = [0,0,0,0,0,0,0,0,0,0] 
        E2 = [0,0,0,0,0,0,0,0,0,0]  
        PreSym2 = [0,0,0,0,0,0,0,0,0,0]
        Asym2 = [0,0,0,0,0,0,0,0,0,0]
        Mild2 = [0,0,0,0,0,0,0,0,0,0]
        Seve2 = [0,0,0,0,0,0,0,0,0,0]
        Hosp2 = [0,0,0,0,0,0,0,0,0,0]
        ICU2 = [0,0,0,0,0,0,0,0,0,0]
        Recov2 = [0,0,0,0,0,0,0,0,0,0]
        Deceas2 = [0,0,0,0,0,0,0,0,0,0]
        
print (S0,"Suscetiveis:")
print (E0,"Expostos:")
print (PreSym,"Pré-Sintomáticos")
print (Asym,"Assintomáticos")
print(Mild,"Mild:")
print(Seve,"Sevear:")
print(Hosp,"Hospitalizados:")
print(ICU,"ICU:")
print(Recov,"Recuperados:")
print(Deceas,"Perdas:")


k=[]
for l in range (10):
    h = S0[l]+E0[l]+PreSym[l]+Asym[l]+Mild[l]+Seve[l]+Hosp[l]+ICU[l]+Recov[l]+Deceas[l]
    k += [h]
    
print (k)
