import streamlit as st
import calculations

s = st.number_input("Current Asset Price :",0., value = 100.)
k = st.number_input("Strike Price :",0., value = 200.)
r = st.number_input("Interest Rate :",0., value = 0.05)
vol = st.number_input("Volatility \u03C3 :",0., value = 0.3)
t = st.number_input("Time to Maturity (in years) :",0., value = 0.75)

call_value = calculations.call_value(s,k,r,vol,t)
put_value = calculations.put_value(s,k,r,vol,t)

st.write(f"Call Value = {call_value}")
st.write(f"Put Value = {put_value}")