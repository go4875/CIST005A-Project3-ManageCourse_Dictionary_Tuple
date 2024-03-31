"""

def create_course():
    Get course data from user and return
    :return: course (string) and course_info (tuple)
course = input("Enter course name: ")
unit = float(input("Enter the number of unit: "))
term = input("Enter the semester you take this course: ")

    # course_info = (term, unit)            # both work
course_info = tuple([term, unit])

return course, course_info


courses = {}   # Initialize courses dictionary
for i in range(0, 2):
    course_name, course_info = create_course()
    courses[course_name] = course_info

print (course_name)

"""


import sys

"""
Name: Jedd Go
Create Date: 3/01/2024
Submit Date: 03/xx/2024
Description: Simple application to view college courses.
"""

def show_options():
    """
    Display all options and return user's choice
    :return: the user's choice
    """
    menu = """\t Welcome to Class Management application
              \t1. List all courses
              \t2. Add a course
              \t3. Drop a course
              \t4. Sort Courses (Asc)
              \t5. Sort Courses (Desc)
              \t6. Exit \n Your choice: """
    choice = int(input(menu))
    return choice

def list_all(c_dict):
    """
    Function to list all courses
    :course_list: passed as course list across different functions. Updated with different functions
    """
    print("Option 1 - List of all courses you are enrolled")
    c_dict = {}
    add_course(c_dict)
    print("Your courses list: ", c_dict)
    #if course_list:
        #print("Your courses list: ", course_list)
    #else:
        #print("Your course list is empty")
    return c_dict


def add_course(course_list, c_dict):
    """
    :function to add course to course list
    :param - course_list - list of courses array. contains list of courses that are added or dropped
    :param - course - course that is added or dropped to course_list array
    """
    print("Option 2 - Add course selected")

    #course = input(str("Please enter course to add: "))
    c_dict = {}
    """
    better to use a while loop with conditions for termination rather 
    than catching exceptions for normal control flow.
    """
    while True:
            c_name = input("Please enter course to add or 'q' to exit: ")
            if c_name.lower() == "q" or c_name == "":
                break

            c_unit_input = input("Please enter the number of units or 'q' to exit: " )
            if c_unit_input.lower() =='q' or c_unit_input =="":
                break
            try:
                c_unit = float(c_unit_input)
            except ValueError:
                print("Invalid input for units. Please enter a number: ")
                continue

            c_term = input("Enter the semester for this course or 'q' to quit: ")
            if c_term.lower() == "q" or c_term == "":
                break

            c_info = tuple([c_unit, c_term])
            c_dict[c_name] = c_info # 
          
    print("Your course list: ", c_dict.items())
#returning c_dict inside the loop, which means it will exit after adding just one course. 
#If you want to keep adding courses, you should move the return statement outside the loop
    return c_dict 
#print("Your course list: ", list(c_dict.keys()), list(c_dict.values()))
    #if course_list is list:
        #course_list.append(course)
    #else:
        #print("Unable to validate input")
    #course_list.append(course)
    #return course_list

def drop_course(c_dict):
    """
    :function to drop course from course list
    :param - course_list - list of courses array. contains list of courses that are added or dropped
    :param - course - course that is added or dropped to course_list array
    """
    print("Option 3 - Drop course selected")
    course = input("Please enter course to drop: ")
    if course in course_list: #passing value of input to check if exist in course_list
        course_list.remove(course)
    else:
        print("Course is not in your list")
    return course_list

def sort_course(c_dict):
    """
    :function to sort in ascending order courses from course list
    :param - course_list - list of courses array. contains list of courses that are added or dropped
    :param - course - course that is added or dropped to course_list array
    """
    if course_list:
        course_list.sort() #calling sort method to sort course list in ascending order
        print("Option 4 selected - Sort courses in ascending order: ", course_list)
    else:
        print("No courses on list. Please add a course")
    return course_list

def sort_course_reverse(c_dict):
    """
    :function to sort in descending order courses from course list
    :param - course_list - list of courses array. contains list of courses that are added or dropped
    :param - course - course that is added or dropped to course_list array
    """
    if course_list:
        course_list.sort(reverse=True) #calling sort method with keyword argement,  to sort course list in descending order
        print("Option 5 selected - Sort courses in descending order: ", course_list)
    else:
        print("No courses on list. Please add a course")
    return course_list


def main():
# --------------------Main Program--------------------------------
    #course_list = list()
    #course_list = []
    c_dict = {}
    while True:
        choice = show_options()
        if choice == 1:
            #course_list = []
            #course_list = list_all(course_list)
            #course_list = c_dict.keys, c_dict.values
            c_dict = list_all(c_dict)
        elif choice == 2:
            c_dict =  add_course(c_dict)
        elif choice == 3:
            c_dict = drop_course(c_dict)
        elif choice == 4:
            c_dict = sort_course(c_dict)
        elif choice == 5:
            c_dict =  sort_course_reverse(c_dict)
        elif choice == 6:
            print("Thank You for attending West Valley College")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

