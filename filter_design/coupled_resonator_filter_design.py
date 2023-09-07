# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:22:30 2022

@author: ARDISSON

Coupled Resonator Filter Design Prototype Calculator
"""
import numpy as np

#%% Low Pass Prototype
gk = []
n = 3
for k in range(1, n+1, 1):
    coefficient = round(2*np.sin((2*k-1)*np.pi/(2*n)),3)
    gk.append(coefficient)

# calculate corner and center frequencies
f1 = 1e9
f2 = 1.1e9
# f0 = f1 + f2 - np.sqrt((f2-f1)**2 + f1*f2)
f0 = np.sqrt(f1*f2)
f1_prime = 1/(2*np.pi)
# w_prime = ((f0/f1)-(f0/f2))*(f0/f1_prime)
w_prime = (f2-f1)/f1_prime
w0 = 2 * np.pi * f0

R1 = 50
Rn = 50
r = 1

#%% Capacitively Coupled lumped-constant BPF
# Resonator Elements
Lrk = 7.5e-9;
Crk = 1/((w0**2)*Lrk)
print(f'Crk is {round(Crk*(10**12),2)} pF, Lrk is {round(Lrk*(10**9),2)} nH')

# First coupling element
C01 = (1/w0) * np.sqrt((w_prime * Crk/R1 * gk[0])/(1 - (w_prime*Crk*R1/gk[0])))
print(f'The first coupling element, C01 is {C01} pF')

# Last coupling element
C34 = (1/w0) * np.sqrt((w_prime * Crk * r/Rn * gk[2])/(1 - w_prime*Crk*Rn/gk[2]))
print(f'The last coupling element, C34 is {C34}')

''' note:
The calculation of Cjk needs to have w_prime normalized by w0,
this is not mentioned in the Cohn paper
'''
C12 = w_prime/w0 * np.sqrt((Crk**2)/(gk[0]*gk[1]))
C23 = w_prime/w0 * np.sqrt((Crk**2)/(gk[1]*gk[2]))

'''
'''

C01_prime = C01/(1 + (w0**2)*(C01**2)*(R1**2))
C34_prime = C34/(1 + (w0**2)*(C34**2)*(Rn**2))

# Resonator 1
Lr1 = Lrk
# Cr1 = np.power(Crk * -C01_prime *-C12, 1/3)
Cr1 = Crk - C01_prime - C12
# Lr1 = 1/((w0**2)*Cr1)
print(f'Resonator 1 values: L={Lr1}, C={Cr1}')

print(f'Resonantor coupling capacitor C12={C12}')
# Resonator 2
Lr2 = Lrk
Cr2 = Crk - C12 - C23
print(f'Resonator 2 values: L={Lr2}, C={Cr2}')
print(f'Resonantor coupling capacitor C23={C23}')
# Resonator 3
Lr3 = Lrk
Cr3 = Crk - C23 - C34_prime
print(f'Resonator 3 values: L={Lr3}, C={Cr3}')

#%% Inductively Coupled Lumped-constant BPF
# # define source and load impedances
# R1 = 1
# Rn = 1
# r = 1

# # assign values to Lk and Ck
# Ck = 1e-12 # 2.2 pF
# Lk = 1/(Ck*(w0**2))
# print(f'Ck is {round(Ck*(10**12),2)} pF, Lk is {round(Lk*(10**9),2)} nH')

# # Get first resonator values
# L0 = 100e-9 # let L0 = 100 nH
# Cr1 = 1e-12 # Let Cr1 = 100 pF
# Lr1 = (1 + (w_prime*L0)/(gk[0]*Rn))/(Cr1*(w0**2))
# print(f'L0 is {round(L0*(10**9),2)} nH, Cr1 is {round(Cr1*10**12,2)}, Lr1 is {round(Lr1*10**9,2)} nH')

# # Get impedance of first impedance inverter
# M01 = (np.sqrt((w_prime*(R1**2 + (w0**2)*(L0**2)))/((w0**2)*Cr1*gk[0]*R1))/w0)
# print(f'M01 is {round(M01*10**12,2)} pico-(units?)')

# # Get the last resonator values
# Lnp1 = L0 # Ln+1 is 100 nH
# Crn = Cr1 # Let Crn be 100 pF
# Lrn = (1 + (w_prime*Lnp1*r/(gk[n-1]*Rn)))/(Crn*(w0**2))
# print(f'Lnp1 is {round(Lnp1*(10**9),2)} nH, Crn is {round(Crn*10**12,2)}, Lrn is {round(Lrn*10**9,2)} nH')

# # Get impedance of last impedance inverter
# Mnp1 = (np.sqrt((w_prime*r*(Rn**2 + (w0**2)*(Lnp1**2)))/((w0**2)*Crn*gk[n-1]*Rn))/w0)
# print(f'Mnp1 is {round(Mnp1*10**12,2)} pico-(units?)')

# # Get intermediate impedance inverter values
# Mjk = []
# for j in range(0,len(gk)-1, 1):
#     k = j + 1
#     coefficient = (w_prime * np.sqrt((Lrn**2)/(gk[j]*gk[k])))/(w0)
#     Mjk.append(coefficient)


# Ls = []
# Cs = []
# Ms = []

# Ls.append(L0 - M01)
# Ls.append(Lr1 - M01 - Mjk[0])
# Ls.append(Lrn - Mjk[0] - Mjk[1])
# Ls.append(Lnp1 - Mnp1)

# Cs.append(Cr1)
# Cs.append(Crn)
# Cs.append(Crn)

# Ms.append(M01)
# Ms.append(Mjk[0])
# Ms.append(Mjk[1])
# Ms.append(Mnp1)

# print('\n')
# print(f'Ls: {Ls}')
# print(f'Cs: {Cs}')
# print(f'Ms: {Ms}')


# Xl = w0*Ms[1]
# C = 1/w0*Xl
# print(C)
