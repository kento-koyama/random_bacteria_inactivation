import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64

st.title('Monte Carlo simulation for bacterial inactivation')
st.write("## Simulation")

Mean_N0 = st.number_input('N0',value=100, min_value=1, max_value=10**3)
rep = st.number_input('Repetition',value=100, min_value=1, max_value=10**3)
param_b = st.number_input('Parameter b',value=1.000)
param_n = st.number_input('Parameter n',value=1.000)
st.write('N0 is', Mean_N0, 'Parameter b is ', param_b,'Parameter n is ', param_n)


box = []

fig, ax = plt.subplots()
for i in range(rep):
    N0 = np.random.poisson(Mean_N0)
    inactivation_time = (param_b/(np.log(10)**(1/param_n)))*np.random.weibull(param_n,N0)
    inactivation_time.sort()
    x = np.append(0,inactivation_time)
    y = np.arange(N0,-1,-1)
    ax.plot(x, np.log10(y), drawstyle='steps-post', zorder=1, label='')
    box.append(x)
ax.set_ylabel("Survival cell counts [$\log_{10}$CFU]", fontsize=14)
ax.set_xlabel('Inactivation time', fontsize=16, color='k')
ax.tick_params(labelsize=14, direction='out')
st.pyplot(fig)

df = pd.DataFrame(box)
event_str = np.array(range(0, df.shape[1], 1))
event_str = [str(n) for n in event_str]
event_str = ['event'+s for s in event_str]
rep_name = np.array(range(1, rep+1, 1))
rep_name = [str(n) for n in rep_name]
rep_name = ['rep'+s for s in rep_name]
df["rep"] = rep_name
df.set_index("rep",inplace=True)
df.columns = event_str
st.subheader('The simulation result')
st.dataframe(df)

csv = df.to_csv(index=True)  
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:application/octet-stream;base64,{b64}" download="result.csv">download</a>'
st.markdown(f"Download the result as a csv file {href}", unsafe_allow_html=True)
    
st.write('## Reference')
st.markdown('Hiura, S., Abe, H., Koyama, K., Koseki, S. Transforming kinetic model into a stochastic inactivation model: Statistical evaluation of stochastic inactivation of individual cells in a bacterial population,  2020, Food Microbiology, 91, 103508. [doi.org/10.1016/j.fm.2020.103508](https://doi.org/10.1016/j.fm.2020.103508)')
