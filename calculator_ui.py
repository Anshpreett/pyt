import streamlit as st

fnum=st.number_input("Enter value",min_value=0,value=50)
snum=st.number_input("Enter value",min_value=0,value=50)

options=["Add","Sub","Mul","Div"]
choice=st.radio("Select an operation",options,horizontal=True)

button=st.button("CALCULATE")

if button:
    if choice==options[0]:
        result=fnum+snum
    elif choice==options[1]:
        result=fnum-snum
    elif choice==options[2]:
        result=fnum*snum
    elif choice==options[3]:
        result=fnum/snum
    st.success(f"Result is {result}")