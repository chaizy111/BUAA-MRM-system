import pymysql
from pymysql import Error


#################################### 数据库操作 ##############################################
def make_connect():  # 建立数据库连接
    conn = pymysql.connect(
        # host='localhost',		# 主机名（或IP地址）
        # password='2003',  # 你本地的数据库密码,请自行更改
        host='110.42.33.194',  # 主机名（或IP地址）
        password='123456',  # 你本地的数据库密码,请自行更改
        port=3306,  # 端口号，默认为3306
        user='dba',  # 用户名
        charset='utf8mb4'  # 设置字符编码
    )
    conn.select_db("medical_record_management")  # 选择数据库
    cursor = conn.cursor()  # 创建游标对象
    # 获取mysql服务信息（测试连接，输出MySQL版本号）
    # print(conn.get_server_info())
    return conn, cursor


def break_connect(conn, cursor):  # 断开数据库连接
    cursor.close()
    conn.close()


##############################################################################################

#这个方法是患者查询使用的方法
def search_patients_by_info(search_info):
    conn, cursor = make_connect()
    try:
        result = search_ids_by_info(search_info, conn, cursor)
        records = []
        for r in result:
            records.append(r[0])
        record_ids = ', '.join(map(str, records))
        query = f"""
        SELECT * FROM Patient p
        JOIN MedicalRecord m ON m.PatientIDCardNumber = p.IDCardNumber 
        WHERE m.MedicalRecordNumber IN ({record_ids})
        """
        cursor.execute(query)
        patients = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get patient info.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return patients


#这个方法是病案查询使用的方法
def get_medical_records_by_info(search_info):
    conn, cursor = make_connect()
    try:
        result = search_ids_by_info(search_info, conn, cursor)
        records = []
        for r in result:
            records.append(r[0])
        record_ids = ''
        if records:
            record_ids = ', '.join(map(str, records))
        query = f"""
        SELECT * FROM MedicalRecord WHERE MedicalRecordNumber IN ({record_ids})
        """
        cursor.execute(query)
        medical_records = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when medical record info.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return medical_records


def search_ids_by_info(search_info, conn, cursor):
    query = """
        SELECT m.MedicalRecordNumber
        FROM MedicalRecord m
        JOIN Patient p ON m.PatientIDCardNumber = p.IDCardNumber
        JOIN Contact c ON p.IDCardNumber = c.PatientID
        JOIN Unit u ON m.UnitID = u.UnitID
        JOIN Disease d ON m.AdmissionDiagnosisID = d.DiseaseID OR m.DischargeDiagnosisID = d.DiseaseID OR m.PathologicalDiagnosisID = d.DiseaseID
        WHERE 1=1
        """
    conditions = []
    values = []

    if search_info.gender is not None:
        conditions.append("p.Gender = %s")
        values.append(search_info.gender)
    if search_info.medical_record_number is not None:
        conditions.append("m.MedicalRecordNumber = %s")
        values.append(search_info.medical_record_number)
    if search_info.patient_name is not None:
        conditions.append("p.Name LIKE %s")
        values.append(f"%{search_info.patient_name}%")
    if search_info.payment_method is not None:
        conditions.append("m.PayMentMethod LIKE %s")
        values.append(f"%{search_info.payment_method}%")
    if search_info.nationality is not None:
        conditions.append("p.Nationality LIKE %s")
        values.append(f"%{search_info.nationality}%")
    if search_info.ethnicity is not None:
        conditions.append("p.Ethnicity LIKE %s")
        values.append(f"%{search_info.ethnicity}%")
    if search_info.occupation is not None:
        conditions.append("p.Occupation LIKE %s")
        values.append(f"%{search_info.occupation}%")
    if search_info.address is not None:
        conditions.append("p.CurrentAddress LIKE %s")
        values.append(f"%{search_info.address}%")
    if search_info.phone is not None:
        conditions.append("p.Phone LIKE %s")
        values.append(f"%{search_info.phone}%")
    if search_info.contact_name is not None:
        conditions.append("c.Name LIKE %s")
        values.append(f"%{search_info.contact_name}%")
    if search_info.contact_phone is not None:
        conditions.append("c.Phone LIKE %s")
        values.append(f"%{search_info.contact_phone}%")
    if search_info.contact_address is not None:
        conditions.append("c.Address LIKE %s")
        values.append(f"%{search_info.contact_address}%")
    if search_info.birth_from and search_info.birth_to:
        conditions.append("p.BirthDate BETWEEN %s AND %s")
        values.extend([search_info.birth_from, search_info.birth_to])
    if search_info.admission_time_from and search_info.admission_time_to:
        conditions.append("m.AdmissionDate BETWEEN %s AND %s")
        values.extend([search_info.admission_time_from, search_info.admission_time_to])
    if search_info.discharge_time_from and search_info.discharge_time_to:
        conditions.append("m.DischargeDate BETWEEN %s AND %s")
        values.extend([search_info.discharge_time_from, search_info.discharge_time_to])
    if search_info.department is not None:
        conditions.append("u.Name LIKE %s")
        values.append(f"%{search_info.department}%")
    if search_info.patient_age_from and search_info.patient_age_to:
        conditions.append("p.Age BETWEEN %s AND %s")
        values.extend([search_info.patient_age_from, search_info.patient_age_to])
    if search_info.disease_name is not None:
        conditions.append("d.Description LIKE %s")
        values.append(f"%{search_info.disease_name}%")
    if search_info.days_from and search_info.days_to:
        conditions.append("DATEDIFF(m.DischargeDate, m.AdmissionDate) BETWEEN %s AND %s")
        values.extend([search_info.days_from, search_info.days_to])

    if conditions:
        query += " AND " + " AND ".join(conditions)

    cursor.execute(query, values)
    records = cursor.fetchall()
    return records


