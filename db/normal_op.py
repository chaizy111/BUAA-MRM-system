from pymysql import Error

from db.assist_op import *
from intermediate_data_structure import medical_record_info
from intermediate_data_structure import patient_info
from intermediate_data_structure import contact_info
from intermediate_data_structure import cost_info
from intermediate_data_structure import surgery_info
from intermediate_data_structure import ward_info
import pymysql

from intermediate_data_structure.contact_info import ContactInfo
from intermediate_data_structure.cost_info import CostInfo
from intermediate_data_structure.medical_record_info import MedicalRecordInfo
from intermediate_data_structure.patient_info import PatientInfo
from intermediate_data_structure.surgery_info import SurgeryInfo
from intermediate_data_structure.ward_info import WardInfo


#################################### 数据库操作 ##############################################
def make_connect():     # 建立数据库连接
    conn = pymysql.connect(
        # host='localhost',		# 主机名（或IP地址）
        # password='2003',  # 你本地的数据库密码,请自行更改
        host='110.42.33.194',		# 主机名（或IP地址）
        password='123456',  # 你本地的数据库密码,请自行更改
        port=3306,				# 端口号，默认为3306
        user='dba',			# 用户名
        charset='utf8mb4'  		# 设置字符编码
    )
    conn.select_db("medical_record_management") # 选择数据库
    cursor = conn.cursor() # 创建游标对象
    # 获取mysql服务信息（测试连接，输出MySQL版本号）
    # print(conn.get_server_info())
    return (conn, cursor)


def break_connect(conn, cursor): # 断开数据库连接
    cursor.close()
    conn.close()
##############################################################################################

def create_medical_record(medical_record_info):
    conn, cursor = make_connect()
    try:
        create_patient(medical_record_info.patient_info, conn, cursor)
        create_contact(medical_record_info.contact_info, conn, cursor)
        insert_query = """
            INSERT INTO MedicalRecord (PatientIDCardNumber, 
                                        AdmissionDate, 
                                        DischargeDate, 
                                        UnitID,
                                        AdmissionDiagnosisID, 
                                        DischargeDiagnosisID, 
                                        PathologicalDiagnosisID, 
                                        TreatStaffID, 
                                        BloodType,
                                        PaymentMethod)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        cursor.execute(insert_query, (medical_record_info.patient_info.id_card_number,
                                        medical_record_info.admission_date,
                                        medical_record_info.discharge_date,
                                        get_unitId_by_name(medical_record_info.unit_name, conn, cursor),
                                        medical_record_info.admission_diagnosis_id,
                                        medical_record_info.discharge_diagnosis_id,
                                        medical_record_info.pathological_diagnosis_id,
                                        get_staffId_by_name(medical_record_info.doctor_name, conn, cursor),
                                        medical_record_info.blood_type,
                                        medical_record_info.payment_method
                                  ))
        conn.commit()
        medical_record_id = get_medicalRecordId_by_patientId(medical_record_info.patient_info.id_card_number, conn, cursor)
        for surgery_info in medical_record_info.surgery_infos:
            create_surgery(medical_record_id, surgery_info, conn, cursor)
        for ward_info in medical_record_info.ward_infos:
            create_recordAndWard(medical_record_id, ward_info, conn, cursor)
        for cost_info in medical_record_info.cost_infos:
            create_cost(medical_record_id, cost_info, conn, cursor)
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when create medical record.")
        break_connect(conn, cursor)
        return False
    break_connect(conn, cursor)
    return True

def create_patient(patient_info, conn, cursor):
    if ~if_patient_exist(patient_info.id_card_number, conn, cursor): #避免重复新建
        insert_query = """
                INSERT INTO Patient (Name, Gender, BirthDate, Age, 
                                    Nationality, PlaceOfBirth, Ethnicity, IDCardNumber, 
                                    Occupation, MaritalStatus, CurrentAddress, Phone, PostalCode, HouseholdAddress)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
        cursor.execute(insert_query, (patient_info.name, patient_info.gender, patient_info.birth_date, patient_info.age,
                                  patient_info.nationality, patient_info.place_of_birth, patient_info.ethnicity, patient_info.id_card_number,
                                  patient_info.occupation, patient_info.marital_status, patient_info.current_address, patient_info.phone, patient_info.postal_code,patient_info.household_address))
        conn.commit()

def create_contact(contact_info, conn, cursor):
    insert_query = """
            INSERT INTO Contact (PatientID, Name, Relationship, Address, Phone)
            VALUES (%s, %s, %s, %s, %s)
            """
    cursor.execute(insert_query, (contact_info.patient_id, contact_info.name,
                                  contact_info.relationship, contact_info.address,contact_info.phone))
    conn.commit()

