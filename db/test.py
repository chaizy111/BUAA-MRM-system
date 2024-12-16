from db.normal_op import *
from db.statistic_op import *
from intermediate_data_structure.patient_info import PatientInfo
from intermediate_data_structure.contact_info import ContactInfo
from intermediate_data_structure.surgery_info import SurgeryInfo
from intermediate_data_structure.ward_info import WardInfo
from intermediate_data_structure.cost_info import CostInfo

class MedicalRecordInfo:
    def __init__(self):
        self.patient_info = PatientInfo(
            name="王五",
            gender="男",
            birth_date="1990-01-01",
            age=34,
            nationality="中国",
            place_of_birth="北京",
            ethnicity="汉",
            id_card_number="123456789012345112",
            occupation="科员",
            marital_status="Married",
            current_address="123 Main St, Anytown, USA",
            phone="123-456-7890",
            postal_code="12345",
            household_address="456 Broadway, Anytown, USA"
        )
        self.contact_info = ContactInfo(
            patient_id=self.patient_info.id_card_number,
            name="王六",
            relationship="父亲",
            address="123 Main St, Anytown, USA",
            phone="987-654-3210"
        )
        self.unit_name = "骨科"
        self.admission_date = "2024-01-01"
        self.discharge_date = "2024-01-15"
        self.admission_diagnosis_id = "A00.000"
        self.discharge_diagnosis_id = "A00.000"
        self.pathological_diagnosis_id = "A00.000"
        self.doctor_name = "唐洋"
        self.blood_type = "11"
        self.payment_method = "Credit Card"
        self.surgery_infos = self.surgery_infos = [
            SurgeryInfo(
                surgery_date="2024-01-10",
                surgery_name="股骨头修复",
                surgeon_name="唐洋",
                assistant_surgeon_name="贺娜"
            )
        ]
        self.ward_infos = [
            WardInfo(
                ward_name="101",
                start_time="2024-01-02 08:00:00",
                end_time="2024-01-10 10:00:00"
            )
        ]
        self.cost_infos = [
            CostInfo(
                num=10000.00,
                kind="手术费"
            )
        ]

# 测试 create_medical_record 函数
def test_create_medical_record():
    # 创建 medical_record_info 实例
    medical_record_info = MedicalRecordInfo()

    # 调用 create_medical_record 函数
    create_medical_record(medical_record_info)

    # 这里可以添加断言来验证数据库中的数据是否正确
    # 例如：assert medical_record_id 是正确的
    # 由于我们没有实际的数据库连接，这里只是模拟调用


if __name__=='__main__':
# 运行测试样例
    test_create_medical_record()

    #search_patients_by_info()
    #get_medical_records_by_info()
    #search_return_info()
    #search_borrow_info()
    #create_borrow_request()
    #create_return_request()
    #get_pending_requests()
    #change_request_status_to_approved()
