def display_patients(patients):

    print("\n--- All Patients ---")

    if len(patients) == 0:
        print("No patients available.")
        return

    for patient in patients:

        print("\n----------------------")

        print("Patient ID:", patient["id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Problem:", patient["problem"])
        print("Doctor:", patient["doctor"])
        print("Department:", patient["department"])
        print("Status:", patient["status"])