def create_surgery(medical_record_id, surgery_info, conn, cursor):
    insert_query = """
            INSERT INTO Surgery (MedicalRecordID, SurgeryDate, SurgeryName, 
                                    SurgeonID, AssistantSurgeonID)
            VALUES (%s, %s, %s, %s, %s)
            """
    cursor.execute(insert_query, (medical_record_id, surgery_info.surgery_date, surgery_info.surgery_name,
                                        get_staffId_by_name(surgery_info.surgeon_name, conn, cursor), get_staffName_by_id(surgery_info.assistant_surgeon_name, conn, cursor)))
    conn.commit()


def create_recordAndWard(medical_record_id, ward_info, conn, cursor):
    insert_query = """
            INSERT INTO MedicalRecordWards (MedicalRecordID, WardID, StartTime, EndTime)
            VALUES (%s, %s, %s, %s)
            """
    cursor.execute(insert_query, (medical_record_id, get_wardId_by_name(ward_info.ward_name, conn, cursor), ward_info.start_time, ward_info.end_time))
    conn.commit()

def create_cost(medical_record_id, cost_info, conn, cursor):
    insert_query = """
            INSERT INTO Cost (MedicalRecordID, Amount, Kind)
            VALUES (%s, %s, %s)
            """
    cursor.execute(insert_query, (medical_record_id, cost_info.num, cost_info.kind))
    conn.commit()

#以上为add病案过程中所用到的所有方法

def get_record_by_recordID(recordID):
    conn, cursor = make_connect()
    try:
        record = get_medicalRecord_by_id(recordID, conn, cursor)
        medical_record_info = MedicalRecordInfo(
        patient_info=get_patient_info(record[1], conn, cursor),
        contact_info=get_contact_info(record[1], conn, cursor),
        surgery_infos=get_surgery_infos(recordID, conn, cursor),
        ward_infos=get_ward_infos(recordID, conn, cursor),
        cost_infos=get_cost_infos(recordID, conn, cursor),
        admission_date=record[2],
        discharge_date=record[3],
        unit_name=get_unitName_by_id(record[4], conn, cursor),
        admission_diagnosis_id=record[5],
        discharge_diagnosis_id=record[6],
        pathological_diagnosis_id=record[7],
        doctor_name=get_staffId_by_name(record[8], conn, cursor),
        blood_type=record[9],
        payment_method=record[10]
        )
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get medical record")
        break_connect(conn, cursor)
        return None
    break_connect(conn, cursor)
    return medical_record_info

def get_patient_info(patientId, conn, cursor):
    query = "SELECT * FROM Patient WHERE IDCardNumber = %s"
    cursor.execute(query, (patientId,))
    patient_data = cursor.fetchone()  # 获取查询结果的第一行
    return PatientInfo(patient_data[0], patient_data[1], patient_data[2], patient_data[3],
                       patient_data[4], patient_data[5], patient_data[6], patient_data[7],
                       patient_data[8], patient_data[9], patient_data[10], patient_data[11],
                       patient_data[12], patient_data[13])

def get_contact_info(patientId, conn, cursor):
    query = "SELECT * FROM Contact WHERE PatientID = %s"
    cursor.execute(query, (patientId,))
    data = cursor.fetchone()  # 获取所有匹配的联系人信息
    return ContactInfo(name=data[1], relationship=data[2], address=data[3], phone=data[4], patient_id=patientId)


def get_surgery_infos(medicalRecordId, conn, cursor):
    query = "SELECT * FROM Surgery WHERE MedicalRecordID = %s"
    cursor.execute(query, (medicalRecordId,))
    datas = cursor.fetchall()
    surgery_infos = []
    for data in datas:
        surgery_info = SurgeryInfo(
            surgery_date=data[2],
            surgery_name=data[3],
            surgeon_name=get_staffName_by_id(data[4], conn, cursor),
            assistant_surgeon_name=get_staffName_by_id(data[5], conn, cursor)
        )
        surgery_infos.append(surgery_info)
    return surgery_infos

def get_ward_infos(medicalRecordId, conn, cursor):
    query = "SELECT * FROM MedicalRecordWards WHERE MedicalRecordID = %s"
    cursor.execute(query, (medicalRecordId,))
    datas = cursor.fetchall()
    ward_infos = []
    for data in datas:
        ward_info = WardInfo(
            ward_name=get_wardName_by_id(data[1], conn, cursor),
            start_time=data[2],
            end_time=data[3]
        )
        ward_infos.append(ward_info)
    return ward_infos

def get_cost_infos(medicalRecordId, conn, cursor):
    query = "SELECT * FROM Cost WHERE MedicalRecordID = %s"
    cursor.execute(query, (medicalRecordId,))
    datas = cursor.fetchall()
    cost_infos = []
    for data in datas:
        cost_info = CostInfo(
            kind=data[3],
            num=data[2]
        )
        cost_infos.append(cost_info)
    return cost_infos

#以上为修改过程中使用的方法

