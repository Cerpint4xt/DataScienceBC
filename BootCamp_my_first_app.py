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
    st.code(code6, language='python')
    #Subtitulo Nro. 4
    st.markdown('''### **4. Merging two dictionaries**  
This amazing trick will help you merge two dictionaries with just 1 line of
code. We just need to use ** in front of the name of the two
dictionaries like below two merge them into a single dictionary:  
> Example  ''')
    code7 = '''d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)'''
    st.code(code7, language='python')
    st.write(output)
    code8 = '''{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}'''
    st.code(code8, language='python')
    #Subtitulo Nro. 5
    st.markdown('''### **5. The zip() function**  
The **zip()** function in python can make your life a lot easier when working with
lists and dictionaries. It is used to combine several lists of the same
length.  
> Example  ''')
    code9 = '''colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)'''
    st.code(code9, language='python')
    st.write(output)
    code10 = '''red apple
yellow banana
green mango'''
    st.code(code10, language='python')
    st.write('''The zip() function can also be used for combining two lists into a
dictionary. This method can be really helpful while grouping data from
the list.  
> Example  ''')
    code11 = '''students = [“Rajesh”, “kumar”, “Kriti”]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)'''
    st.code(code11, language='python')
    st.write(output)
    code12 = '''{‘Rajesh’: 87, ‘kumar’: 90, ‘Kriti’: 88}'''
    st.code(code12, language='python')
    #Subtitulo Nro. 6
    st.markdown('''### **6. Assigning multiple list values to a variable**  
If you want to assign some specific values of a list to a variable and all
 the remaining values to another variable in a list format, you can use
the following technique:   
> Example  ''')
    code13 = '''mylist = [1,2,3,4,5]
a,*b = mylist
print(f”a =”,a)
print(f”b =”,b)'''
    st.code(code13, language='python')
    st.write(output)
    code14 = '''a = 1
b = [2, 3, 4, 5]'''
    st.code(code14, language='python')
    st.write('''This process is also called list unpacking and you can apply this method for more than 2 variables also!  ''')
    #Subtitulo Nro. 7
    st.markdown('''### **7. Remove duplicate list items**  
Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the **set()** function.  
> Example  ''')
    code15 = '''mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist)'''
    st.code(code15, language='python')
    st.write(output)
    code16 = '''{1, 2, 3, 4, 5, 6, 7, 8, 9}'''
    st.code(code16, language='python')
    #Subtitulo Nro. 8
    st.markdown('''### **8. Lambda function**  
If you need a function that is not very complicated, it can be done easily in one line using **lambda**. They are also called anonymous functions and are used heavily in data science and web development.  
> Example  
Let’s say you want to write a function to multiply two numbers. Instead of
writing a conventional function, you can do that in one line using :  ''')
    code17 = '''mul = lambda a,b: a*b
mul(5,6)'''
    st.code(code17, language='python')
    st.write(output)
    code18 = '''30'''
    st.code(code18, language='python')
    #Subtitulo Nro. 9
    st.markdown('''### **9. Swapping variable value**  
One of the first programs that we learn while learning about variables is
swapping the values of two variables. In python you can achieve that
with one line of code:    
> Example  ''')
    code19 = '''a = 100
b = 200
a,b = b,a  
print(f’a = ‘,a)  
print(f’b = ‘,b)'''
    st.code(code19, language='python')
    st.write(output)
    code20 = '''a = 200
b = 100'''
    st.code(code20, language='python')
    #Subtitulo Nro. 10
    st.markdown('''### **10. Use a password in your code**  
This python trick is amazing for securing your code with a password. We will use the **getpass() function** from the **library getpass** which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool!     
> Example  ''')
    code21 = '''from getpass import getpass
password = getpass(“password: “)
if password == “abcd”:    
    print(“welcome strnger!”)
else:    
    print(“wrong password”)'''
    st.code(code21, language='python')
    st.write(output)
    code22 = '''password: **** [abcd]
**Welcome stranger!**
Password: **** [abdc]
Wrong password'''
    st.code(code22, language='python')
    