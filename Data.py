# Importing necessary modules and setting up logging
from typing import List, Optional, Tuple
from dataclasses import dataclass, field
import random
import math
import logging

logging.basicConfig(level=logging.INFO) # This is for logging purpose
logger = logging.getLogger(__name__)

from dataclasses import dataclass, field
from typing import List, Optional
import random
import math

# Represents a department within the institution.
@dataclass
class Department:
    id: int  # Unique identifier for the department
    name: str  # The official name of the department

# Represents a program that a student can enroll in.
@dataclass
class Program:
    id: int  # Unique identifier for the program
    name: str  # Name of the program (e.g., Computer Science)
    duration_in_semesters: int  # Total duration of the program in semesters

# Represents a section within a semester.
@dataclass
class Section:
    id: int
    name: str
    semester_id: int
    department_id: int
    num_students: int

# Represents a semester within a program.
@dataclass
class Semester:
    id: int
    program_id: int
    semester_number: int
    department_id: int
    num_students: int
    sections: List[Section]

# Function to generate sections based on number of students
def generate_sections(semester_id: int, department_id: int, num_students: int) -> List[Section]:
    sections = []
    num_sections = math.ceil(num_students / 60)
    num_sections = min(num_sections, 5)  # Cap at 5 sections
    students_per_section = math.ceil(num_students / num_sections)

    for i in range(num_sections):
        section_students = min(students_per_section, num_students)
        sections.append(Section(
            id=len(sections) + 1,
            name=f"Section {chr(65 + i)}",  # A, B, C, D, E
            semester_id=semester_id,
            department_id=department_id,
            num_students=section_students
        ))
        num_students -= section_students

    return sections


# Represents a subject taught within a department.
@dataclass
class Subject:
    id: int  # Unique identifier for the subject
    department_id: int  # Reference to the department offering the subject
    semester_id: int  # Reference to the semester in which the subject is offered
    name: str  # Subject name (e.g., Data Structures)
    points: int  # Credit points for the subject
    is_elective: bool  # Indicates if the subject is optional (elective)
    is_lab: bool  # Indicates if the subject includes practical lab work

# Represents a group of elective subjects available in a semester.
@dataclass
class ElectiveGroup:
    id: int  # Unique identifier for the elective group
    semester_id: int  # Reference to the semester containing this group
    group_name: str  # Name of the elective group

# Represents a specific elective subject within an elective group.
@dataclass
class ElectiveSubject:
    id: int  # Unique identifier for the elective subject
    subject_id: int  # Reference to the subject
    elective_group_id: int  # Reference to the elective group containing this subject

# Represents a classroom or lab room available for scheduling classes.
@dataclass
class Room:
    id: int  # Unique identifier for the room
    department_id: int  # Reference to the department where the room is located
    name: str  # Room name (e.g., Room 101)
    capacity: int  # Number of students the room can accommodate
    is_lab: bool  # Indicates if the room is a laboratory
    is_available: bool = True  # Indicates if the room is available for scheduling classes

# Represents a teacher employed by the institution.
@dataclass
class Teacher:
    id: int  # Unique identifier for the teacher
    name: str  # Teacher's name
    department_id: int  # Reference to the department where the teacher works
    subjects: List[int]  # List of subject IDs the teacher is qualified to teach

# Represents a student enrolled in the institution.
@dataclass
class Student:
    id: int  # Unique identifier for the student
    name: str  # Student's name
    department_id: int  # Reference to the department the student belongs to
    program_id: int  # Reference to the program the student is enrolled in
    current_semester: int  # Current semester number for the student

# Represents a time slot for scheduling classes.
@dataclass
class TimeSlot:
    id: int  # Unique identifier for the time slot
    start_time: str  # Start time of the slot (format: HH:MM)
    end_time: str  # End time of the slot (format: HH:MM)
    day_of_week: str  # Day of the week for this time slot
    is_lab: bool  # Indicates if the slot is intended for lab sessions

# Represents a scheduled class session.
@dataclass
class Class:
    id: int  # Unique identifier for the class
    subject_id: int  # Reference to the subject being taught
    teacher_id: int  # Reference to the teacher conducting the class
    room_id: int  # Reference to the room where the class is held
    time_slot_id: int  # Reference to the time slot for the class
    semester_id: int  # Reference to the semester in which the class occurs
    section_id: int  # Reference to the section in which the class occurs

# Represents a student's choice of elective subjects.
@dataclass
class StudentElectiveChoice:
    id: int  # Unique identifier for the elective choice
    student_id: int  # Reference to the student making the choice
    elective_subject_id: int  # Reference to the elective subject chosen by the student

# Represents the availability of a teacher for specific time slots.
@dataclass
class TeacherAvailability:
    id: int  # Unique identifier for the availability record
    teacher_id: int  # Reference to the teacher
    time_slot_id: int  # Reference to the time slot
    is_available: bool  # Indicates if the teacher is available during this time slot


@dataclass
class Schedule:
    classes: List['Class'] = field(default_factory=list)
    score: float = 0.0

    def add_class(self, new_class: 'Class'):
        print('This is new_class', new_class)
        self.classes.append(new_class)

    def remove_class(self, class_to_remove: 'Class'):
        self.classes.remove(class_to_remove)
      
    def retrieve_class(self, class_id:int):
      return next(cls for cls in self.classes if cls.id== class_id),None