#使用的时候要使用多次，根据下边诊断类型来决定最后一个参数，先查所有入院诊断为该疾病的病案，再查所有出院诊断为该疾病的病案，最后查病理诊断为该疾病的病案，最后组合后返回
def search_disease_info(medical_record_number=None, patient_name=None, gender=None,
                        admission_date_from=None, admission_date_to=None,
                        discharge_date_from=None, discharge_date_to=None,
                        unit_name=None, disease_name=None, diagnosis_type=None):
    conn, cursor = make_connect()
    try:
        query = """
        SELECT m.MedicalRecordNumber, p.Name, p.Gender, m.AdmissionDate, u.Name AS UnitName, DATEDIFF(m.DischargeDate, m.AdmissionDate) AS HospitalizationDays,
                d.DiseaseID, d.Description AS DiseaseName
        FROM MedicalRecord m
        JOIN Patient p ON m.PatientIDCardNumber = p.IDCardNumber
        JOIN Unit u ON m.UnitID = u.UnitID
        JOIN Disease d ON m.AdmissionDiagnosisID = d.DiseaseID OR m.DischargeDiagnosisID = d.DiseaseID OR m.PathologicalDiagnosisID = d.DiseaseID
        WHERE 1=1
        """
        conditions = []
        values = []

        if medical_record_number is not None:
            conditions.append("m.MedicalRecordNumber = %s")
            values.append(medical_record_number)
        if patient_name is not None:
            conditions.append("p.Name LIKE %s")
            values.append(f"%{patient_name}%")
        if gender is not None:
            conditions.append("p.Gender = %s")
            values.append(gender)
        if admission_date_from and admission_date_to:
            conditions.append("m.AdmissionDate BETWEEN %s AND %s")
            values.extend([admission_date_from, admission_date_to])
        if discharge_date_from and discharge_date_to:
            conditions.append("m.DischargeDate BETWEEN %s AND %s")
            values.extend([discharge_date_from, discharge_date_to])
        if unit_name is not None:
            conditions.append("u.Name LIKE %s")
            values.append(f"%{unit_name}%")
        if disease_name is not None:
            conditions.append("d.Description LIKE %s")
            values.append(f"%{disease_name}%")
        if diagnosis_type == 'Admission':
            conditions.append("m.AdmissionDiagnosisID IS NOT NULL")
        elif diagnosis_type == 'Discharge':
            conditions.append("m.DischargeDiagnosisID IS NOT NULL")
        elif diagnosis_type == 'Pathological':
            conditions.append("m.PathologicalDiagnosisID IS NOT NULL")

        if conditions:
            query += " AND " + " AND ".join(conditions)

        cursor.execute(query, values)
        records = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get disease info.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return records


