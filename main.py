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

Sfinal = [0,0,0,0,0,0,0,0,0,0]


h = 1/24
γ = 0.729
σ = 0.159
θ = 0.475
µ = [0.001,0.005,0.005,0.024,0.037,0.068,0.183,0.325,0.446,0.611]
ψ = [0.021168,0.006048,0.012096,0.009828,0.017388,0.021924,0.031752,0.055944,\
     0.033264,0.055944]
ϕ0 = [0.972,0.992,0.984,0.987,0.977,0.971,0.958,0.926,0.956,0.926]
ϕ1 = [1,1,0.85,0.85,0.76,0.76,0.73,0.69,0.74,0.74]
ω = [0.167,0.095,0.099,0.162,0.338,0.275,0.343,0.378,0.334,0.302]
τ1 = [0.000185,0.000925,0.00092,0.0044,0.0068,0.0126,0.034,0.060,0.083,0.113]
τ2 = [0.000185,0.000925,0.00092,0.0044,0.0068,0.0126,0.034,0.060,0.083,0.113]
δ1 = 0.240
δ2 = [0.735,0.7499,0.744,0.746,0.739,0.734,0.724,0.700,0.723,0.700]
δ3 = [0.184815,0.184075,0.184075,0.18056,0.17815,0.17242,0.151145,0.124875,\
      0.10249,0.071965]
δ4 = [0.184815,0.184075,0.184075,0.18056,0.17815,0.17242,0.151145,0.124875,\
      0.10249,0.071965]
p = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]

Casym = ([[7.71, 1.23, 1.03, 2.4, 1.36, 1.06, 0.59, 0.24, 0.11, 0.01],
                 [1.2, 10.38, 2.44, 2.32, 2.83, 0.93, 0.37, 0.3, 0.04, 0.04],
                 [0.93, 2.25, 6.06, 3.57, 3.51, 2.95, 0.65, 0.31, 0.31, 0.07],
                 [2.03, 2.01, 3.35, 5.53, 4.9, 3.22, 1.35, 0.55, 0.26, 0.08],
                 [1.03,2.19,2.95,4.38,5.56,3.36,1.48,1,0.3,0.04],
                 [0.89,0.79,2.74,3.18,3.72,3.82,1.44,0.63,0.37,0.05],
                 [0.65,0.42,0.8,1.75,2.15,1.89,1.96,0.92,0.33,0.05],
                 [0.34,0.44,0.49,0.94,1.89,1.08,1.19,1.5,0.32,0.04],
                 [0.27,0.11,0.85,0.75,0.99,1.09,0.74,0.56,1,0.16],
                 [0.28,0.88,1.64,1.91,1.08,1.27,1.03,0.61,1.37,0.97]])

Csym = ([[6.815,1.071,0.935,2.214,1.229,0.939,0.5025,0.20498,0.0837,0.01194],
         [1.0448,9.334,2.2277,2.0904,2.6278,0.8367,0.3156,0.264,0.037,0.0392],
         [0.841,2.055,5.639,3.218,3.180,2.703,0.577,0.271,0.276,0.075],
         [1.88,1.82,3.037,4.98,4.368,2.875,1.167,0.492,0.232,0.081],
         [0.946,2.072,2.719,3.955,5.072,3.049,1.3014,0.9,0.27,0.0414],
         [0.79144,0.7228,2.5313,2.8519,3.3395,3.488,1.264,0.5509,0.3237,0.049],
         [0.5567,0.35828,0.709467,1.52096,1.87329,1.66128,1.69075,0.78677,0.279\
          ,0.0485],
         [0.29128,0.3844,0.4277,0.8222,1.6626,0.9286,1.0093,1.3159,0.2786,\
          0.0421],
         [0.21034,0.0952,0.771,0.68597,0.88027,0.9645,0.6327,0.49247,0.95,\
          0.173],
         [0.234973,0.79023,1.64042,1.8801,1.0585,1.13766,0.8633,0.5832,1.362,\
          1.00253]])

cnt = {}
cntransicao = {}

tS0 = tuple(S0)
tE0 = tuple(E0)
tPreSym = tuple(PreSym)
tAsym = tuple(Asym)
tMild = tuple(Mild)
tSeve = tuple(Seve)
tHosp = tuple(Hosp)
tICU = tuple(ICU)
tRecov = tuple(Recov)
tDeceas = tuple (Deceas)

