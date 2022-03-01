import PatientClass as pa
import ProcedureClass as pr


def main():

    my_patient = pa.Patient(
        1, "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", "TRUE"
    )

    my_pro1 = pr.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
    my_pro2 = pr.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
    my_pro3 = pr.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)

    total_charges = 0

    print("*** Patient Bill ***")
    print("Name:", my_patient.get_patName())
    print("Address:", my_patient.get_address())
    print("Phone:", my_patient.get_phone())
    print()

    print("Procedure:", my_pro1.get_proName())
    print("Date:", my_pro1.get_proDate())
    print("Practitioner:", my_pro1.get_practitioner())
    print("Charge: $", format(my_pro1.get_charges(), ".2f"))
    print()

    print("Procedure:", my_pro2.get_proName())
    print("Date:", my_pro2.get_proDate())
    print("Practitioner:", my_pro2.get_practitioner())
    print("Charge: $", format(my_pro2.get_charges(), ".2f"))
    print()

    if my_pro1.get_nameID() == my_patient.get_patID():
        total_charges += my_pro1.get_charges()

    if my_pro2.get_nameID() == my_patient.get_patID():
        total_charges += my_pro2.get_charges()

    if my_pro3.get_nameID() == my_patient.get_patID():
        total_charges += my_pro3.get_charges()

    if my_patient.get_vet_status() == "TRUE":
        total_charges *= 0.60

    print("Total Charges: $", format(total_charges, ",.2f"))


main()