#根据病案号删除，注意删除与其相关的所有信息
def delete_record_by_recordID(recordID):
    conn, cursor = make_connect()
    try:
        cursor.execute("SELECT PatientIDCardNumber FROM MedicalRecord WHERE MedicalRecordNumber = %s", (recordID,))
        patient_id_card_number = cursor.fetchone()[0]

        # 删除借阅信息
        cursor.execute("DELETE FROM MedicalRecordBorrow WHERE MedicalRecordNumber = %s", (recordID,))
        # 删除归还信息
        cursor.execute("DELETE FROM MedicalRecordReturn WHERE MedicalRecordNumber = %s", (recordID,))
        # 删除费用信息
        cursor.execute("DELETE FROM Cost WHERE MedicalRecordID = %s", (recordID,))
        # 删除手术信息
        cursor.execute("DELETE FROM Surgery WHERE MedicalRecordID = %s", (recordID,))
        # 删除病房信息
        cursor.execute("DELETE FROM MedicalRecordWards WHERE MedicalRecordID = %s", (recordID,))
        # 删除联系人信息
        cursor.execute("DELETE FROM Contact WHERE PatientID = %s", (patient_id_card_number,))
        # 删除病案信息
        cursor.execute("DELETE FROM MedicalRecord WHERE MedicalRecordNumber = %s", (recordID,))
        # 删除病人信息
        cursor.execute("DELETE FROM Patient WHERE IDCardNumber = %s", (patient_id_card_number,))

        conn.commit()
    except Error as e:
        print(f"The error '{e}' occurred when deleting the medical record and related information.")
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        break_connect(conn, cursor)
        return False
    break_connect(conn, cursor)
    return True
#借阅方法
def create_borrow_request(br_info):
    conn, cursor = make_connect()
    try:
        insert_query = """
            INSERT INTO MedicalRecordBorrow (MedicalRecordNumber, BorrowDate, BorrowedBy, 
                                            UnitID, IDCardNumber, BorrowReason, 
                                            ContactPhone, Status)
            VALUES (%s, NOW(), %s, %s, %s, %s, %s, 'Pending')
            """
        cursor.execute(insert_query, (br_info.medical_record_id, br_info.borrowed_by,
                                  get_unitId_by_name(br_info.unit_name, conn, cursor),
                                  br_info.IDcard_num, br_info.borrow_reason,
                                  br_info.contact_phone))
        conn.commit()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when create borrow request.")
        break_connect(conn, cursor)
        return False
    break_connect(conn, cursor)
    return True

#归还方法，与借阅不同，其没有状态属性，如果对于该病案号借阅次数比归还次数多就可以归还
def create_return_request(br_info):
    conn, cursor = make_connect()
    try:
        cursor.execute("SELECT COUNT(*) FROM MedicalRecordBorrow WHERE MedicalRecordNumber = %s", (br_info.medical_record_id, ))
        borrow_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM MedicalRecordReturn WHERE MedicalRecordNumber = %s", (br_info.medical_record_id, ))
        return_count = cursor.fetchone()[0]

        if borrow_count > return_count:
            # 插入归还记录
            insert_query = """
                INSERT INTO MedicalRecordReturn (MedicalRecordNumber, ReturnDate, 
                                                 ReturnedBy, UnitID, IDCardNumber, ContactPhone)
                VALUES (%s, NOW(), %s, %s, %s, %s)
                """
            cursor.execute(insert_query, (
                br_info.medical_record_id, br_info.borrowed_by,
                get_unitId_by_name(br_info.unit_name, conn, cursor), br_info.IDcard_num, br_info.contact_phone))
            conn.commit()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when create return request.")
        break_connect(conn, cursor)
        return False
    break_connect(conn, cursor)
    return True

#借阅请求处理有关方法
def get_pending_requests():
    conn, cursor = make_connect()
    try:
        cursor = conn.cursor()
        query = """
            SELECT * FROM MedicalRecordBorrow WHERE Status = 'Pending'
            """
        cursor.execute(query)
        pending_borrows = cursor.fetchall()  # 获取所有匹配的记录
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get pending request.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return pending_borrows

def change_request_status_to_approved(borrow_request_ids, username):
    conn, cursor = make_connect()
    try:
        record_id_conditions = ', '.join(map(str, borrow_request_ids))
        update_query = f"""
            UPDATE MedicalRecordBorrow 
            SET Status = 'Approved' , Approver = %s
            WHERE BorrowID IN ({record_id_conditions})
            """
        cursor.execute(update_query, (username,))
        conn.commit()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when change request status to approved.")
        break_connect(conn, cursor)
        return False
    break_connect(conn, cursor)
    return True

def change_request_status_to_rejected(borrow_request_ids, username):
    conn, cursor = make_connect()
    try:
        record_id_conditions = ', '.join(map(str, borrow_request_ids))
        update_query = f"""
            UPDATE MedicalRecordBorrow 
            SET Status = 'Rejected' , Approver = %s
            WHERE BorrowID IN ({record_id_conditions})
            """
        cursor.execute(update_query, (username,))
        conn.commit()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when change request status to rejected.")
        break_connect(conn, cursor)
        return False
    break_connect(conn, cursor)
    return True
