import streamlit as st


st.image('./header.png')
st.header("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.subheader("Agree if you're ready to learn some Python")
if (st.checkbox('I agree')):
    st.write('''The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.  
    In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.''')
    st.markdown('''# **1. Walrus operator**  
    The **`Walrus` or `:=`** operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.  
    > Example  
    >  
    If we want to check and print the length of a list:''')
    code1 = '''Mylist = [1,2,3] 
            if(l := len(mylist > 2))
            print(l)'''
    st.code(code1, language='python')
    st.markdown('''> Output
    \>''')
    code2 = '''3'''
    st.code(code2, language='python')

