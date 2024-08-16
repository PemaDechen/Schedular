import Data

def room_conflict_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
    return all(cls.room_id != room.id or cls.time_slot_id != slot.id for cls in schedule.classes)


def teacher_conflict_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
    return all(cls.teacher_id != teacher.id or cls.time_slot_id != slot.id for cls in schedule.classes)

# def student_conflict_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
#     return all(cls.section_id != section.id or cls.time_slot_id != slot.id for cls in schedule.classes)

# def room_capacity_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
#     return room.capacity >= section.num_students


# def class_duration_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
#     if subject.is_lab:
#         return slot.start_time in ["09:00", "14:00"]
#     return True

# def elective_group_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
#     if subject.is_elective:
#         elective_subjects = [cls for cls in schedule.classes if cls.subject_id in [s.id for s in subjects if s.is_elective]]
#         return all(cls.time_slot_id == slot.id for cls in elective_subjects)
#     return True


# def daily_class_limit_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
#     day_classes = [cls for cls in schedule.classes if cls.section_id == section.id and
#                    any(ts.id == cls.time_slot_id and ts.day_of_week == slot.day_of_week for ts in time_slots)]
#     lab_sessions = sum(1 for cls in day_classes if next(subj for subj in subjects if subj.id == cls.subject_id).is_lab)
#     theory_sessions = len(day_classes) - lab_sessions

#     if subject.is_lab:
#         return lab_sessions < 1 and theory_sessions <= 4
#     return lab_sessions <= 1 and theory_sessions < 4


# def teacher_working_hours_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
#     teacher_day_classes = [cls for cls in schedule.classes if cls.teacher_id == teacher.id and
#                         any(ts.id == cls.time_slot_id and ts.day_of_week == slot.day_of_week for ts in time_slots)]
#     total_hours = sum(3 if next(subj for subj in subjects if subj.id == cls.subject_id).is_lab else 1 for cls in teacher_day_classes)
#     return 6 <= total_hours + (3 if subject.is_lab else 1) <= 8

# def department_room_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
#     return room.department_id == subject.department_id

# def theory_class_duration_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
#     if not subject.is_lab:
#         start_time, end_time = slot.start_time, slot.end_time
#         return (int(end_time.split(":")[0]) - int(start_time.split(":")[0])) == 1
#     return True

# def lunch_break_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
#     return not (slot.start_time == "13:00" or slot.end_time == "14:00")


# def lab_duration_constraint(schedule: Data.Schedule, slot: Data.TimeSlot, subject: Data.Subject, section: Data.Section, teacher: Data.Teacher, room: Data.Room) -> bool:
#     if subject.is_lab:
#         return slot.start_time in ["09:00", "14:00"] and (slot.end_time == "12:00" or slot.end_time == "17:00")
#     return True

# # Helper Functions
# def select_teacher_for_subject(teachers: List[Teacher], subject: Data.Subject, department_id: int) -> Optional[Teacher]:
#     qualified_teachers = [teacher for teacher in teachers
#                           if subject.id in teacher.subjects and teacher.department_id == department_id]
#     return random.choice(qualified_teachers) if qualified_teachers else None


# def select_room_for_section(rooms: List[Room], section: Data.Section, is_lab: bool) -> Optional[Room]:
#     suitable_rooms = [room for room in rooms
#                       if room.capacity >= section.num_students
#                       and room.department_id == section.department_id
#                       and room.is_lab == is_lab]
#     return random.choice(suitable_rooms) if suitable_rooms else None


# def generate_possible_slots(subject: Data.Subject, time_slots: List[TimeSlot]) -> List[TimeSlot]:
#     if subject.is_lab:
#         return [slot for slot in time_slots if slot.is_lab]
#     else:
#         return [slot for slot in time_slots if not slot.is_lab]


# def sort_constraints_by_priority(constraints: List[Tuple[callable, int]]) -> List[Tuple[callable, int]]:
#     return sorted(constraints, key=lambda x: -x[1])