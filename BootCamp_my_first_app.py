import streamlit as st


st.image('./header.png')
st.header("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.subheader("Agree if you're ready to learn some Python")
st.checkbox('I agree')

st.markdown('**1. Walrus operator**')

st.markdown('The **`Walrus` or `:=`** operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')
st.markdown('> Example')

st.markdown('>')
st.markdown('If we want to check and print the length of a list:')
st.code('Mylist = [1,2,3] > 2)')
st.code('if(l := len(mylist)')
st.code('print(l)')
st.markdown('> Output')
st.markdown('>')
