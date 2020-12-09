#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
from pylab import *
import scipy.integrate as spi

#Parametros
S0 = 0.999
I0 = 0.001
H0 = 0.0
E0 = 0.0
K0 = 0.0
R0 = 0.0
PopIn = (S0, E0, I0, H0, K0, R0)
beta_F = 0.50
beta_H = beta_F/2
alpha = 1/2.
kappa = 0.05
lamda = 1/14. 
gamma =1/10.    
t_end = 200       
t_start = 1
t_step = .02
t_interval = np.arange(t_start, t_end, t_step)

#Resolvemos ecuacion diferenciales sujeto a condiciones iniciales.

def eq_system(PopIn,t):
    #Creando un arreglo de ecuaciones
    Eqs= np.zeros((6))
    Eqs[0] = -beta_F*PopIn[0]*PopIn[2] - lamda*PopIn[0]
    Eqs[1] = beta_F*PopIn[0]*PopIn[2] + beta_H*PopIn[3]*PopIn[2] - alpha*PopIn[1]
    Eqs[2] = alpha*PopIn[1] - gamma*PopIn[2] - kappa*PopIn[2]*PopIn[3]
    Eqs[3] = lamda*PopIn[0] - beta_H*PopIn[3]*PopIn[2]
    Eqs[4] = kappa*PopIn[2]*PopIn[3]
    Eqs[5] = gamma*PopIn[2]
    return Eqs

SIR = spi.odeint(eq_system, PopIn, t_interval)


S=(SIR[:,0])
E=(SIR[:,1])
I=(SIR[:,2])
H=(SIR[:,3])
K=(SIR[:,4])
R=(SIR[:,5])


x=arange(len(SIR),dtype=float)


for i in range(len(x)):
    x[i]=(x[i]*t_step)

SIR_plot= vstack([S,E,I,H,K,R,x])

#Graficar
fig= figure()
ax = fig.add_subplot(211)
plot(SIR_plot[6],SIR_plot[0],'g--',SIR_plot[6],SIR_plot[2],'r-',SIR_plot[6],SIR_plot[3],'-.b',linewidth=3) 
xlabel("Tiempo (dias")
ylabel("Proporcion de la poblacion")
title("Simulacion: z0mb1e")
grid(True)
legend(("Sobrevivientes en peligro", "Infectados", "Sobrevivientes a salvo"), shadow=True, fancybox=True)

ax = fig.add_subplot(212)
plot(SIR_plot[6],SIR_plot[4],'k--',SIR_plot[6],SIR_plot[5],linewidth=3) 
xlabel("Tiempo (dias)")
ylabel("Proporcion de la poblacion")
grid(True)
legend(("Zombies eliminados", "Humanos eliminados"), shadow=True, fancybox=True)

show()


# In[ ]:




