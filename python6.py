import tkinter as tk
from tkinter import ttk
from datetime import date
import csv
from tkinter import messagebox
from tkinter import filedialog

class Person:
    def __init__(self, id, first_name, last_name, date_of_birth, contact_number, email,street,city):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.contact_number = contact_number
        self.email = email
        self.street = street
        self.city = city

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Student(Person):
    def __init__(self, student_id, id, street, city, grade, parent_first_name, parent_last_name, **kwargs):
        super().__init__(id=id, street=street, city=city, **kwargs)
        self.student_id = student_id
        self.grade = grade
        self.parent_first_name = parent_first_name
        self.parent_last_name = parent_last_name
        self.parent_street = street
        self.parent_city = city
        
    def get_student_details(self):
        return f"Student ID: {self.student_id}, Grade: {self.grade}, " \
               f"Name: {self.first_name} {self.last_name}, " \
               f"Parent: {self.parent_first_name} {self.parent_last_name}"


class Parent(Person):
    def __init__(self, student_id, is_primary_guardian, **kwargs):
        super().__init__(**kwargs)
        self.parent_id = student_id
        self.is_primary_guardian = is_primary_guardian

    def get_parent_details(self):
        return f"Parent ID: {self.parent_id}, Guardian: {self.is_guardian}, Name: {self.get_full_name()}"

class Staff(Person):
    def __init__(self, staff_id, role, salary, **kwargs):
        super().__init__(**kwargs)
        self.staff_id = staff_id
        self.role = role
        self.salary = salary

    def get_staff_details(self):
        return f"Staff ID: {self.staff_id}, Role: {self.role}, Salary: ${self.salary}, Name: {self.get_full_name()}"

class Classroom:
    def __init__(self, classroom_id, class_name, teacher, students):
        self.classroom_id = classroom_id
        self.class_name = class_name
        self.teacher = teacher
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def get_class_details(self):
        student_details = "\n".join([student.get_student_details() for student in self.students])
        return f"Classroom ID: {self.classroom_id}, Class Name: {self.class_name}, Teacher: {self.teacher.get_full_name()}\nStudents:\n{student_details}"

