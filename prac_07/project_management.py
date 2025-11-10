"""
CP1404/CP5632 Practical - project_management.py
Estimate: 4 hours
Actual: 6 hours
"""
import datetime
from prac_07.project import Project

INITIAL_FILENAME = "projects.txt"
MENU_STRING = "- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects \n- (A)dd new projects \n- (U)pdate projects \n- (Q)uit \n>>>"

def main():
    print("Welcome to Pythonic Project Management")
    filename = INITIAL_FILENAME
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} from {filename}")
    menu_choice = input(MENU_STRING).lower()
    while menu_choice != "q":
        if menu_choice == "l":
            new_filename = input("Enter a filename: ")
            if new_filename !="":
                filename = new_filename
            load_projects(filename)
        elif menu_choice == "s":
            new_filename = input("Enter a filename: ")
            if new_filename !="":
                filename = new_filename
            save_projects(projects, filename)
        elif menu_choice == "d":
            display_projects(projects)
        elif menu_choice == "f":
            filter_projects(projects)
        elif menu_choice == "a":
            get_new_project(projects)
        elif menu_choice == "u":
            update_project(projects)
        else:
            print("Invalid menu choice")
        menu_choice = input(MENU_STRING)
    user_choice = input(f"Would you like to save to {filename}?").lower()
    if user_choice == "yes":
        save_projects(projects, filename)
    print("Thank you for using custom-built project management software.")



def load_projects(filename):
    projects = []
    in_file = open(filename, 'r', encoding='UTF-8')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        percent_complete = int(parts[4])
        projects.append(Project(parts[0], start_date, priority, cost_estimate, percent_complete))
    in_file.close()
    return projects


def display_projects(projects):
    projects.sort()
    for project in projects:
        if not project.is_completed():
            print(project)
    for project in projects:
        if project.is_completed():
            print(project)


def save_projects(projects, filename):
    projects = sorted(projects)
    for project in projects:
        project.start_date = project.start_date.strftime('%d/%m/%Y')
    with open(filename, "w",encoding='UTF-8') as out_file:
        for project in projects:
            print(repr(project),file=out_file)


def filter_projects(projects):
    date_string = input("Show projects that start after date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date >= date:
            print(project)


def get_new_project(projects):
    #TODO error checking all these inputs tbh
    name = get_name("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = get_valid_int("Priority: ")
    cost_estimate = input("Cost estimate: $")
    percent_complete = get_valid_int("Percent complete: ")
    if percent_complete > 100 :
        percent_complete = 100
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


def update_project(projects):
    #TODO: all the error checking in this
    for index, project in enumerate(projects):
        print(f"{index} {project}")

    project_choice = get_valid_int("project_choice: ")
    print(projects[project_choice])

    new_percentage = input("New Percentage: ")
    if new_percentage !="":
        projects[project_choice].percent_complete = new_percentage
    new_priority = input("New Priority: ")
    if new_priority !="":
        projects[project_choice].priority = new_priority


def get_valid_int(prompt):
    """ Get valid number from user input. """
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Number must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number


def get_name(prompt):
    """ Get unblank name. """
    choice = input(prompt)
    while choice == "":
        print("Input can not be blank")
        choice = input(prompt)
    return choice.title()


main()