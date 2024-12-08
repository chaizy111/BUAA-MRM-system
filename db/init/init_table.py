import pymysql
import xlrd
import openpyxl

#################################### 数据库操作 ##############################################
def make_connect():     # 建立数据库连接
    conn = pymysql.connect(
        host='localhost',		# 主机名（或IP地址）
        port=3306,				# 端口号，默认为3306
        user='root',			# 用户名
        password='2003',	# 你本地的数据库密码,请自行更改
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
def create_patients_table(conn, cursor):
    create_patients_table_query = """
       CREATE TABLE IF NOT EXISTS Patient (
           Name VARCHAR(255) NOT NULL,
           Gender ENUM('1', '2') NOT NULL,
           BirthDate DATE NOT NULL,
           Age INT,
           Nationality VARCHAR(50),
           PlaceOfBirth VARCHAR(255),
           Ethnicity VARCHAR(50),
           IDCardNumber VARCHAR(18) UNIQUE NOT NULL PRIMARY KEY,
           Occupation VARCHAR(100),
           MaritalStatus ENUM('Married', 'Single', 'Divorced', 'Widowed'),
           CurrentAddress TEXT,
           Phone VARCHAR(20),
           PostalCode VARCHAR(10),
           HouseholdAddress TEXT
       );
       """
    cursor.execute(create_patients_table_query)
    conn.commit()

def create_contact_table(conn, cursor):
    create_contact_table_query = """
    CREATE TABLE IF NOT EXISTS Contact (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        PatientID VARCHAR(18),
        Name VARCHAR(255) NOT NULL,
        Relationship VARCHAR(50),
        Address TEXT,
        Phone VARCHAR(20),
        FOREIGN KEY (PatientID) REFERENCES Patient(IDCardNumber)
    );
    """
    cursor.execute(create_contact_table_query)
    conn.commit()

def create_medical_record_table(conn, cursor):
    create_medical_record_table_query = """
       CREATE TABLE IF NOT EXISTS MedicalRecord (
           MedicalRecordNumber INT AUTO_INCREMENT PRIMARY KEY,
           PatientIDCardNumber VARCHAR(18),
           AdmissionDate DATE,
           DischargeDate DATE, 
           UnitID INT,
           AdmissionDiagnosisID VARCHAR(255),
           DischargeDiagnosisID VARCHAR(255),
           PathologicalDiagnosisID VARCHAR(255),
           TreatStaffID INT,
           BloodType INT,
           PayMentMethod VARCHAR(50),
           FOREIGN KEY (PatientIDCardNumber) REFERENCES Patient(IDCardNumber),
           FOREIGN KEY (UnitID) REFERENCES Unit(UnitID),
           FOREIGN KEY (TreatStaffID) REFERENCES Staff(StaffID),
           FOREIGN KEY (AdmissionDiagnosisID) REFERENCES Disease(DiseaseID),
           FOREIGN KEY (DischargeDiagnosisID) REFERENCES Disease(DiseaseID),
           FOREIGN KEY (PathologicalDiagnosisID) REFERENCES Disease(DiseaseID),
           FOREIGN KEY (BloodType) REFERENCES BloodType(BloodTypeID)
       );
       """
    cursor.execute(create_medical_record_table_query)
    conn.commit()

def create_disease_table(conn, cursor):
    create_table_query = """
            CREATE TABLE IF NOT EXISTS Disease (
                DiseaseID VARCHAR(255) NOT NULL PRIMARY KEY,
                Description VARCHAR(255) NOT NULL
            );
            """
    cursor.execute(create_table_query)
    conn.commit()

def create_surgery_table(conn, cursor):
    create_surgery_table_query = """
        CREATE TABLE IF NOT EXISTS Surgery (
            SurgeryID INT AUTO_INCREMENT PRIMARY KEY,
            MedicalRecordID INT,
            SurgeryDate DATE NOT NULL,
            SurgeryName VARCHAR(255),
            SurgeonID INT,
            AssistantSurgeonID INT,
            FOREIGN KEY (MedicalRecordID) REFERENCES MedicalRecord(MedicalRecordNumber),
            FOREIGN KEY (SurgeonID) REFERENCES Staff(StaffID),
            FOREIGN KEY (AssistantSurgeonID) REFERENCES Staff(StaffID)
        );
        """
    cursor.execute(create_surgery_table_query)
    conn.commit()

def create_unit_table(conn, cursor):
    create_unit_table_query = """
        CREATE TABLE IF NOT EXISTS Unit (
            UnitID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255) NOT NULL
        );
        """
    cursor.execute(create_unit_table_query)
    conn.commit()

def create_ward_table(conn, cursor):
    create_ward_table_query = """
        CREATE TABLE IF NOT EXISTS Ward (
            WardID INT AUTO_INCREMENT PRIMARY KEY,
            UnitID INT,
            Description VARCHAR(255),
            FOREIGN KEY (UnitID) REFERENCES Unit(UnitID)
        );
        """
    cursor.execute(create_ward_table_query)
    conn.commit()

def create_recordAndWard_table(conn, cursor):
    create_medical_record_wards_table_query = """
        CREATE TABLE IF NOT EXISTS MedicalRecordWards (
            MedicalRecordID INT,
            WardID INT,
            StartTime DATETIME,
            EndTime DATETIME,
            PRIMARY KEY (MedicalRecordID, WardID),
            FOREIGN KEY (MedicalRecordID) REFERENCES MedicalRecord(MedicalRecordNumber),
            FOREIGN KEY (WardID) REFERENCES Ward(WardID)
        );
        """
    cursor.execute(create_medical_record_wards_table_query)
    conn.commit()

def create_cost_table(conn, cursor):
    create_cost_table_query = """
        CREATE TABLE IF NOT EXISTS Cost (
            CostID INT AUTO_INCREMENT PRIMARY KEY,
            MedicalRecordID INT,
            Amount DECIMAL(10, 2) NOT NULL,
            Kind VarChar(50),
            FOREIGN KEY (MedicalRecordID) REFERENCES MedicalRecord(MedicalRecordNumber)
        );
        """
    cursor.execute(create_cost_table_query)
    conn.commit()

def create_staff_table(conn, cursor):
    create_staff_table_query = """
        CREATE TABLE IF NOT EXISTS Staff (
            StaffID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            Position VARCHAR(255),
            UnitID INT,
            FOREIGN KEY (UnitID) REFERENCES Unit(UnitID)
        );
        """
    cursor.execute(create_staff_table_query)
    conn.commit()

def create_bloodType_table(conn, cursor):
    create_blood_type_table_query = """
        CREATE TABLE IF NOT EXISTS BloodType (
            BloodTypeID INT AUTO_INCREMENT PRIMARY KEY,
            Type VARCHAR(50) NOT NULL,
            RhType VARCHAR(50) NOT NULL 
        );
        """
    cursor.execute(create_blood_type_table_query)
    conn.commit()

def create_medical_record_borrow_table(conn, cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS MedicalRecordBorrow (
         BorrowID INT AUTO_INCREMENT PRIMARY KEY,
         MedicalRecordNumber INT NOT NULL,
         BorrowDate DATETIME NOT NULL,
         BorrowedBy VARCHAR(255) NOT NULL,
         UnitID INT,
         IDCardNumber VARCHAR(18),
         BorrowReason TEXT,
         ContactPhone VARCHAR(18),
         Approver VARCHAR(255),
         Status ENUM('Pending', 'Approved', 'Rejected') NOT NULL DEFAULT 'Pending',
         FOREIGN KEY (MedicalRecordNumber) REFERENCES MedicalRecord(MedicalRecordNumber),
         FOREIGN KEY (UnitID) REFERENCES Unit(UnitID)
     );
    """
    cursor.execute(create_table_query)
    conn.commit()

def create_medical_record_return_table(conn, cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS MedicalRecordReturn (
         ReturnID INT AUTO_INCREMENT PRIMARY KEY,
         MedicalRecordNumber INT NOT NULL,
         ReturnDate DATETIME NOT NULL,
         ReturnedBy VARCHAR(255) NOT NULL,
         UnitID INT,
         IDCardNumber VARCHAR(18),
         ContactPhone VARCHAR(18),
         FOREIGN KEY (MedicalRecordNumber) REFERENCES MedicalRecord(MedicalRecordNumber),
         FOREIGN KEY (UnitID) REFERENCES Unit(UnitID)
     );
    """
    cursor.execute(create_table_query)
    conn.commit()

def create_tables():
    conn, cursor = make_connect()

    create_patients_table(conn, cursor)
    create_contact_table(conn, cursor)
    create_unit_table(conn, cursor)
    create_staff_table(conn, cursor)
    create_disease_table(conn, cursor)
    create_bloodType_table(conn, cursor)
    create_medical_record_table(conn, cursor)
    create_surgery_table(conn, cursor)
    create_ward_table(conn, cursor)
    create_recordAndWard_table(conn, cursor)
    create_cost_table(conn, cursor)
    create_medical_record_borrow_table(conn, cursor)
    create_medical_record_return_table(conn, cursor)

    break_connect(conn, cursor)

def drop_table_if_exists(conn, cursor, schema_name, table_name):
    sql = "DROP TABLE IF EXISTS `{}`.`{}`;".format(schema_name, table_name)
    cursor.execute(sql)
    conn.commit()

def drop_tables():
    conn, cursor = make_connect()

    drop_table_if_exists(conn, cursor, 'medical_record_management', 'Contact')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'Cost')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'MedicalRecordBorrow')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'MedicalRecordReturn')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'Surgery')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'MedicalRecordWards')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'MedicalRecord')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'Patient')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'Disease')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'Ward')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'Staff')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'Unit')
    drop_table_if_exists(conn, cursor, 'medical_record_management', 'BloodType')


    break_connect(conn, cursor)

