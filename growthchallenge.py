import streamlit as st
import io
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Streamlit App Title
st.title("Interactive Learning and Conversion Tool")

st.write("Explore different mathematical functions, Python coding exercises, and file format conversions!")

# Initialize session state for category selection
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# Main Category Selection
category = st.sidebar.selectbox("Choose a subject:", ["Convert CSV to XLSX", "Mathematics", "Python Programming"], index=0)

# Reset quiz state when switching categories
if category != st.session_state.selected_category:
    st.session_state.selected_category = category
    st.session_state.quiz_index = 0
    st.session_state.correct_answers = 0

if category == "Convert CSV to XLSX":
    st.title("Growth Mindset Challenge")
    st.write("### What is the Growth Mindset Challenge?")
    st.write("The Growth Mindset Challenge is designed to encourage continuous learning and improvement. By tackling different tasks, you develop a mindset focused on persistence, problem-solving, and adaptability.")
    st.write("### Convert CSV to XLSX")
    st.write("Upload your CSV file and convert it to an Excel XLSX format.")
    
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"]) if category == 'Convert CSV to XLSX' else None
    
    if category == 'Convert CSV to XLSX' and uploaded_file is not None:
        st.success("File uploaded successfully!")
        if st.button("Convert to XLSX"):
            st.write("Processing file...")
            df = pd.read_csv(uploaded_file)
            output = io.BytesIO()
            df.to_excel(output, index=False, engine='xlsxwriter')
            output.seek(0)
            st.download_button("Download XLSX", data=output, file_name="converted.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

elif category == "Mathematics":
    # User Input for Custom Equation
    st.write("### Graph Plotter")
    equation = st.text_input("Enter a mathematical equation in terms of x (e.g., sin(x), x**2 + 3*x - 5)", "x**2")
    x_min, x_max = st.slider("Select x-axis range:", -10.0, 10.0, (-5.0, 5.0))
    
    # Generate x values
    x = np.linspace(x_min, x_max, 400)
    
    try:
        y = eval(equation, {"x": x, "np": np})
        fig, ax = plt.subplots()
        ax.plot(x, y, label=f"y = {equation}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        ax.grid()
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Invalid equation: {e}")

elif category == "Python Programming":
    st.write("### Python Fundamentals")
    fundamentals = {
        "Variables and Data Types": "Python supports different data types like int, float, string, and boolean.",
        "Conditional Statements": "if, elif, else statements are used for decision making.",
        "Loops": "for and while loops allow repetition of code blocks.",
        "Functions": "Defined using def keyword to make code reusable.",
        "Lists and Tuples": "Lists are mutable, tuples are immutable collections of elements.",
        "Dictionaries": "Key-value pairs used to store related data.",
        "Classes and Objects": "Python supports object-oriented programming through classes.",
    }

    topic = st.selectbox("Select a topic to learn:", list(fundamentals.keys()))
    st.write(f"### {topic}")
    st.write(fundamentals[topic])

    # Python Quiz Section
    st.write("### Python Quiz")
    quiz_questions = [
        ("What is the correct syntax to define a function in Python?", ["def functionName():", "function functionName():", "define functionName():", "func functionName() {}"], "def functionName():"),
        ("Which data type is mutable?", ["Tuple", "List", "String", "Integer"], "List"),
        ("What keyword is used to create a loop?", ["for", "while", "loop", "repeat"], "for"),
        ("How do you add an element to a list?", ["list.add()", "list.append()", "list.insert()", "list.push()"], "list.append()"),
        ("Which symbol is used for comments in Python?", ["//", "#", "/* */", "--"], "#"),
        ("What does the len() function do?", ["Returns list length", "Adds an element", "Sorts a list", "Removes an element"], "Returns list length"),
        ("Which keyword is used to define a class?", ["class", "Class", "define", "cls"], "class"),
        ("What does the input() function do?", ["Takes user input", "Prints text", "Returns a random number", "Reads a file"], "Takes user input"),
        ("Which module is used for mathematical operations?", ["math", "random", "numpy", "os"], "math"),
        ("What is the output of print(type(10))?", ["int", "float", "string", "boolean"], "int")
    ]

    if st.session_state.quiz_index < len(quiz_questions):
        question, options, correct_answer = quiz_questions[st.session_state.quiz_index]
        answer = st.radio(question, options)
        if st.button("Next"):
            if answer == correct_answer:
                st.session_state.correct_answers += 1
            st.session_state.quiz_index += 1
            st.rerun()
    else:
        st.write(f"### Quiz Completed! You got {st.session_state.correct_answers} out of {len(quiz_questions)} correct.")
        if st.button("Restart Quiz"):
            st.session_state.quiz_index = 0
            st.session_state.correct_answers = 0
            st.rerun()

st.write("Modify the parameters and explore different subjects interactively!")
