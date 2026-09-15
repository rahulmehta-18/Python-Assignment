blood_donors = []

def addDonor():
    donor_id = int(input("Enter Donor ID: "))
    name = input("Enter Donor Name: ")
    blood_group = input("Enter Blood Group: ").upper()
    age = int(input("Enter Age: "))
    city = input("Enter City: ")

    donor = {
        "ID": donor_id,
        "Name": name,
        "Blood": blood_group,
        "Age": age,
        "City": city
    }

    blood_donors.append(donor)
    print("Donor added successfully.")


def displayDonors():
    if len(blood_donors) == 0:
        print("No donor records available.")
        return

    print("\n------------------------------------------------------------")
    print("ID\tName\t\tBlood Group\tAge\tCity")
    print("------------------------------------------------------------")

    for donor in blood_donors:
        print(donor["ID"], "\t", donor["Name"], "\t\t",
              donor["Blood"], "\t\t", donor["Age"], "\t", donor["City"])


def searchDonor():
    value = input("Enter Donor ID or Blood Group to search: ").upper()
    found = False

    for donor in blood_donors:
        if str(donor["ID"]) == value or donor["Blood"] == value:
            print("\nDonor Found")
            print("-------------------------")
            print("Donor ID    :", donor["ID"])
            print("Name        :", donor["Name"])
            print("Blood Group :", donor["Blood"])
            print("Age         :", donor["Age"])
            print("City        :", donor["City"])
            found = True

    if found == False:
        print("Donor record not found.")


def updateDonor():
    donor_id = int(input("Enter Donor ID to update: "))
    found = False

    for donor in blood_donors:
        if donor["ID"] == donor_id:
            found = True
            print("1. Change Name")
            print("2. Change Blood Group")
            print("3. Change Age")
            print("4. Change City")

            choice = input("Enter what you want to update: ")

            if choice == "1":
                donor["Name"] = input("Enter new name: ")
            elif choice == "2":
                donor["Blood"] = input("Enter new blood group: ").upper()
            elif choice == "3":
                donor["Age"] = int(input("Enter new age: "))
            elif choice == "4":
                donor["City"] = input("Enter new city: ")
            else:
                print("Invalid choice.")
                return

            print("Donor details updated successfully.")
            break

    if found == False:
        print("Donor ID not found.")


def deleteDonor():
    donor_id = int(input("Enter Donor ID to delete: "))
    found = False

    for donor in blood_donors:
        if donor["ID"] == donor_id:
            blood_donors.remove(donor)
            found = True
            print("Donor record deleted successfully.")
            break

    if found == False:
        print("Donor ID not found.")


def sortDonors():
    if len(blood_donors) == 0:
        print("No donor records available for sorting.")
        return

    print("1. Sort by Donor Name")
    print("2. Sort by Age")
    print("3. Sort by Blood Group")

    choice = input("Enter your choice: ")

    if choice == "1":
        blood_donors.sort(key=lambda x: x["Name"].lower())
    elif choice == "2":
        blood_donors.sort(key=lambda x: x["Age"])
    elif choice == "3":
        blood_donors.sort(key=lambda x: x["Blood"])
    else:
        print("Invalid choice.")
        return

    print("Donor records sorted successfully.")
    displayDonors()