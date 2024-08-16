import Data
import random


# Create sample data for departments
departments = [
    Data.Department(1, "Computer Science"),
    Data.Department(2, "Electrical Engineering"),
    Data.Department(3, "Mechanical Engineering"),
    Data.Department(4, "Electronics and Communication Engineering"),
    Data.Department(5, "Civil Engineering")
]

# Create sample data for programs
programs = [
    Data.Program(1, "B.Tech", 8),  # Bachelor of Technology with 8 semesters 
    Data.Program(2, "M.Tech", 4)   # Master of Technology with 4 semesters
]

# Create sample data for semesters with dynamic section generation
semesters = []
semester_id = 1
for department in departments:
    for program in programs:
        for semester_number in range(1, program.duration_in_semesters + 1):
            # Generate a random number of students for this semester (between 30 and 300)
            num_students = random.randint(30, 300)
            semester = Data.Semester(
                id=semester_id,
                program_id=program.id,
                semester_number=semester_number,
                department_id=department.id,
                num_students=num_students,
                sections=[]
            )
            semester.sections = Data.generate_sections(semester_id, department.id, num_students)
            semesters.append(semester)
            semester_id += 1

# Print out the generated semesters and sections for verification
# for semester in semesters:
#     print(f"Department: {next(d.name for d in departments if d.id == semester.department_id)}")
#     print(f"Program: {next(p.name for p in programs if p.id == semester.program_id)}")
#     print(f"Semester: {semester.semester_number}")
#     print(f"Total Students: {semester.num_students}")
#     print("Sections:")
#     for section in semester.sections:
#         print(f"  {section.name}: {section.num_students} students")
#     print()


# Create sample data for subjects
subjects = [
    # Computer Science Core Subjects
    Data.Subject(1, 1, 1, "Data Structures", 4, False, False),
    Data.Subject(2, 1, 2, "Algorithms", 4, False, False),
    Data.Subject(3, 1, 3, "Database Systems", 3, False, False),
    Data.Subject(4, 1, 4, "Operating Systems", 3, False, False),
    Data.Subject(5, 1, 5, "Computer Networks", 3, False, False),

    # Computer Science Elective Subjects
    Data.Subject(6, 1, 6, "Machine Learning", 3, True, False),
    Data.Subject(7, 1, 7, "Artificial Intelligence", 3, True, False),
    Data.Subject(8, 1, 8, "Big Data Analytics", 3, True, False),

    # Computer Science Lab Subjects
    Data.Subject(9, 1, 1, "Data Science Lab", 2, False, True),
    Data.Subject(10, 1, 2, "Algorithms Lab", 2, False, True),

    # Electrical Engineering Core Subjects
    Data.Subject(11, 2, 1, "Circuit Analysis", 4, False, False),
    Data.Subject(12, 2, 2, "Electromagnetic Fields", 3, False, False),
    Data.Subject(13, 2, 3, "Power Systems", 3, False, False),
    Data.Subject(14, 2, 4, "Control Systems", 4, False, False),

    # Electrical Engineering Elective Subjects
    Data.Subject(15, 2, 5, "Renewable Energy Systems", 3, True, False),
    Data.Subject(16, 2, 6, "Smart Grid Technology", 3, True, False),

    # Electrical Engineering Lab Subjects
    Data.Subject(17, 2, 1, "Power Electronics Lab", 2, False, True),
    Data.Subject(18, 2, 2, "Circuit Design Lab", 2, False, True),

    # Mechanical Engineering Core Subjects
    Data.Subject(19, 3, 1, "Thermodynamics", 4, False, False),
    Data.Subject(20, 3, 2, "Fluid Mechanics", 4, False, False),
    Data.Subject(21, 3, 3, "Mechanics of Materials", 3, False, False),
    Data.Subject(22, 3, 4, "Manufacturing Processes", 3, False, False),

    # Mechanical Engineering Elective Subjects
    Data.Subject(23, 3, 5, "Robotics", 3, True, False),
    Data.Subject(24, 3, 6, "Automotive Engineering", 3, True, False),

    # Mechanical Engineering Lab Subjects
    Data.Subject(25, 3, 1, "Fluid Mechanics Lab", 2, False, True),
    Data.Subject(26, 3, 2, "Manufacturing Lab", 2, False, True),

    # Electronics and Communication Engineering Core Subjects
    Data.Subject(27, 4, 1, "Analog Electronics", 4, False, False),
    Data.Subject(28, 4, 2, "Digital Signal Processing", 4, False, False),
    Data.Subject(29, 4, 3, "Communication Systems", 3, False, False),

    # Electronics and Communication Engineering Elective Subjects
    Data.Subject(30, 4, 4, "VLSI Design", 3, True, False),
    Data.Subject(31, 4, 5, "Embedded Systems", 3, True, False),

    # Electronics and Communication Engineering Lab Subjects
    Data.Subject(32, 4, 1, "Microprocessor Lab", 2, False, True),
    Data.Subject(33, 4, 2, "Digital Communication Lab", 2, False, True),

    # Civil Engineering Core Subjects
    Data.Subject(34, 5, 1, "Structural Analysis", 4, False, False),
    Data.Subject(35, 5, 2, "Geotechnical Engineering", 3, False, False),
    Data.Subject(36, 5, 3, "Transportation Engineering", 3, False, False),

    # Civil Engineering Elective Subjects
    Data.Subject(37, 5, 4, "Environmental Engineering", 3, True, False),
    Data.Subject(38, 5, 5, "Hydraulic Engineering", 3, True, False),

    # Civil Engineering Lab Subjects
    Data.Subject(39, 5, 1, "Structural Lab", 2, False, True),
    Data.Subject(40, 5, 2, "Geotechnical Lab", 2, False, True),
]

