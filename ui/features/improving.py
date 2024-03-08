import streamlit as st

text = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Basics</title>
</head>
<body>
    <h2>Python Basics</h2>
    <p>Python is a versatile, easy-to-learn programming language that is widely used for a variety of tasks, including web development, data analysis, and machine learning.</p>
    <h3>Syntax</h3>
    <p>Python's syntax is simple and easy to read, making it a great choice for beginners. Here are a few key points about Python syntax:</p>
    <ul>
        <li>Python uses indentation to indicate blocks of code, rather than curly braces like some other languages.</li>
        <li>Python uses the colon (:) to separate statements in a compound statement (like an if statement or a for loop).</li>
        <li>Python does not have a type system, which means that you can assign any value to any variable without worrying about type compatibility.</li>
    </ul>
    <h3>Data Types</h3>
    <p>Python has a rich set of built-in data types, including strings, numbers, and lists. Here are a few of the most common data types:</p>
    <ul>
        <li><b>Strings</b> represent sequences of characters and can be enclosed in either single or double quotes.</li>
        <li><b>Numbers</b> include integers (whole numbers) and floating-point numbers (numbers with a decimal point). Integers are typically represented without a decimal point, while floating-point numbers are represented with a decimal point and a fractional part.</li>
        <li><b>Lists</b> are ordered collections of values that can be of any type. Lists are enclosed in square brackets ([]).</li>
    </ul>
    <h3>Control Flow</h3>
    <p>Python has a variety of control flow statements that allow you to control the execution of your program. Here are a few of the most common control flow statements:</p>
    <ul>
        <li><b>if</b> statements allow you to execute a block of code only if a certain condition is true.</li>
        <li><b>for</b> loops allow you to iterate over a sequence of values and execute a block of code for each value.</li>
        <li><b>while</b> loops allow you to execute a block of code repeatedly as long as a certain condition is true.</li>
    </ul>
    <h3>Conclusion</h3>
    <p>These are just a few of the basics of Python. There is much more to learn, but with a little practice, you'll be able to start writing Python programs in no time!</p>
    <p><b>Try it out:</b></p>
    <ol>
        <li>Open your favorite text editor or IDE.</li>
        <li>Type the following code:</li>
        <pre><code>
print("Hello, world!")
        </code></pre>
        <li>Save the file with a .py extension (for example, my_first_program.py).</li>
        <li>Run the program by typing the following command in your terminal or command prompt:</li>
        <pre><code>
python my_first_program.py
        </code></pre>
    </ol>
</body>
</html>
"""
def get_model_output():
    return "Hello World"
def improving_page():
    data = get_model_output()
    st.components.v1.html(text, height=1000, scrolling=True)