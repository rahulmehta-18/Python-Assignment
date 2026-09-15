import BloodCrud as b1

while True:
    print("\n======================================")
    print("       BLOOD MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Add Donor")
    print("2. Display Donors")
    print("3. Update Donor")
    print("4. Search Donor")
    print("5. Delete Donor")
    print("6. Sort Donors")
    print("7. Exit")
    print("======================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        b1.addDonor()
    elif choice == "2":
        b1.displayDonors()
    elif choice == "3":
        b1.updateDonor()
    elif choice == "4":
        b1.searchDonor()
    elif choice == "5":
        b1.deleteDonor()
    elif choice == "6":
        b1.sortDonors()
    elif choice == "7":
        print("Thank you for using Blood Management System.")
        break
    else:
        print("Please enter a valid choice.")n