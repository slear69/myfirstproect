import streamlit as st
st.title("my first project")
ime=st.texti_input("what is your name")
if ime :
  st.write(f"hello {ime}")

