#STUDENT REPORT CARD GENERATOR
def assign_grade(average):
    if avg >= 90:
        grad = "A"
    elif avg >= 80:
        grad = "B"
    elif avg >= 70:
        grad = "C"
    elif avg >= 60:
        grad = "D"
    else:
        grad = "E"

#students scoring above 90 in any subject
def find_students_above_90(dictionary):
    subjects = ["ENGLISH", "HINDI", "MATHS", "SCIENCE", "SOCIAL SCIENCE"]
    for subject in subjects:
        print(f"\nSTUDENTS SCORING ABOVE 90 IN {subject}:")
        for i in dictionary:
            student_dict = dictionary[i]
            name = list(student_dict.keys())[0]
            details = student_dict[name]
            if details[subject] > 90:
                print(f"{name} scored {details[subject]} in {subject}")

#SUBJECT WISE TOPPER
def find_subject_topper(dictionary):
    subjects = ["ENGLISH", "HINDI", "MATHS", "SCIENCE", "SOCIAL SCIENCE"]
    for subject in subjects:
        toppers = sorted(dit.values(), key=lambda item: list(item.values())[0][f"{subject}"], reverse=True)
        for topper in toppers:
            name = list(topper.keys())[0]
            print(f"TOPPER IN {subject}:",name)
            break

def display_student_report(lst):
    rn=input("ENTER NAME OF THE STUDENT TO SEE REPORT CARD:")
    print(f"\nREPORT CARD OF {rn}")
    for item in lst:
        sd=item[1]          
        N = list(sd.keys())[0]  
        marks = sd[N]       
        if N == rn:  
            print(f"Name: {N}")
            print(f"English: {marks['ENGLISH']}")
            print(f"Hindi: {marks['HINDI']}")
            print(f"Maths: {marks['MATHS']}")
            print(f"Science: {marks['SCIENCE']}")
            print(f"Social Science: {marks['SOCIAL SCIENCE']}")
            print(f"Average Marks: {marks['AVERAGE']}")
            print(f"Grade: {marks['GRADE']}\n")
        else:
            print("STUDENT NOT FOUND")
while True:
    print("CHOOSE AN OPTION:")
    print("1. GENERATE REPORT CARD")
    print("2. ENTER DATA")
    print("3. SUBJECTWISE TOPPERS")
    print("4. STUDENTS SCORING ABOVE 90 IN ANY SUBJECT")
    print("5. EXIT")
    cnt=int(input("Enter your choice: "))
    if cnt == 2:
        dit={}
        lst={}
        n=int(input("Enter number of students:"))
        for i in range(1,n+1):
            print("STUDENT", i)
            # Input student details
            name=input("Enter student name:")
            print("ENTER MARKS")
            eng=int(input("ENGLISH->"))
            hin=int(input("HINDI->"))
            math=int(input("MATHS->"))
            sci=int(input("SCIENCE->"))
            sst=int(input("SOCIAL SCIENCE->"))

            # Calculate average and grade
            avg = (eng + hin + math + sci + sst) / 5
            avg = round(avg, 2)
            grad=assign_grade(avg)

            dit[i]={name:{"ENGLISH":eng,"HINDI":hin,"MATHS":math,"SCIENCE":sci,"SOCIAL SCIENCE":sst,"AVERAGE":avg,"GRADE":grad}}
            lst = list(dit.items())
        print("DATA COLLECTED SUCCESSFULLY!!!\n")

    elif cnt == 3:
        print("\n!!!SUBJECT WISE TOPPERS:!!!")
        find_subject_topper(dit)
        
    elif cnt == 1:
        print("\nREPORT CARD!!!\n")
        display_student_report(lst)

    elif cnt == 4:
        find_students_above_90(dit)

#tuple
#rank on avg
# Create a list from dit values, sorted by average marks
sorted_list = sorted(
    dit.values(), 
    key=lambda student: list(student.values())[0]["AVERAGE"]
)

# Optional: print names and averages
for student in sorted_list:
    name = list(student.keys())[0]
    avg = student[name]["AVERAGE"]
    print(f"{name}: {avg}")

#subject wise class average
