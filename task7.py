# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

# Number of students
num_students = int(input("Enter the number of students: "))

for i in range(1, num_students + 1):
    # Get student marks and ensure they're within 0 to 100
    marks = int(input(f"Enter marks for student {i} (0-100): "))
    
    # Validate that marks are within the correct range
    if marks < 0 or marks > 100:
        print("Invalid input! Marks should be between 0 and 100.")
    else:
        # Determine grade based on marks
        if marks > 79:
            grade = "A"
        elif marks >= 60:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "E"
        
        # Output the grade
        print(f"Grade for student {i}: {grade}")
