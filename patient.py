def add_patient(patients):

    print("\n--- Add Patient ---")

    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    problem = input("Enter Problem: ")

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "problem": problem,
        "doctor": "Not Assigned",
        "department": "Not Assigned",
        "status": "Pending"
    }

    patients.append(patient)

    print("Patient added successfully.")    