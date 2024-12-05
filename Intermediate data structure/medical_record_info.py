class MedicalRecordInfo:
    def __init__(self, patient_info, contact_info, admission_date, discharge_date, unit_name,
                 admission_diagnosis_id, discharge_diagnosis_id, pathological_diagnosis_id, blood_type,
                 nursing_info, doctor_name, surgery_infos, ward_infos, cost_infos):
        self.patient_info = patient_info
        self.contact_info = contact_info
        self.admission_date = admission_date
        self.discharge_date = discharge_date
        self.unit_name = unit_name
        self.admission_diagnosis_is = admission_diagnosis_id
        self.discharge_diagnosis_id = discharge_diagnosis_id
        self.pathological_diagnosis_id = pathological_diagnosis_id
        self.blood_type = blood_type
        self.nursing_info = nursing_info
        self.doctor_name = doctor_name
        self.surgery_infos = surgery_infos
        self.ward_info = ward_infos
        self.cost_infos = cost_infos
