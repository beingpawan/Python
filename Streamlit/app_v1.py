
import streamlit as st

st.title("My first app")
st.write("I'm in College")

hours = st.slider(
    "Hours Studied",
    0.0,
    10.0,
    5.0,
    step=0.1
)

st.write(f"Hours studied: {hours}")
