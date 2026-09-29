def assign_doctor(patients):

    print("\n--- Doctor Assignment ---")

    patient_id = input("Enter Patient ID: ")

    doctor = input("Enter Doctor Name: ")
    department = input("Enter Department: ")

    found = False

    for patient in patients:

        if patient["id"] == patient_id:

            patient["doctor"] = doctor
            patient["department"] = department

            print("Doctor assigned successfully.")

            found = True
            break

    if found == False:
        print("Patient not found.")