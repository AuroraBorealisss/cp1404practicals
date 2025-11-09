"""
CP1404/CP5632 Practical - project_management.py
Estimate: 4 hours

"""
import datetime

from prac_07.project import Project

FILENAME = "projects.txt"
MENU_STRING = "- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects \n- (A)dd new projects \n- (U)pdate projects \n- (Q)uit \n>>>"

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(filename=FILENAME)
    print(f"Loaded {len(projects)} from {FILENAME}")
    menu_choice = input(MENU_STRING).lower()
    while menu_choice != "q":
        if menu_choice == "l":
            load_projects(filename=input("Enter a filename:") or FILENAME)
        elif menu_choice == "s":
            save_projects(projects, filename=input("Enter a filename:") or FILENAME)
        elif menu_choice == "d":
            display_projects(projects)
        elif menu_choice == "f":
            filter_projects(projects)
        elif menu_choice == "a":
            add_new_project(projects)
        elif menu_choice == "u":
            update_project(projects)
        else:
            print("Invalid menu choice")
        menu_choice = input(MENU_STRING)



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
    projects.sort()
    with open(filename, "w",encoding='UTF-8') as out_file:
        for project in projects:
            print(repr(project),file=out_file)


# def filter_projects(projects):
#     date_string = input("Show projects that start after date (d/m/yyyy): ")  # e.g., "30/9/2022"
#     date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
#     for project in projects:
#         if project.start_date >= date:
#             print(project)


def add_new_project(projects):
    #TODO error checking all these inputs tbh
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = input("Cost estimate: $")
    percent_complete = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


def update_project(projects):
    #TODO: all the error checking in this
    for project, index in enumerate(projects):
        print(f"{index} {project}")
    project_choice = int(input("project_choice: "))
    print(projects[project_choice])
    projects[project_choice].percent_complete = int(input("New Percentage: "))
    projects[project_choice].priority = int(input("New Priority: "))

main()