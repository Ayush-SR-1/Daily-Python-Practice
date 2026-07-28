import pickle
import os

Student_Record = "student_history.dat"

def load_students():
  
  if os.path.exists(Student_Record):
    with open(Student_Record, 'rb') as f:
      try:
        return pickle.load(f)
      except EOFError:
        return []
      
  return []

def save_student(students):
  
  with open(Student_Record, 'wb') as f:
    pickle.dump(students, f)

def add_student():
  
  students = load_students()
  
  Roll_Number = int(input("Enter your Roll Number: "))
  Name = input("Enter your Name: ")
  student_class = input("Enter the Class: ")
  Marks = float(input("Enter your total Marks: "))
  
  
  students.append({
    "Name": Name, 
    "Roll_Number": Roll_Number, 
    "Class": student_class, 
    'Marks': Marks
  })
  save_student(students)
  print(f"\nStudent {Name} has been added successfully")

def search_student():
  
  students = load_students()
  
  Roll_Number = int(input("Enter the roll number you want to search: "))
  for student in students:
    
    if student["Roll_Number"] == Roll_Number:
      print(f"Found -> Roll Number: {student["Roll_Number"]}, Student: {student["Name"]}, Class: {student["Class"]}, Marks: {student["Marks"]}")
      return
    
  print("No student found with the given roll number.")

def edit_record():
  
  students = load_students()
  
  Roll_Number = int(input("Enter the Roll Number: "))
  print()
  for student in students:
    
    if student["Roll_Number"] == Roll_Number:
      print("Choice the option you want to edit: ")
      print("1. Roll Number \n2. Name \n3. Class \n4. Marks\n")
      
      choice = int(input("Choice Between (1-4): "))
      print()
      
      if choice == 1:
        
        New_Roll_Number = int(input("Enter the New Roll Number: "))
        student["Roll_Number"] = New_Roll_Number
      
      elif choice == 2:
        
        New_Name = input("Enter the New Name: ")
        student["Name"] = New_Name
      
      elif choice == 3:
        
        New_Class = input("Enter the New Class: ")
        student["Class"] = New_Class
      
      elif choice == 4:
        
        New_Marks = int(input("Enter the new Marks: "))
        student["Marks"] = New_Marks
      
      else:
        print("Invalid input !! Enter the correct input between (1-4).")
        return
      
      save_student(students)
      print("Record Updated Successfully.")
      return
    
  print("No Student Found with the given roll number.")

def view_record():
  
  students = load_students()
  
  if not students:
    print("No student found.")
    return
  
  print("----------Student Lists----------")
  for student in students:
    print(f"Found -> Roll Number: {student["Roll_Number"]}, Student: {student["Name"]}, Class: {student["Class"]}, Marks: {student["Marks"]}")
  print("---------------------------------")

def remove_student():
  
  students = load_students()
  
  Roll_Number = int(input("Enter the Roll number to remove: "))
  for student in students:
    if student["Roll_Number"] == Roll_Number:
      students.remove(student)
      save_student(students)
      print(f"Student Removed -> Roll Number: {student["Roll_Number"]}, Student: {student["Name"]}, Class: {student["Class"]}, Marks: {student["Marks"]}")
      return
  
  print("No Student found for the given roll number.")

def main():
  
  while True:
      
    print("\n----------Student Record System----------\n")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Edit Record")
    print("4. View Records")
    print("5. Remove Student Record")
    print("6. Exit\n")
    
    choice = int(input("Choice option (1-6): "))
    print()
    
    if choice == 1:
      add_student()
    
    elif choice == 2:
      search_student()
    
    elif choice == 3:
      edit_record()
    
    elif choice == 4:
      view_record()
    
    elif choice == 5:
      remove_student()
    
    elif choice == 6:
      print("----------GoodBye----------\n")
      break
    
    else:
      print("Invalid Input !! Enter the correct option.")


if __name__ == "__main__":
  main()