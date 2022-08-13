import streamlit as st

output = '''> Output  '''
st.image('./header.png')
st.header("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.subheader("Agree if you're ready to learn some Python")
if (st.checkbox('I agree')):
    st.write('''The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.  
    In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.''')
    #Subtitulo Nro. 1
    st.markdown('''### **1. Walrus operator**  
The **`Walrus` or `:=`** operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.  
> Example  
If we want to check and print the length of a list:''')
    code1 = '''Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)'''
    st.code(code1, language='python')
    st.write(output)
    code2 = '''3'''
    st.code(code2, language='python')
    # Subitulo Nro. 2
    st.markdown('''### **2. Splitting a string**  
If you want to split the components of a string into a list you can do
that easily using the split() function in python. This will make the
string operations a lot easier!  
> Example  ''')
    code3 = '''string = “hello world”
string.split()'''
    st.code(code3, language='python')
    st.write(output)
    code4= '''[‘hello’, ‘world’]'''
    st.code(code4, language='python')
    # Subtitulo Nro. 3
    st.markdown('''### **3. Reversing a string**  
If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.  
> Example  ''')
    code5 = '''str=”hello world!”
a=str[::-1]
print(a)'''
    st.code(code5, language='python')
    st.write(output)
    code6 = '''!dlrow olleh'''
    st.code(code2, language='python')
    #Subtitulo Nro. 4
    st.markdown('''### **4. Merging two dictionaries**  
This amazing trick will help you merge two dictionaries with just 1 line of
code. We just need to use ** in front of the name of the two
dictionaries like below two merge them into a single dictionary:  
> Example  ''')
    code5 = '''d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)'''
    st.code(code5, language='python')
    st.write(output)
    code6 = '''{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}'''
    st.code(code6, language='python')
    #Subtitulo Nro. 5
    st.markdown('''### **5. The zip() function**  
The **zip()** function in python can make your life a lot easier when working with
lists and dictionaries. It is used to combine several lists of the same
length.  
> Example  ''')
    code7 = '''colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)'''
    st.code(code7, language='python')
    st.write(output)
    code8 = '''red appleyellow bananagreen mango'''
    st.code(code8, language='python')