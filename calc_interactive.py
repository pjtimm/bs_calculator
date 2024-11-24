import streamlit as st
from calculations import *


st.title("Black Scholes Calculator")

# Sidebar 
with st.sidebar:
    st.header("Enter your Parameters \U0001F9EE", divider="blue")
    s = st.number_input("Current Asset Price :",0.00001, value = 100. ,step=1.)
    k = st.number_input("Strike Price :",0.00001, value = 200. ,step=1.)
    r = st.number_input("Interest Rate :",0.00001, value = 0.05 ,step=0.01)
    vol = st.number_input("Volatility \u03C3 :",0.00001, value = 0.3, step=0.01)
    t = st.number_input("Time to Maturity (in years) :",0.00001, value = 0.75, step=0.01)

call_value = call_value(s,k,r,vol,t)
put_value = put_value(s,k,r,vol,t)


# Create two columns for layout
col1, col2 = st.columns(2)

custom_css = """
    <style>
        /* Ensure proper contrast and visibility in dark mode */
        .call-box {
            font-size: 30px; 
            color: white;
            background-color: #4CAF50; 
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Add subtle shadow for better visibility */
        }
        .put-box {
            font-size: 30px; 
            color: white;
            background-color: #FF5733;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Add subtle shadow for better visibility */
        }
    </style>
"""

# Inject custom CSS into Streamlit
st.markdown(custom_css, unsafe_allow_html=True)

# Place the call and put values inside colored boxes in the columns
with col1:
    st.markdown(f'<div class="call-box">Call Value: ${call_value}</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="put-box">Put Value: ${put_value}</div>', unsafe_allow_html=True)



st.subheader("How does the spot price affect the option?",divider="grey")

(start,end) = st.slider("Choose a range for the spot prices", value = (0.,k*2))

fig, ax = assetprice_change_plot(start,end,k,r,vol,t)

st.pyplot(fig)