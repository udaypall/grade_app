import streamlit as st


# -----------------------------
# Grade calculation
# -----------------------------
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


# -----------------------------
# Page title
# -----------------------------
st.title("Student Grade Manager")


# -----------------------------
# Session State
# -----------------------------
if "students" not in st.session_state:
    st.session_state.students = []


# -----------------------------
# Add Student Form
# -----------------------------
with st.form("add_student"):

    name = st.text_input("Name")

    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        step=1
    )

    submitted = st.form_submit_button("Add")


# -----------------------------
# Add student
# -----------------------------
if submitted:

    if name.strip() == "":
        st.error("Please enter the student name.")

    else:
        grade = get_grade(mark)

        student = {
            "Name": name,
            "Mark": mark,
            "Grade": grade
        }

        st.session_state.students.append(student)

        st.success(f"{name} added successfully!")


# -----------------------------
# Display students
# -----------------------------
if st.session_state.students:

    st.subheader("Student Results")

    st.table(st.session_state.students)


    # -----------------------------
    # Class calculations
    # -----------------------------
    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)


    # -----------------------------
    # Display metrics
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average", f"{average:.1f}")

    with col2:
        st.metric("Highest", highest)

    with col3:
        st.metric("Lowest", lowest)

else:

    st.info("No students added yet. Add a student using the form above.")