## Create sample data for rooms, categorized by department
rooms = [
    # Computer Science Rooms
    Data.Room(1, 1, "CS101", 60, False),
    Data.Room(2, 1, "CS102", 40, False),
    Data.Room(3, 1, "CS103", 50, False),
    Data.Room(4, 1, "CS104", 60, False),
    Data.Room(5, 1, "CS105", 55, False),
    Data.Room(6, 1, "CS106", 45, False),
    Data.Room(7, 1, "CS107", 50, False),
    Data.Room(8, 1, "CS108", 40, False),
    Data.Room(9, 1, "CS109", 60, False),
    Data.Room(10, 1, "CS110", 50, False),
    Data.Room(11, 1, "CSLab1", 60, True),
    Data.Room(12, 1, "CSLab2", 60, True),
    Data.Room(13, 1, "CSLab3", 60, True),

    # Electrical Engineering Rooms
    Data.Room(14, 2, "EE101", 50, False),
    Data.Room(15, 2, "EE102", 40, False),
    Data.Room(16, 2, "EE103", 45, False),
    Data.Room(17, 2, "EE104", 55, False),
    Data.Room(18, 2, "EE105", 50, False),
    Data.Room(19, 2, "EE106", 60, False),
    Data.Room(20, 2, "EE107", 40, False),
    Data.Room(21, 2, "EE108", 45, False),
    Data.Room(22, 2, "EE109", 55, False),
    Data.Room(23, 2, "EE110", 50, False),
    Data.Room(24, 2, "EELab1", 60, True),
    Data.Room(25, 2, "EELab2", 60, True),
    Data.Room(26, 2, "EELab3", 60, True),

    # Mechanical Engineering Rooms
    Data.Room(27, 3, "ME101", 60, False),
    Data.Room(28, 3, "ME102", 50, False),
    Data.Room(29, 3, "ME103", 45, False),
    Data.Room(30, 3, "ME104", 55, False),
    Data.Room(31, 3, "ME105", 50, False),
    Data.Room(32, 3, "ME106", 40, False),
    Data.Room(33, 3, "ME107", 45, False),
    Data.Room(34, 3, "ME108", 55, False),
    Data.Room(35, 3, "ME109", 50, False),
    Data.Room(36, 3, "ME110", 60, False),
    Data.Room(37, 3, "MELab1", 60, True),
    Data.Room(38, 3, "MELab2", 60, True),
    Data.Room(39, 3, "MELab3", 60, True),

    # Electronics and Communication Engineering Rooms
    Data.Room(40, 4, "ECE101", 55, False),
    Data.Room(41, 4, "ECE102", 45, False),
    Data.Room(42, 4, "ECE103", 50, False),
    Data.Room(43, 4, "ECE104", 40, False),
    Data.Room(44, 4, "ECE105", 55, False),
    Data.Room(45, 4, "ECE106", 50, False),
    Data.Room(46, 4, "ECE107", 45, False),
    Data.Room(47, 4, "ECE108", 40, False),
    Data.Room(48, 4, "ECE109", 50, False),
    Data.Room(49, 4, "ECE110", 55, False),
    Data.Room(50, 4, "ECELab1", 60, True),
    Data.Room(51, 4, "ECELab2", 60, True),
    Data.Room(52, 4, "ECELab3", 60, True),

    # Civil Engineering Rooms
    Data.Room(53, 5, "CE101", 60, False),
    Data.Room(54, 5, "CE102", 50, False),
    Data.Room(55, 5, "CE103", 55, False),
    Data.Room(56, 5, "CE104", 45, False),
    Data.Room(57, 5, "CE105", 50, False),
    Data.Room(58, 5, "CE106", 60, False),
    Data.Room(59, 5, "CE107", 40, False),
    Data.Room(60, 5, "CE108", 45, False),
    Data.Room(61, 5, "CE109", 55, False),
    Data.Room(62, 5, "CE110", 50, False),
    Data.Room(63, 5, "CELab1", 60, True),
    Data.Room(64, 5, "CELab2", 60, True),
    Data.Room(65, 5, "CELab3", 60, True),
]