class School:



    def __init__(self, school_id, school_name, address, classrooms):
        self.school_id = school_id
        self.school_name = school_name
        self.address = address
        self.classrooms = classrooms

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def get_school_details(self):
        classroom_details = "\n".join([classroom.get_class_details() for classroom in self.classrooms])
        return f"School ID: {self.school_id}, School Name: {self.school_name}, Address: {self.address}\nClassrooms:\n{classroom_details}"

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SkyPy")

        # Create Notebook (Tabs)
        self.notebook = ttk.Notebook(root)

        # Create Student Tab
        self.tab_student = ttk.Frame(self.notebook)
        self.create_student_tab()

        #export button
        self.create_export_button()  

        # Add Student Tab to Notebook
        self.notebook.add(self.tab_student, text="Student Information")
        self.notebook.pack(expand=1, fill="both")

        # List to collect students
        self.students_list = []

    def create_student_tab(self):
        self.label_student_id = ttk.Label(self.tab_student, text="Student ID:")
        self.entry_student_id = ttk.Entry(self.tab_student)

        self.label_student_first_name = ttk.Label(self.tab_student, text="First Name:")
        self.entry_student_first_name = ttk.Entry(self.tab_student)

        self.label_student_last_name = ttk.Label(self.tab_student, text="Last Name:")
        self.entry_student_last_name = ttk.Entry(self.tab_student)

        self.label_student_dob = ttk.Label(self.tab_student, text="Date of Birth (YYYY-MM-DD):")
        self.entry_student_dob = ttk.Entry(self.tab_student)

        self.label_student_contact = ttk.Label(self.tab_student, text="Contact Number:")
        self.entry_student_contact = ttk.Entry(self.tab_student)

        self.label_student_email = ttk.Label(self.tab_student, text="Email:")
        self.entry_student_email = ttk.Entry(self.tab_student)

        self.label_student_grade = ttk.Label(self.tab_student, text="Grade:")
        self.entry_student_grade = ttk.Entry(self.tab_student)

        self.button_create_student = ttk.Button(self.tab_student, text="Create Student", command=self.create_student)

        self.text_display_student = tk.Text(self.tab_student, height=10, width=60, wrap=tk.WORD)
        self.text_display_student.insert(tk.END, "Student details will be displayed here.")

        self.label_student_id.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_student_id.grid(row=0, column=0, padx=(50,5), pady=5)

        self.label_student_first_name.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_student_first_name.grid(row=1, column=0, padx=(50,5), pady=5)

        self.label_student_last_name.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_student_last_name.grid(row=2, column=0, padx=(50,5), pady=5)

        self.label_student_dob.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_student_dob.grid(row=3, column=0, padx=(50,5), pady=5)

        self.label_student_contact.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_student_contact.grid(row=4, column=0, padx=(50,5), pady=5)

        self.label_student_email.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_student_email.grid(row=5, column=0, padx=(50,5), pady=5)

        self.label_student_grade.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_student_grade.grid(row=6, column=0, padx=(50,5), pady=5)

        self.button_create_student.grid(row=7, column=0, columnspan=2, pady=10)

        self.text_display_student.grid(row=8, column=0, columnspan=2, padx=5, pady=5)


                ################ Parent Information ###############

    #parent first name
        self.label_parent_first_name = ttk.Label(self.tab_student, text="Parent's First Name:")
        self.entry_parent_first_name = ttk.Entry(self.tab_student)      
        self.label_parent_first_name.grid(row=1, column=2, sticky=tk.E, padx=5, pady=5)
        self.entry_parent_first_name.grid(row=1, column=3, padx=5, pady=5)

    #parent last name
        self.label_parent_last_name = ttk.Label(self.tab_student, text="Parent's Last Name:")
        self.entry_parent_last_name = ttk.Entry(self.tab_student)
        self.label_parent_last_name.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)
        self.entry_parent_last_name.grid(row=2, column=2, padx=5, pady=5)
        
    #parent street
        self.label_parent_street = ttk.Label(self.tab_student, text="Street Address:")
        self.entry_parent_street = ttk.Entry(self.tab_student)
        self.label_parent_street.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)
        self.entry_parent_street.grid(row=3, column=2, padx=5, pady=5)

    #parent city
        self.label_parent_city = ttk.Label(self.tab_student, text="City:")
        self.entry_parent_city = ttk.Entry(self.tab_student)
        self.label_parent_city.grid(row=4, column=1, sticky=tk.E, padx=5, pady=5)
        self.entry_parent_city.grid(row=4, column=2, padx=5, pady=5) 

    #primary guardian    

        self.primary_guardian_var = tk.BooleanVar()
        self.checkbox_primary_guardian = ttk.Checkbutton(self.tab_student, text="Primary Guardian",
                                                     variable=self.primary_guardian_var)
        self.checkbox_primary_guardian.grid(row=5, column=2, pady=5)

    #if not custodial
        self.label_custodial = ttk.Label(self.tab_student, text="Name of Primary:")
        self.entry_custodial = ttk.Entry(self.tab_student) 
        self.label_custodial.grid(row=6, column=1, sticky=tk.E, padx=5, pady=5)
        self.entry_custodial.grid(row=6, column=2, padx=5, pady=5)       
        # Bind the custodial parent entry field to the checkbox state
        self.checkbox_primary_guardian.configure(command=self.toggle_custodial_entry)
        
                ################ Parent Information ###############

    def create_parent(self):
        
            #Get parent info from user input
            parent_first_name = self.entry_parent_first_name.get()
            parent_last_name = self.entry_parent_last_name.get()
            parent_street = self.entry_parent_street.get()
            parent_city = self.entry_parent_city.get()
        
            #Create Parent instance
            parent = Parent(parent_first_name=parent_first_name,parent_last_name=parent_last_name, parent_street = parent_street, parent_city = parent_city)

            #Add parent to list
            self.students_list.append(parent)

            #clear input boxes
            #self.clear_parent_input()
        
            #Display parent details
            self.display_student_details()

    #checkbox toggle        
    def toggle_custodial_entry(self):
        if self.primary_guardian_var.get():
            # If checkbox is checked, disable the entry field
            self.entry_custodial.config(state=tk.DISABLED)
            self.entry_custodial.delete(0, tk.END)  # Clear the entry field
        else:
        # If checkbox is unchecked, enable the entry field
            self.entry_custodial.config(state=tk.NORMAL)

    def create_student(self):
        try:
            # Get student details from user input
            student_id = int(self.entry_student_id.get())
            student_first_name = self.entry_student_first_name.get()
            student_last_name = self.entry_student_last_name.get()
            student_dob = date.fromisoformat(self.entry_student_dob.get())
            student_contact = self.entry_student_contact.get()
            student_email = self.entry_student_email.get()
            student_grade = int(self.entry_student_grade.get())
            parent_first_name = self.entry_parent_first_name.get()
            parent_last_name = self.entry_parent_last_name.get()
            parent_street = self.entry_parent_street.get()
            parent_city = self.entry_parent_city.get()

            # Create Student instance
            student = Student(student_id=student_id, grade=student_grade,
                              id=student_id, first_name=student_first_name, last_name=student_last_name,
                              date_of_birth=student_dob, contact_number=student_contact, email=student_email,  parent_first_name=parent_first_name, 
                              parent_last_name=parent_last_name,street = parent_street, city=parent_city)

            # Add student to the list
            self.students_list.append(student)

            # Clear input boxes
            self.clear_student_input()

            # Display student details
            self.display_student_details()



        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input. Please enter correct values for Student ID, Date of Birth, and Grade.")

    def create_export_button(self):
        self.button_export_csv = ttk.Button(self.tab_student, text="Export to CSV", command=self.export_to_csv)
        self.button_export_csv.grid(row=9, column=0, columnspan=2, pady=10)

    def export_to_csv(self):
        try:
            filename = tk.filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save CSV file")
            if filename:
                with open(filename, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Student ID", "First Name", "Last Name", "Date of Birth", "Contact Number", "Email", "Grade", "Parent First Name", "Parent Last Name", "City", "Street"])
                    for student in self.students_list:
                        writer.writerow([
                            student.student_id,
                            student.first_name,
                            student.last_name,
                            student.date_of_birth,
                            student.contact_number,
                            student.email,
                            student.grade,
                            student.parent_first_name,
                            student.parent_last_name,
                            student.city,
                            student.street

                        ])
                tk.messagebox.showinfo("Export Successful", "Student information exported to CSV successfully.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred during export: {str(e)}")

    def clear_student_input(self):
        # Clear all input boxes
        self.entry_student_id.delete(0, tk.END)
        self.entry_student_first_name.delete(0, tk.END)
        self.entry_student_last_name.delete(0, tk.END)
        self.entry_student_dob.delete(0, tk.END)
        self.entry_student_contact.delete(0, tk.END)
        self.entry_student_email.delete(0, tk.END)
        self.entry_student_grade.delete(0, tk.END)
        self.entry_parent_first_name.delete(0, tk.END)
        self.entry_parent_last_name.delete(0, tk.END)
        self.entry_parent_city.delete(0, tk.END)
        self.entry_parent_street.delete(0, tk.END)


    def display_student_details(self):
        # Display all students with numbering
        details = ""
        for i, student in enumerate(self.students_list, start=1):
            details += f"{i}. {student.get_student_details()}\n"

        self.text_display_student.delete(1.0, tk.END)
        self.text_display_student.insert(tk.END, details)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()