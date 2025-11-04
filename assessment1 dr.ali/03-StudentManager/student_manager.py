from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Load student data
def load_students():
    students = []
    try:
        with open("studentMarks.txt", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                parts = line.strip().split(",")
                code = parts[0].strip()
                name = parts[1].strip()
                coursework = list(map(int, parts[2:5]))
                exam = int(parts[5].strip())
                total_coursework = sum(coursework)
                overall = (total_coursework + exam) / 160 * 100
                if overall >= 70: grade = 'A'
                elif overall >= 60: grade = 'B'
                elif overall >= 50: grade = 'C'
                elif overall >= 40: grade = 'D'
                else: grade = 'F'
                students.append({
                    "code": code, "name": name, "coursework": total_coursework,
                    "exam": exam, "overall": overall, "grade": grade
                })
    except FileNotFoundError:
        messagebox.showerror("Error", "studentMarks.txt not found!")
    return students

students = load_students()

# GUI setup
root = Tk()
root.title("Student Manager")
root.geometry("700x400")
root.configure(bg="#f0f2f5")

# Title
Label(root, text="Student Manager", font=("Arial", 18, "bold"), bg="#f0f2f5").pack(pady=10)

# Frame for buttons
btn_frame = Frame(root, bg="#f0f2f5")
btn_frame.pack(pady=10)

def display_student(s):
    text_area.config(state=NORMAL)
    text_area.delete("1.0", END)
    text_area.insert(END, f"Name: {s['name']}\n")
    text_area.insert(END, f"Number: {s['code']}\n")
    text_area.insert(END, f"Coursework Total: {s['coursework']}\n")
    text_area.insert(END, f"Exam Mark: {s['exam']}\n")
    text_area.insert(END, f"Overall Percentage: {s['overall']:.2f}%\n")
    text_area.insert(END, f"Grade: {s['grade']}\n")
    text_area.config(state=DISABLED)

def view_all():
    text_area.config(state=NORMAL)
    text_area.delete("1.0", END)
    for s in students:
        display_student(s)
        text_area.insert(END, "-"*50 + "\n")
    text_area.config(state=DISABLED)

def show_highest():
    highest = max(students, key=lambda x: x["overall"])
    display_student(highest)

def show_lowest():
    lowest = min(students, key=lambda x: x["overall"])
    display_student(lowest)

Button(btn_frame, text="View All Student Records", width=25, command=view_all).grid(row=0, column=0, padx=5)
Button(btn_frame, text="Show Highest Score", width=20, command=show_highest).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Show Lowest Score", width=20, command=show_lowest).grid(row=0, column=2, padx=5)

# Frame for individual student
ind_frame = Frame(root, bg="#f0f2f5")
ind_frame.pack(pady=10)

Label(ind_frame, text="View Individual Student Record:", bg="#f0f2f5").grid(row=0, column=0, padx=5)
student_names = [f"{s['name']} ({s['code']})" for s in students]
combo = ttk.Combobox(ind_frame, values=student_names, width=40)
combo.grid(row=0, column=1, padx=5)

def view_individual():
    selected = combo.get()
    if not selected:
        messagebox.showinfo("Info", "Please select a student")
        return
    code = selected.split("(")[-1].strip(")")
    s = next((x for x in students if x["code"] == code), None)
    if s:
        display_student(s)

Button(ind_frame, text="View Record", command=view_individual).grid(row=0, column=2, padx=5)

# Text area for output
text_area = Text(root, width=80, height=12, state=DISABLED, font=("Arial", 12))
text_area.pack(pady=10)

root.mainloop()
