import patient
import search
import doctor
import consultation
import display
patients = []
while True:

    print()
    print("================================")
    print("      MINI HOSPITAL SYSTEM")
    print("================================")
    print("1. Add Patient")
    print("2. Search Patient")
    print("3. Show All Patients")
    print("4. Assign Doctor")
    print("5. Update Consultation")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        patient.add_patient(patients)

    elif choice == "2":
        search.search_patient(patients)

    elif choice == "3":
        display.display_patients(patients)

    elif choice == "4":
        doctor.assign_doctor(patients)

    elif choice == "5":
        consultation.update_consultation(patients)

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")