t0 = tuple([tS0,tE0,tPreSym,tAsym,tMild,tSeve,tHosp,tICU,tRecov,tDeceas])
cnt[t0]=1

t=0
for t in range (2):
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
        for j in range (10):
            assert (S0[j] >= 0)
            A1 = 0
            for i in range (10):
                A = ((Casym[j][i])*(PreSym[i]+Asym[i]))+(Csym[j][i]*
                                                         (Mild[i]+Seve[i]))
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
     
            IMildNew = np.random.binomial(PreSym[j]-IAsym1[j],1-math.exp
                                          (-h*(1-p[j]))*θ)
            IMild1 += [IMildNew]
            
            ISeveNew = np.random.binomial(Mild[j],1-math.exp(-h*ψ[j]))
            ISeve1 += [ISeveNew]
            
            IHospNew = np.random.binomial(Seve[j],1-math.exp(-h*ϕ1[j]*ω[j]))
            IHosp1 += [IHospNew]
            
            IICUNew = np.random.binomial(Seve[j]-IHosp1[j],1-math.exp(-h*
                                                            (1-ϕ1[j])*ω[j]))
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
            
        tS0 = tuple(S0)
        tE0 = tuple(E0)
        tPreSym = tuple(PreSym)
        tAsym = tuple(Asym)
        tMild = tuple(Mild)
        tSeve = tuple(Seve)
        tHosp = tuple(Hosp)
        tICU = tuple(ICU)
        tRecov = tuple(Recov)
        tDeceas = tuple (Deceas)
        
        tS2 = tuple(S2)
        tE2 = tuple(E2)
        tPreSym2 = tuple(PreSym2)
        tAsym2 = tuple(Asym2)
        tMild2 = tuple(Mild2)
        tSeve2 = tuple(Seve2)
        tHosp2 = tuple(Hosp2)
        tICU2 = tuple(ICU2)
        tRecov2 = tuple(Recov2)
        tDeceas2 = tuple (Deceas2)

        ttrans = tuple([tS0,tE0,tPreSym,tAsym,tMild,tSeve,tHosp,tICU,tRecov,tDeceas\
                       ,tS2,tE2,tPreSym2,tAsym2,tMild2,tSeve2,tHosp2,tICU2,tRecov2\
                         ,tDeceas])
        
        if ttrans in cntransicao:
            cntransicao[ttrans]+=1
        
        else:
            cntransicao[ttrans]=1
        
                                  
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
        
        tS0 = tuple(S0)
        tE0 = tuple(E0)
        tPreSym = tuple(PreSym)
        tAsym = tuple(Asym)
        tMild = tuple(Mild)
        tSeve = tuple(Seve)
        tHosp = tuple(Hosp)
        tICU = tuple(ICU)
        tRecov = tuple(Recov)
        tDeceas = tuple (Deceas)

        t0 = tuple([tS0,tE0,tPreSym,tAsym,tMild,tSeve,tHosp,tICU,tRecov,tDeceas])
        
        if t0 in cnt:
            cnt[t0]+=1
            
        else:
            cnt[t0]=1


"""        
        print ("step",t+1)
        print ("Suscetiveis:",S0,"Expostos:",E0,"Pré-Sintomáticos",PreSym,\
               "Assintomáticos",Asym,"Mild:",Mild,"Sevear:",Seve,"Hospitaliza"\
                   "dos:",Hosp,"ICU:",ICU,"Recuperados:",Recov,"Perdas:",Deceas)
 """       

k=[]
for l in range (10):
    h = S0[l]+E0[l]+PreSym[l]+Asym[l]+Mild[l]+Seve[l]+Hosp[l]+ICU[l]+Recov[l]+Deceas[l]
    k += [h]
    


pessoastotal = 0
mortes =0


for p in range (10):
    pessoastotal += k[p]

for i in range (10):
    mortes += Deceas[i]
    
mortalidade = (mortes / pessoastotal)*100





"""
s1 = [1,2]
i1 =[2,3]
ts1 = tuple(s1)
ti1 = tuple (i1)
t1 = tuple([ts1,ti1])
cnt[t1]=0


if t1 in cnt:
    cnt[t1]+=1

else:
    cnt[t1]=1

s2 = [1,2]
i2 =[4,3]
ts2 = tuple(s2)
ti2 = tuple (i2)
t2 = tuple([ts2,ti2])


if t2 in cnt:
    cnt[t2]+=1

else:
    cnt[t2]=1
    
 """   
