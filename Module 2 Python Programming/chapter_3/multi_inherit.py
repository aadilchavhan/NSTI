# class A:
#    def abc(self):
#        print("This A")

# class B(A):
#     def xyz(self):
#         print("This B")

# class C(A):
#     def wwe(self):
#         print("This C")

# class D(A):
#     def exc(self):
#         print("This D")

# class E(B,C,D):
#     pass
# x=E()
# x.exc()
# x.wwe()
# x.xyz()
# x.abc()


"""________________________________________________""" 



# class NSTI:
#     def __init__(self, lunch):
#         self.lunch = lunch

# class Lab:
#     def __init__(self, lab):
#         self.lab = lab

# class AI(NSTI, Lab):
#     def __init__(self, lunch, lab, computer):
#         NSTI.__init__(self, lunch)
#         Lab.__init__(self, lab)
#         self.computer = computer

#     def disp(self):
#         print(f'Lunch: {self.lunch}, Lab: {self.lab}, Computer: {self.computer}')

# x = AI("Roti Sabzi", "ADIT Lab", "hp")
# x.disp()
  


'''Question 1: Create a Specialist class that inherits from two parent classes, Doctor and Surgeon.
 The Doctor class should have a method diagnose that prints "Diagnosing the patient", 
 and the Surgeon class should have a method operate that prints "Performing surgery". 
 The Specialist class should have a constructor that initializes the specialist's name and specialty, 
and a method display_info that prints the name and specialty.'''



# class Doctor:
#     def diagnose(self):
#         print("Diagnosing the patient")

# class Surgeon:
#     def operate(self):
#         print("Performing surgery")

# class Specialist(Doctor, Surgeon):
#     def __init__(self, name, specialty):
#         self.name = name
#         self.specialty = specialty

#     def display(self):
#         print(f'Specialist Name: {self.name}')
#         print(f'Specialty: {self.specialty}')


# specialist = Specialist("Dr. Majid Khan ", "Neurologist")
# specialist.display()
# specialist.diagnose()
# specialist.operate()


"""Question 2: Create an OnlineCourse class that inherits from two parent classes, CourseContent and InteractiveTools.
 The CourseContent class should have a method provide_materials that prints "Providing course materials",
  and the InteractiveTools class should have a method facilitate_interaction that prints "Facilitating student interaction with tools". 
  The OnlineCourse class should have a constructor that initializes the course name and a method display_info that prints the course name. 
  Additionally, write a method start_course that prints "Starting the course"."""


# class Course_Content:
#     def provide_materials(self):
#         print("Providing course materials")

# class Interactive_Tools:
#     def facilitate_interaction(self):
#         print("Facilitating student interaction with tools")

# class Online_Course(Course_Content, Interactive_Tools):
#     def __init__(self, name):
#         self.name= name

#     def display_info(self):
#         print(f'Course Name: {self.name}')

#     def start_course(self):
#         print("Starting the course")


# online_course = Online_Course("AI Micro Degree")
# online_course.display_info()
# online_course.provide_materials()
# online_course.facilitate_interaction()
# online_course.start_course()


'''Question 3: Create a Drone class that inherits from two parent classes, FlyingMechanism and Camera. 
The FlyingMechanism class should have a method fly that prints "Drone is flying", 
and the Camera class should have a method take_photo that prints "Taking a photo". 
The Drone class should have a constructor that initializes the drone's model and a method display_info that prints the model.
 Additionally, write a method perform_actions that calls the methods from both parent classes.'''


class FlyingMechanism:
    def fly(self):
        print("Drone is flying")

class Camera:
    def take_photo(self):
        print("Taking a photo")

class Drone(FlyingMechanism, Camera):
    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        print(f'Model: {self.name}')

    def perform_actions(self):
        self.fly()
        self.take_photo()

drone = Drone("DRDO Rustom-II ")
drone.display_info()
drone.perform_actions()

