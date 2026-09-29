def update_consultation(patients):

    print("\n--- Consultation Status ---")

    patient_id = input("Enter Patient ID: ")

    for patient in patients:

        if patient["id"] == patient_id:

            print("\n1. Pending")
            print("2. In Progress")
            print("3. Completed")

            choice = input("Enter your choice: ")

            if choice == "1":
                patient["status"] = "Pending"

            elif choice == "2":
                patient["status"] = "In Progress"

            elif choice == "3":
                patient["status"] = "Completed"

            else:
                print("Invalid choice.")
                return

            print("Consultation status updated.")
            return

    print("Patient not found.")