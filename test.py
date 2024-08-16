import unittest
import Data
import Constraints

class TestCalc(unittest.TestCase):
#    def test_roomcints.room_conflict_constraint(schedule, slot,  subject, section, teacher, room), True)

   def test_teacher_conflict_constraint(self):
        new_class = Data.Class(id=1, subject_id=1, teacher_id=1, room_id=1, time_slot_id=1, semester_id=1, section_id=1)
        room = Data.Room(id=2, department_id=1, name="Room A", capacity=50, is_lab=False)
        slot = Data.TimeSlot(id=2, start_time='09:00', end_time='10:00', day_of_week='Monday', is_lab=False)
        subject = Data.Subject(38, 5, 5, "Hydraulic Engineering", 3, True, False)
        section = Data.Section(id=1, name='Section A', semester_id=1, department_id=1, num_students=47)
        teacher =  Data.Teacher(1, "Rahul Sharma", 1, [1, 2, 9]),
        schedule = Data.Schedule()
        schedule.add_class(new_class)


        self.assertEqual(Constraints.teacher_conflict_constraint(schedule, slot,  subject, section, teacher, room), True)

if __name__ == '__main__':
    # unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # Add exit=False here
