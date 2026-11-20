import streamlit as st
import pandas as pd

# --------------------------------------------------
# 1. Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# 2. Application Header
# --------------------------------------------------

st.title("🎓 Student Grade Manager")
st.write("Manage students, marks, and grades easily.")

st.divider()

# --------------------------------------------------
# 3. Initialize Student Data
# --------------------------------------------------

if "students" not in st.session_state:
    st.session_state.students = []

# --------------------------------------------------
# 4. Grade Calculation Function
# --------------------------------------------------

def get_grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 80:
        return "B"

    elif mark >= 70:
        return "C"

    elif mark >= 60:
        return "D"

    else:
        return "E"

# --------------------------------------------------
# 5. Add Student Form
# --------------------------------------------------

st.subheader("➕ Add Student")

with st.form("add_student_form"):

    student_name = st.text_input("Student Name")

    student_mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submitted = st.form_submit_button("Add Student")

    if submitted:

        if student_name.strip() == "":
            st.error("Please enter the student name.")

        else:

            student = {
                "Name": student_name.strip(),
                "Mark": int(student_mark),
                "Grade": get_grade(student_mark)
            }

            st.session_state.students.append(student)

            st.success(f"{student_name} added successfully!")

# --------------------------------------------------
# 6. Display Student Records
# --------------------------------------------------

if st.session_state.students:

    st.divider()

    st.subheader("📋 Student Records")

    # Convert student list into DataFrame
    df = pd.DataFrame(st.session_state.students)

    # Display student table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # 7. Class Statistics
    # --------------------------------------------------

    marks = [student["Mark"] for student in st.session_state.students]

    average_mark = sum(marks) / len(marks)

    highest_mark = max(marks)

    lowest_mark = min(marks)

    st.divider()

    st.subheader("📊 Class Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Class Average",
            value=f"{average_mark:.2f}"
        )

    with col2:
        st.metric(
            label="Highest Mark",
            value=highest_mark
        )

    with col3:
        st.metric(
            label="Lowest Mark",
            value=lowest_mark
        )

# --------------------------------------------------
# 8. Empty State
# --------------------------------------------------

else:

    st.info("No students added yet. Add your first student above!")