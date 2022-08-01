from datetime import date

class Student:
    academic_yr = '2022-23'
    num_students = 0

    def __init__(self,first_name,last_name,tuition):
        self.first_name = first_name
        self.last_name = last_name
        self.tuition = tuition
        Student.num_students +=1

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_email(self):
        return f"{self.first_name}.{self.last_name}@school.edu"
    
    @classmethod
    def set_fee_waiver(cls,fee_waiver):
        cls.fee_waiver = fee_waiver
    
    def apply_fee_waiver(self):
        self.tuition -= self.tuition*Student.fee_waiver
        return self.tuition   
    
    @classmethod
    def from_tuple(cls,student_tuple):
        first_name, last_name, tuition = student_tuple
        return cls(first_name,last_name,tuition)

    @staticmethod
    def is_fall(date):
        if date.month in [9,10,11]:
            print("Yes, the fall semester is in progress.")
        else:
            print("Not the fall semester")
            
