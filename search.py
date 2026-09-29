def search_patient(patients):

    print("\n--- Search Patient ---")

    patient_id = input("Enter Patient ID: ")

    found = False

    for patient in patients:

        if patient["id"] == patient_id:

            print("\nPatient Found")
            print("Patient ID:", patient["id"])
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Problem:", patient["problem"])
            print("Doctor:", patient["doctor"])
            print("Department:", patient["department"])
            print("Status:", patient["status"])

            found = True
            break

    if found == False:
        print("Patient not found.")