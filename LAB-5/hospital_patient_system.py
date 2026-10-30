"""Hospital patient records and admission manager."""
import hashlib
import os
import secrets

patient_records = {
    "P101": {"name": "John Doe", "ward": "ICU",
             "is_admitted": True, "bill": 2400.0},
    "P102": {"name": "Jane Smith", "ward": "General",
             "is_admitted": False, "bill": 450.0},
    "P103": {"name": "Robert Brown", "ward": "Private",
             "is_admitted": True, "bill": 1200.0},
}


def admit_patient(p_id, name, ward, intake_log=None):
    """Admit a new patient; return False if the ID already exists."""
    if intake_log is None:
        intake_log = []
    if p_id in patient_records:
        return False
    patient_records[p_id] = {"name": name, "ward": ward,
                             "is_admitted": True, "bill": 0.0}
    intake_log.append(f"Admitted patient {p_id} into ward {ward}")
    return True


def discharge_patient(p_id):
    """Mark a patient as discharged; return False if unknown."""
    try:
        patient_records[p_id]["is_admitted"] = False
    except KeyError:
        return False
    return True


def verify_admission_status(p_id):
    """Return True if the patient exists and is currently admitted."""
    if patient_records.get(p_id) is None:
        return False
    return bool(patient_records[p_id]["is_admitted"])


def calculate_treatment_cost(p_id, tax_multiplier=1.12):
    """Return the patient's bill multiplied by the tax multiplier."""
    base_bill = patient_records[p_id]["bill"]
    return round(base_bill * float(tax_multiplier), 2)


def generate_patient_hash(p_id):
    """Return a SHA-256 hex digest of the patient ID."""
    return hashlib.sha256(p_id.encode()).hexdigest()


def generate_ward_token():
    """Return a cryptographically secure 4-digit ward token."""
    return secrets.randbelow(9000) + 1000


def export_patient_ledger(filename="patient_records.txt"):
    """Write all patient records to a text file."""
    with open(filename, "w", encoding="utf-8") as ledger:
        ledger.write(str(patient_records))
    print("Patient ledger exported to: " + filename)


def get_ward_summary(records):
    """Return the number of currently admitted patients."""
    return sum(1 for details in records.values() if details["is_admitted"])


def main():
    """Run a demo of the patient management workflow."""
    nurse_access_key = os.environ.get("NURSE_ACCESS_KEY", "")
    admit_patient("P104", "Alice Walker", "General")
    discharge_patient("P101")
    print("Is P103 admitted:", verify_admission_status("P103"))
    print("Cost calculated:", calculate_treatment_cost("P103", 1.12))
    print("Patient Hash:", generate_patient_hash("P103"))
    print("Ward Token:", generate_ward_token())
    export_patient_ledger()
    print("Active admits:", get_ward_summary(patient_records))
    print("Access key configured:", bool(nurse_access_key))


if __name__ == "__main__":
    main()