def search_surgery_info(medical_record_number=None, patient_name=None, patient_gender=None, payment_method=None,
                        admission_date_from=None, admission_date_to=None,
                        discharge_date_from=None, discharge_date_to=None,
                        unit_name=None, age_from=None, age_to=None, days_from=None, days_to=None,
                        surgery_name=None, surgery_date_from=None, surgery_date_to=None, surgeon_name=None
                        ):
    conn, cursor = make_connect()
    try:
        base_query = """
        SELECT m.MedicalRecordNumber, p.Name AS PatientName, p.Gender, s.SurgeryDate, s.SurgeryName, st.Name AS SurgeonName
        FROM MedicalRecord m
        JOIN Patient p ON m.PatientIDCardNumber = p.IDCardNumber
        JOIN Surgery s ON m.MedicalRecordNumber = s.MedicalRecordID
        JOIN Unit u ON m.UnitID = u.UnitID
        JOIN Staff st ON s.SurgeonID = st.StaffID
        WHERE 1=1
        """
        conditions = []
        values = []

        # 根据查询条件添加查询条件
        if medical_record_number:
            conditions.append("m.MedicalRecordNumber = %s")
            values.append(medical_record_number)
        if patient_name:
            conditions.append("p.Name LIKE %s")
            values.append(f"%{patient_name}%")
        if patient_gender:
            conditions.append("p.Gender = %s")
            values.append(patient_gender)
        if payment_method:
            conditions.append("m.PaymentMethod LIKE %s")
            values.append(payment_method)
        if admission_date_from and admission_date_to:
            conditions.append("m.AdmissionDate BETWEEN %s AND %s")
            values.extend([admission_date_from, admission_date_to])
        if discharge_date_from and discharge_date_to:
            conditions.append("m.DischargeDate BETWEEN %s AND %s")
            values.extend([discharge_date_from, discharge_date_to])
        if unit_name:
            conditions.append("u.Name LIKE %s")
            values.append(f"%{unit_name}%")
        if age_from and age_to:
            conditions.append("p.Age BETWEEN %s AND %s")
            values.extend([age_from, age_to])
        if days_from and days_to:
            conditions.append("DATEDIFF(m.DischargeDate, m.AdmissionDate) BETWEEN %s AND %s")
            values.append([days_from, days_to])
        if surgery_name:
            conditions.append("s.SurgeryName LIKE %s")
            values.append(f"%{surgery_name}%")
        if surgery_date_from and surgery_date_to:
            conditions.append("s.SurgeryDate BETWEEN %s AND %s")
            values.extend([surgery_date_from, surgery_date_to])
        if surgeon_name:
            conditions.append("st.Name LIKE %s")
            values.append(surgeon_name)

        # 将条件连接为一个字符串
        if conditions:
            condition_str = " AND ".join(conditions)
            base_query += f" AND {condition_str}"

        # 执行查询
        cursor.execute(base_query, values)
        surgery_details = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get surgery info.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return surgery_details


def search_return_info(medical_record_number=None, payment_method=None,
                       patient_name=None, borrower_name=None,
                       borrower_phone=None, borrower_id_card_number=None,
                       department=None, borrow_reason=None,
                       start_time=None, end_time=None):
    conn, cursor = make_connect()
    try:
        base_query = """
            SELECT m.MedicalRecordNumber, p.Name AS PatientName, p.Gender, u.Name AS UnitName, br.BorrowedBy, r.ReturnDate, br.BorrowReason
            FROM MedicalRecord m
            JOIN Patient p ON m.PatientIDCardNumber = p.IDCardNumber
            JOIN MedicalRecordBorrow br ON m.MedicalRecordNumber = br.MedicalRecordNumber
            JOIN MedicalRecordReturn r ON br.MedicalRecordNumber = r.MedicalRecordNumber AND br.BorrowedBy = r.ReturnedBy
            JOIN Unit u ON r.UnitID = u.UnitID
            WHERE 1=1
            """
        conditions = []
        values = []

        # 构建查询条件
        if medical_record_number:
            conditions.append("m.MedicalRecordNumber LIKE %s")
            values.append(f"%{medical_record_number}%")
        if payment_method:
            conditions.append("m.PaymentMethod LIKE %s")
            values.append(f"%{payment_method}%")
        if patient_name:
            conditions.append("p.Name LIKE %s")
            values.append(f"%{patient_name}%")
        if borrower_name:
            conditions.append("br.BorrowedBy LIKE %s")
            values.append(f"%{borrower_name}%")
        if borrower_phone:
            conditions.append("br.ContactPhone LIKE %s")
            values.append(f"%{borrower_phone}%")
        if borrower_id_card_number:
            conditions.append("br.IDCardNumber LIKE %s")
            values.append(f"%{borrower_id_card_number}%")
        if department:
            conditions.append("u.Name LIKE %s")
            values.append(f"%{department}%")
        if borrow_reason:
            conditions.append("br.BorrowReason LIKE %s")
            values.append(f"%{borrow_reason}%")
        if start_time and end_time:
            conditions.append("r.ReturnDate BETWEEN %s AND %s")
            values.extend([start_time, end_time])

        # 将条件连接为一个字符串
        if conditions:
            condition_str = " AND ".join(conditions)
            base_query += f" AND {condition_str}"

        cursor.execute(base_query, values)
        records = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get return info.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return records


