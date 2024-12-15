import pymysql

def get_staffId_by_name(name, conn, cursor):
    query = """
            SELECT StaffID FROM Staff WHERE Name = %s;
        """
    cursor.execute(query, (name,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    if result:
        return result[0]  # 返回StaffID
    else:
        return None  # 如果没有找到，返回None

def get_staffName_by_id(id, conn, cursor):
    query = """
            SELECT Name FROM Staff WHERE StaffID = %s;
        """
    cursor.execute(query, (id,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    if result:
        return result[0]  # 返回Name
    else:
        return None  # 如果没有找到，返回None

def get_wardId_by_name(name, conn, cursor):
    query = """
            SELECT WardID FROM Ward WHERE Description = %s;
        """
    cursor.execute(query, (name,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    if result:
        return result[0]  # 返回StaffID
    else:
        return None  # 如果没有找到，返回None


def get_wardName_by_id(id, conn, cursor):
    query = """
            SELECT Description FROM Ward WHERE WardID = %s;
        """
    cursor.execute(query, (id,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    if result:
        return result[0]  # 返回Name
    else:
        return None  # 如果没有找到，返回None


def get_unitId_by_name(name, conn, cursor):
    query = """
            SELECT UnitID FROM Unit WHERE Name = %s;
            """
    cursor.execute(query, (name,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    if result:
        return result[0]  # 返回UnitID
    else:
        return None  # 如果没有找到，返回None

def get_unitName_by_id(id, conn, cursor):
    query = """
            SELECT UnitID FROM Unit WHERE Name = %s;
            """
    cursor.execute(query, (id,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    if result:
        return result[0]  # 返回Name
    else:
        return None  # 如果没有找到，返回None

def get_medicalRecordId_by_patientId(patientId, conn, cursor):
    query = """
            SELECT MedicalRecordNumber FROM MedicalRecord WHERE PatientIDCardNumber = %s;
            """
    cursor.execute(query, (patientId,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    if result:
        return result[0]  # 返回MedicalRecordID
    else:
        return None  # 如果没有找到，返回None

def get_medicalRecord_by_id(id, conn, cursor):
    query = "SELECT * FROM MedicalRecord WHERE MedicalRecordNumber = %s"
    cursor.execute(query, (id,))
    record = cursor.fetchone()  # 获取查询结果的第一行
    if record:
        return record  # 返回病案信息的字典
    else:
        return None  # 如果没有找到，返回None

def if_patient_exist(patientId, conn, cursor):
    query = "SELECT EXISTS (SELECT 1 FROM Patient WHERE IDCardNumber = %s)"
    cursor.execute(query, (patientId,))
    result = cursor.fetchone()
    return result[0]  # 返回True或False

def if_medical_record_exist(medicalRecordId, conn, cursor):
    query = "SELECT EXISTS (SELECT 1 FROM MedicalRecord WHERE MedicalRecordNumber = %s)"
    cursor.execute(query, (medicalRecordId,))
    result = cursor.fetchone()
    return result[0]  # 返回True或False

def get_diseaseName_by_id(diseaseId, conn, cursor):
    query = "SELECT Description FROM Disease WHERE DiseaseID = %s"
    cursor.execute(query, (diseaseId,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    if result:
        return result[0]  # 返回疾病名称
    else:
        return None  # 如果没有找到，返回None