def create_course():
    """
    Get course data from user and return
    :return: course (string) and course_info (tuple)
    """
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




