class ContactInfo:
    def __init__(self, patient_id, name, relationship, address=None, phone=None):
        self.patient_id = patient_id
        self.name = name
        self.relationship = relationship
        self.address = address
        self.phone = phone