# Create sample data for teachers, categorized by department
teachers = [
    # Computer Science Teachers
    Data.Teacher(1, "Rahul Sharma", 1, [1, 2, 9]),
    Data.Teacher(2, "Anjali Singh", 1, [3, 4, 10]),
    Data.Teacher(3, "Vijay Kumar", 1, [5, 6]),
    Data.Teacher(4, "Neha Mehta", 1, [7, 8, 9]),
    Data.Teacher(5, "Anil Gupta", 1, [1, 2, 10]),
    Data.Teacher(6, "Pooja Verma", 1, [3, 4]),
    Data.Teacher(7, "Rajesh Malhotra", 1, [5, 6, 7]),
    Data.Teacher(8, "Sunita Desai", 1, [8, 9, 10]),
    Data.Teacher(9, "Suresh Bhat", 1, [1, 2]),
    Data.Teacher(10, "Kavita Reddy", 1, [3, 4, 9]),

    # Electrical Engineering Teachers
    Data.Teacher(11, "Vikram Singh", 2, [11, 12, 17]),
    Data.Teacher(12, "Aruna Rao", 2, [11, 13, 14, 18]),
    Data.Teacher(13, "Ashok Nair", 2, [15, 16, 17]),
    Data.Teacher(14, "Deepa Iyer", 2, [11, 12, 18]),
    Data.Teacher(15, "Sanjay Mehta", 2, [11, 13, 14]),
    Data.Teacher(16, "Suman Patil", 2, [11, 15, 16, 17]),
    Data.Teacher(17, "Pankaj Deshmukh", 2, [11, 12, 18]),
    Data.Teacher(18, "Meena Reddy", 2, [11, 13, 14]),
    Data.Teacher(19, "Subhash Gupta", 2, [15, 16, 17]),
    Data.Teacher(20, "Anu Jain", 2, [11, 12, 18]),

    # Mechanical Engineering Teachers
    Data.Teacher(21, "Shashank Agarwal", 3, [19, 20, 25]),
    Data.Teacher(22, "Maya Deshmukh", 3, [21, 22, 26]),
    Data.Teacher(23, "Ajay Kumar", 3, [23, 24, 25]),
    Data.Teacher(24, "Sneha Rao", 3, [19, 20, 26]),
    Data.Teacher(25, "Kiran Nair", 3, [21, 22]),
    Data.Teacher(26, "Rajini Patel", 3, [23, 24, 25]),
    Data.Teacher(27, "Rakesh Verma", 3, [19, 20, 26]),
    Data.Teacher(28, "Sonali Jain", 3, [21, 22]),
    Data.Teacher(29, "Mahesh Gupta", 3, [23, 24, 25]),
    Data.Teacher(30, "Bhavana Iyer", 3, [19, 20, 26]),

    # Electronics and Communication Engineering Teachers
    Data.Teacher(31, "Vishal Sharma", 4, [27, 28, 32]),
    Data.Teacher(32, "Anjali Nair", 4, [29, 30, 33]),
    Data.Teacher(33, "Gopal Singh", 4, [31, 32, 27]),
    Data.Teacher(34, "Deepika Deshmukh", 4, [28, 29, 33]),
    Data.Teacher(35, "Mukesh Kumar", 4, [30, 31]),
    Data.Teacher(36, "Sunita Rao", 4, [27, 28, 32]),
    Data.Teacher(37, "Vinay Malhotra", 4, [29, 30, 33]),
    Data.Teacher(38, "Asha Jain", 4, [31, 32, 27]),
    Data.Teacher(39, "Santosh Gupta", 4, [28, 29, 33]),
    Data.Teacher(40, "Rekha Patel", 4, [30, 31]),

    # Civil Engineering Teachers
    Data.Teacher(41, "Anuj Sharma", 5, [34, 35, 39]),
    Data.Teacher(42, "Shalini Rao", 5, [36, 37, 40]),
    Data.Teacher(43, "Dinesh Kumar", 5, [38, 39, 34]),
    Data.Teacher(44, "Ranjana Iyer", 5, [35, 36, 40]),
    Data.Teacher(45, "Pradeep Nair", 5, [37, 38]),
    Data.Teacher(46, "Madhuri Patel", 5, [34, 35, 39]),
    Data.Teacher(47, "Suraj Desai", 5, [36, 37, 40]),
    Data.Teacher(48, "Namrata Jain", 5, [38, 39, 34]),
    Data.Teacher(49, "Prakash Gupta", 5, [35, 36, 40]),
    Data.Teacher(50, "Sarika Reddy", 5, [37, 38]),
]

# Create sample data for time slots
time_slots = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
regular_times = ["09:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-13:00", "14:00-15:00", "15:00-16:00", "16:00-17:00"]
lab_times = ["09:00-12:00", "14:00-17:00"]

# Populate time slots for each day of the week
for day in days:
    # Add regular class time slots
    for time in regular_times:
        time_slots.append(Data.TimeSlot(len(time_slots) + 1, time.split("-")[0], time.split("-")[1], day, is_lab=False))
    # Add lab time slots
    for time in lab_times:
        time_slots.append(Data.TimeSlot(len(time_slots) + 1, time.split("-")[0], time.split("-")[1], day, is_lab=True))



students = []
student_id = 1
for department in departments:
    for program in programs:
        for semester_number in range(1, program.duration_in_semesters + 1):
            semester = next((s for s in semesters if s.department_id == department.id and
                             s.program_id == program.id and s.semester_number == semester_number), None)
            if semester:
                for _ in range(semester.num_students):
                    students.append(Data.Student(
                        id=student_id,
                        name=f"Student_{student_id}",
                        department_id=department.id,
                        program_id=program.id,
                        current_semester=semester.id
                    ))
                    student_id += 1