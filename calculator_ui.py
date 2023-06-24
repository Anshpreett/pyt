import streamlit as st

st.title("Calculator for basic operations")

st.write("   ")
num1 = st.number_input(label="Enter first number")
num2 = st.number_input(label="Enter second number")
st.write("Operation")

operation = st.radio("select an operation to perform:",("Add","Subtract","Multiply","Divide","Power","Max","Min"))

ans=0

def calculate():
    if operation=="Add":
        ans= num1+num2
    elif operation=="Subtract":
        ans= num1-num2
    elif operation=="Multiply":
        ans= num1*num2
    elif operation=="Divide":
        ans= num1/num2
    elif operation=="Power":
        ans= num1**num2
    elif operation=="Max":
        if num1>num2:
            ans= num1
        else:
            ans= num2
    elif operation=="Min":
        if num1<num2:
            ans= num1
        else:
            ans= num2
    
    st.success(f"Answer={ans}")

if st.button("Calculater result"):
    calculate()

# streamlit run file name