def load_unit_data():
    # 打开Excel文件
    workbook = xlrd.open_workbook('D:\桌面\科室名称.xls') # xls表格路径
    sheet = workbook.sheet_by_index(0)  # 选择第一个工作表

    # 读取前两列数据
    data = []
    for row in range(1, sheet.nrows):  # 跳过标题行，从第二行开始
        row_data = [sheet.cell_value(row, col) for col in range(0, 2)]
        data.append(row_data)

    conn, cursor = make_connect()

    # 插入数据的SQL语句
    insert_query = "INSERT INTO unit (UnitID, Name) VALUES (%s, %s)"
    # 遍历数据并插入到数据库
    for row in data:
        cursor.execute(insert_query, row)
    conn.commit()

    break_connect(conn, cursor)

def load_disease_data():
    #打开excel
    workbook = xlrd.open_workbook('D:\桌面\疾病代码.xls') # xls表格路径
    sheet = workbook.sheet_by_index(0)  # 选择第一个工作表

    # 读取前两列数据
    data = []
    for row in range(1, sheet.nrows):  # 跳过标题行，从第二行开始
        row_data = [sheet.cell_value(row, col) for col in range(0, 2)]
        data.append(row_data)

    conn, cursor = make_connect()

    # 插入数据的SQL语句
    insert_query = "INSERT INTO disease (DiseaseID, Description) VALUES (%s, %s)"
    # 遍历数据并插入到数据库
    for row in data:
        cursor.execute(insert_query, row)
    conn.commit()

    break_connect(conn, cursor)

def load_bloodType_data():
    # 打开excel
    workbook = xlrd.open_workbook('D:\桌面\血型代码表.xls')  # xls表格路径
    sheet = workbook.sheet_by_index(0)  # 选择第一个工作表

    # 读取前两列数据
    data = []
    for row in range(1, sheet.nrows):  # 跳过标题行，从第二行开始
        row_data = [sheet.cell_value(row, col) for col in range(0, 3)]
        data.append(row_data)

    conn, cursor = make_connect()

    # 插入数据的SQL语句
    insert_query = "INSERT INTO bloodtype (BloodTypeID, Type, RhType) VALUES (%s, %s, %s)"
    # 遍历数据并插入到数据库
    for row in data:
        cursor.execute(insert_query, row)
    conn.commit()

    break_connect(conn, cursor)

if __name__ == '__main__':
    drop_tables() #注意这个方法，每次跑的时候都会导致表的新建
    create_tables()
    load_unit_data()
    load_disease_data()
    load_bloodType_data()
