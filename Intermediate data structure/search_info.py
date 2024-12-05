class QueryConditions:
    def __init__(self, gender=None, medical_record_number=None,
                  patient_name=None, payment_method=None, nationality=None,
                 ethnicity=None, address=None, contact_phone=None, contact_address=None, birth_from=None, birth_to=None,
                 admission_time_from=None, admission_time_to=None, discharge_time_from=None, discharge_time_to=None,
                 department=None, patient_age_from=None, patient_age_to=None, disease_name=None,
                 diagnosis_type=None, treatment_status=None):
        self.gender = gender
        self.medical_record_number = medical_record_number
        self.patient_name = patient_name
        self.payment_method = payment_method
        self.nationality = nationality
        self.ethnicity = ethnicity
        self.address = address
        self.contact_phone = contact_phone
        self.contact_address = contact_address
        self.birth_from = birth_from
        self.birth_to = birth_to
        self.admission_time_from = admission_time_from
        self.admission_time_to = admission_time_to
        self.discharge_time_from = discharge_time_from
        self.discharge_time_to = discharge_time_to
        self.department = department
        self.patient_age_from = patient_age_from
        self.patient_age_to = patient_age_to
        self.disease_name = disease_name
        self.diagnosis_type = diagnosis_type
        self.treatment_status = treatment_status