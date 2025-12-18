import streamlit as st
st.title("my first project")
ime=st.text_input("what is your name")
if ime :
  st.write(f"hello {ime}")

