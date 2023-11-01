from prac_07.project import Project
import datetime


def main():
    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)iler projects by date\n- (A)dd new "
          "project\n- (U)pdate project\n-(Q)uit")
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "l":
            projects = load_projects(input("Input file: "))
        elif choice == "s":
            out_file = input("Out file:")
            save_projects(out_file, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_date = input("Date: ")
            filtered_projects = projects.sort(key=datetime(filter_date))
            print(filtered_projects)
        elif choice == "a":
            print("Let's add a new project")
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid input")
        choice = input(">>>").lower()
    print("Thank you for using custom-built project management software.")


def load_projects(input_file):
    input_file = open(input_file)
    projects = []

    input_file.readline()
    for line in input_file:
        line = line.strip()
        parts = line.split('\t')
        print(parts)
        projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    input_file.close()
    return projects


def save_projects(out_file, out_list):
    out_file = open(out_file, "w")
    for item in out_list:
        out_file.write(str(item) + "\n")
    out_file.close()


def display_projects(projects):
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects = [project for project in projects if not project.is_complete()]
    print(f"Incomplete projects: {incomplete_projects}")
    print(f"Completed projects: {completed_projects}")


def add_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    percent_complete = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))
    return projects


def update_project(projects):
    for i, item in enumerate(projects):
        print(i, item)
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    project[4] = float(input("New Percentage: "))
    project[2] = int(input("New Priority: "))
    projects[project_choice] = project
    return projects


main()
