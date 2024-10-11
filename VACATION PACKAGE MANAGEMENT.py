from collections import deque
class VacationPackageManager:
    def __init__(site):
        
        site.available_packages = ["Beach Muhazi", "Huye Adventure", "City Tour", "Akagera Guest"]

        site.booked_packages = []
        site.scheduled_vacations = deque()
    def show_available_packages(site):
        print("Available Packages:")
        for i, package in enumerate(site.available_packages, 1):
            print(f"{i}. {package}")
        print()

    def book_package(site, package_name):
        if package_name in site.available_packages:
            site.booked_packages.append(package_name)
            print(f"Package '{package_name}' booked successfully!\n")
        else:
            print(f"Package '{package_name}' is not available!\n")

    def undo_booking(site):
        if site.book_package:
            last_package = site.booked_packages.pop()
            print(f"Booking for '{last_package}' has been undone.\n")
        else:
            print("No bookings to undo.\n")

    def schedule_vacation(site, package_name):
        if package_name in site.booked_packages:
            site.scheduled_vacations.append(package_name)
            print(f"Vacation for '{package_name}' has been scheduled.\n")
        else:
            print(f"Package '{package_name}' is not booked, so it can't be scheduled.\n")

    def process_next_vacation(site):
        if site.scheduled_vacations:
            next_vacation = site.scheduled_vacations.popleft()
            print(f"Processing vacation for '{next_vacation}'. Have a great trip!\n")
        else:
            print("No vacations scheduled.\n")

    def show_menu(site):
        print("1. Show available packages")
        print("2. Book a package")
        print("3. Undo last booking")
        print("4. Schedule a vacation")
        print("5. Process next scheduled vacation")
        print("6. Exit\n")


    def run(site):
        while True:
            site.show_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                site.show_available_packages()

            elif choice == "2":
                package_name = input("Enter the name of the package to book: ")
                site.book_package(package_name)

            elif choice == "3":
                site.undo_booking()

            elif choice == "4":
                package_name = input("Enter the name of the package to schedule: ")
                site.schedule_vacation(package_name)

            elif choice == "5":
                site.process_next_vacation()
            elif choice == "6":
                print("Exiting the Vacation Package Manager.")
                break
            else:
                print("Invalid option, please choose a valid option.\n")

manager = VacationPackageManager()
manager.run()