def search_borrow_info(medical_record_number=None, payment_method=None, patient_name=None,
                       borrower_name=None, borrower_phone=None, borrower_id_card_number=None,
                       department=None, borrow_reason=None,
                       start_time=None, end_time=None, approver=None):
    conn, cursor = make_connect()
    try:
        base_query = """
        SELECT m.MedicalRecordNumber, p.Name AS PatientName, p.Gender, u.Name AS UnitName, br.BorrowedBy, br.BorrowDate, br.BorrowReason, br.Approver AS ApprovedByName
        FROM MedicalRecord m
        JOIN Patient p ON m.PatientIDCardNumber = p.IDCardNumber
        JOIN MedicalRecordBorrow br ON m.MedicalRecordNumber = br.MedicalRecordNumber
        JOIN Unit u ON br.UnitID = u.UnitID
        WHERE 1=1
        """
        conditions = []
        values = []

        # 构建查询条件
        if medical_record_number:
            conditions.append("m.MedicalRecordNumber LIKE %s")
            values.append(f"%{medical_record_number}%")
        if payment_method:
            conditions.append("m.PaymentMethod LIKE %s")
            values.append(f"%{payment_method}%")
        if patient_name:
            conditions.append("p.Name LIKE %s")
            values.append(f"%{patient_name}%")
        if borrower_name:
            conditions.append("br.BorrowedBy LIKE %s")
            values.append(f"%{borrower_name}%")
        if borrower_phone:
            conditions.append("br.ContactPhone LIKE %s")
            values.append(f"%{borrower_phone}%")
        if borrower_id_card_number:
            conditions.append("br.IDCardNumber LIKE %s")
            values.append(f"%{borrower_id_card_number}%")
        if department:
            conditions.append("u.Name LIKE %s")
            values.append(f"%{department}%")
        if borrow_reason:
            conditions.append("br.BorrowReason LIKE %s")
            values.append(f"%{borrow_reason}%")
        if start_time and end_time:
            conditions.append("br.BorrowDate BETWEEN %s AND %s")
            values.extend([start_time, end_time])
        if approver:
            conditions.append("br.Approver LIKE %s")
            values.append(f"%{approver}%")

        if conditions:
            condition_str = " AND ".join(conditions)
            base_query += f" AND {condition_str}"

        cursor.execute(base_query, values)
        records = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get borrow info.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return records


def search_admission_info(admission_start_date, admission_end_date, unit_name):
    conn, cursor = make_connect()
    try:
        query = """
        SELECT m.MedicalRecordNumber, p.Name, p.Gender, m.AdmissionDate, u.Name AS UnitName
        FROM MedicalRecord m
        JOIN Patient p ON m.PatientIDCardNumber = p.IDCardNumber
        JOIN Unit u ON m.UnitID = u.UnitID
        WHERE m.AdmissionDate BETWEEN %s AND %s 
        """
        if unit_name:
            query.join("AND u.Name = %s")
            cursor.execute(query, (admission_start_date, admission_end_date, unit_name))
        else:
            cursor.execute(query, (admission_start_date, admission_end_date))
        admission_info = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get admission info.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return admission_info


def search_discharge_info(medical_record_number=None, unit_name=None, start_date=None, end_date=None):
    conn, cursor = make_connect()
    try:
        query = """
        SELECT 
            m.MedicalRecordNumber, p.Name, p.Gender, u.Name, SUM(c.Amount) AS TotalAmount,  
            m.AdmissionDate, m.DischargeDate, DATEDIFF(m.DischargeDate, m.AdmissionDate) AS hospitalization_days
        FROM MedicalRecord m
        JOIN Patient p ON m.PatientIDCardNumber = p.IDCardNumber
        JOIN Unit u ON m.UnitID = u.UnitID
        LEFT JOIN Cost c ON m.MedicalRecordNumber = c.MedicalRecordID
        WHERE 1=1"""
        conditions = []
        values = []

        if medical_record_number:
            conditions.append("m.MedicalRecordNumber = %s")
            values.append(medical_record_number)
        if unit_name:
            conditions.append("u.Name = %s")
            values.append(unit_name)
        if start_date and end_date:
            conditions.append("m.AdmissionDate >= %s AND m.DischargeDate <= %s")
            values.extend([start_date, end_date])

        if conditions:
            query += " AND " + " AND ".join(conditions)

        query += "GROUP BY m.MedicalRecordNumber, p.Name, p.Gender, u.Name, m.AdmissionDate, m.DischargeDate"
        cursor.execute(query, values)
        results = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get discharge info.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return results
