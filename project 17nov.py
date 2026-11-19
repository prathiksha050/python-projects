donors = []
blood = {"A+": 0, "B+": 0, "O+": 0, "AB+": 0}

def add_donor():
    name = input("Enter donor name: ")
    group = input("Enter blood group: ").upper()

    if group in blood:
        donors.append((name, group))
        blood[group] += 1
        print("Donor added successfully!")
    else:
        print("Invalid blood group!")
def display_donors():
    if not donors:
        print("No donors available.")
        return

    print("List of Donors:")
    for donor in donors:
        print(f"Name: {donor[0]}, Blood Group: {donor[1]}")
def display_blood_count():
    print("Blood Group Count:")
    for group, count in blood.items():
        print(f"{group}: {count}")
def main():
    while True:
        print("\nBlood Donation Management System")
        print("1. Add Donor")
        print("2. Display Donors")
        print("3. Display Blood Group Count")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_donor()
        elif choice == "2":
            display_donors()
        elif choice == "3":
            display_blood_count()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")
main()