import yaml

def load_data(file_path):
    """Load data from a YAML file."""
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def display_students(students):
    """Display all students."""
    print("\nAll Students:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}, GPA: {student['gpa']}")

def filter_students_by_gpa(students, min_gpa):
    """Filter and display students by minimum GPA."""
    filtered_students = [s for s in students if s['gpa'] >= min_gpa]

    print(f"\nStudents with GPA >= {min_gpa}:")
    if filtered_students:
        for student in filtered_students:
            print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}, GPA: {student['gpa']}")
    else:
        print("No students found.")

def main():
    # Load data from YAML file
    data = load_data('students.yaml')
    students = data['students']

    # Display all students
    display_students(students)

    # Filter students by GPA
    min_gpa = float(input("\nEnter minimum GPA to filter students: "))
    filter_students_by_gpa(students, min_gpa)

if __name__ == "__main__":
    main()
