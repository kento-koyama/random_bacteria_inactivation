import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Monte Carlo simulation for bacterial inactivation')
st.write("Simulation")

Mean_N0 = st.number_input('N0',value=100)
rep = st.number_input('Repetition',value=100)
param_b = st.number_input('Parameter b',value=1.000)
param_n = st.number_input('Parameter n',value=1.000)
st.write('N0 is', Mean_N0, 'Parameter b is ', param_b,'Parameter n is ', param_n)



fig, ax = plt.subplots()
for i in range(rep):
    N0 = np.random.poisson(Mean_N0)
    inactivation_time = (param_b/(np.log(10)**(1/param_n)))*np.random.weibull(param_n,N0)
    inactivation_time.sort()
    x = np.append(0,inactivation_time)
    y = np.arange(N0,-1,-1)
    ax.plot(x, np.log10(y), drawstyle='steps-post', zorder=1, label='')
ax.set_ylabel("Survival cell counts [$\log_{10}$CFU]", fontsize=16)
ax.set_xlabel('Inactivation time [h]', fontsize=16, color='k')
ax.tick_params(labelsize=16, direction='out')
st.pyplot(fig)
    
st.write('Reference')
st.write('Transforming kinetic model into a stochastic inactivation model: Statistical evaluation of stochastic inactivation of individual cells in a bacterial population')
