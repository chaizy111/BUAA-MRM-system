import pymysql

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
    return (conn,cursor)


def break_connect(conn, cursor): # 断开数据库连接
    cursor.close()
    conn.close()
##############################################################################################

def get_staffId_by_name(name):
    conn, cursor = make_connect()
    query = """
            SELECT StaffID FROM Staff WHERE Name = %s;
        """
    cursor.execute(query, (name,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    break_connect(conn, cursor)
    if result:
        return result[0]  # 返回StaffID
    else:
        return None  # 如果没有找到，返回None

def get_staffName_by_id(id):
    conn, cursor = make_connect()
    query = """
            SELECT Name FROM Staff WHERE StaffID = %s;
        """
    cursor.execute(query, (id,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    break_connect(conn, cursor)
    if result:
        return result[0]  # 返回Name
    else:
        return None  # 如果没有找到，返回None

def get_wardId_by_name(name):
    conn, cursor = make_connect()
    query = """
            SELECT WardID FROM Ward WHERE Description = %s;
        """
    cursor.execute(query, (name,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    break_connect(conn, cursor)
    if result:
        return result[0]  # 返回StaffID
    else:
        return None  # 如果没有找到，返回None


def get_wardName_by_id(id):
    conn, cursor = make_connect()
    query = """
            SELECT Description FROM Ward WHERE WardID = %s;
        """
    cursor.execute(query, (id,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    break_connect(conn, cursor)
    if result:
        return result[0]  # 返回Name
    else:
        return None  # 如果没有找到，返回None


def get_unitId_by_name(name):
    conn, cursor = make_connect()
    query = """
            SELECT UnitID FROM Unit WHERE Name = %s;
            """
    cursor.execute(query, (name,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    break_connect(conn, cursor)
    if result:
        return result[0]  # 返回UnitID
    else:
        return None  # 如果没有找到，返回None

def get_unitName_by_id(id):
    conn, cursor = make_connect()
    query = """
            SELECT UnitID FROM Unit WHERE Name = %s;
            """
    cursor.execute(query, (id,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    break_connect(conn, cursor)
    if result:
        return result[0]  # 返回Name
    else:
        return None  # 如果没有找到，返回None

def get_medicalRecordId_by_patientId(patientId):
    conn, cursor = make_connect()
    query = """
            SELECT MedicalRecordNumber FROM MedicalRecord WHERE PatientIDCardNumber = %s;
            """
    cursor.execute(query, (patientId,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    break_connect(conn, cursor)
    if result:
        return result[0]  # 返回MedicalRecordID
    else:
        return None  # 如果没有找到，返回None

def get_medicalRecord_by_id(id):
    conn, cursor = make_connect()
    query = "SELECT * FROM MedicalRecord WHERE MedicalRecordNumber = %s"
    cursor.execute(query, (id,))
    record = cursor.fetchone()  # 获取查询结果的第一行
    break_connect(conn, cursor)
    if record:
        return record  # 返回病案信息的字典
    else:
        return None  # 如果没有找到，返回None

def if_patient_exist(patientId):
    conn, cursor = make_connect()
    query = "SELECT EXISTS (SELECT 1 FROM Patient WHERE IDCardNumber = %s)"
    cursor.execute(query, (patientId,))
    result = cursor.fetchone()
    break_connect(conn, cursor)
    return result[0]  # 返回True或False

def if_medical_record_exist(medicalRecordId):
    conn, cursor = make_connect()
    query = "SELECT EXISTS (SELECT 1 FROM MedicalRecord WHERE MedicalRecordNumber = %s)"
    cursor.execute(query, (medicalRecordId,))
    result = cursor.fetchone()
    break_connect(conn, cursor)
    return result[0]  # 返回True或False

def get_diseaseName_by_id(diseaseId):
    conn, cursor = make_connect()
    query = "SELECT Description FROM Disease WHERE DiseaseID = %s"
    cursor.execute(query, (diseaseId,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    break_connect(conn, cursor)
    if result:
        return result[0]  # 返回疾病名称
    else:
        return None  # 如果没有找到，返回None