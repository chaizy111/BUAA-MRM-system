import pymysql

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
    return (conn,cursor)


def break_connect(conn, cursor): # 断开数据库连接
    cursor.close()
    conn.close()
##############################################################################################

def login(username, password):
    conn, cursor = make_connect()
    query = """
            SELECT * FROM login WHERE name = %s AND password = %s
            """
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    break_connect(conn, cursor)
    if result:
        return True  # 登录成功
    else:
        return False  # 登录失败

#传入用户名，密码，是否为患者，是否为医生，姓名，证件号，科室名。
# 实现逻辑：如果是患者，直接向login表中加条目，identity为Patient；
# 如果是医生，需要先找到staff中姓名相同的所有项，检查证件号是否与这些项的一致，
# 如果一致，检查科室名对应的id是否与staff表中的科室id一致，
# 如果科室名是病案科，且符合前边的判断条件，添加条目并将identity设为Manager， 否则设为Doctor。
def sign(username, password, is_patient, is_doctor, name, id_number, department_name):
    conn, cursor = make_connect()
    # 检查用户名是否已存在
    cursor.execute("SELECT * FROM login WHERE name = %s", (username,))
    if cursor.fetchone():
        return False
    # 检查医生信息
    if is_doctor:
        cursor.execute("""
                SELECT s.*, u.Name AS UnitName
                FROM Staff s
                JOIN Unit u ON s.UnitID = u.UnitID
                WHERE s.name = %s AND s.IDCardNumber = %s AND u.Name = %s""",
                       (name, id_number, department_name))
        doctor_info = cursor.fetchone()
        if doctor_info:
            if doctor_info[3] != department_name:
                return False
            elif doctor_info[3] == '病案科':
                cursor.execute("""
                        INSERT INTO login (name, password, identity)
                        VALUES (%s, %s, 'Manager')
                        """, (username, password))
            else:
                cursor.execute("""
                                        INSERT INTO login (name, password, identity)
                                        VALUES (%s, %s, 'Doctor')
                                        """, (username, password))
        else:
            return False
    elif is_patient:
        # 插入login表，设置identity为Patient
        cursor.execute("""
                    INSERT INTO login (name, password, identity)
                    VALUES (%s, %s, 'Patient')
                """, (username, password))
    conn.commit()
    break_connect(conn, cursor)
    return True

#登录页面将用户名传至主页面，当前用户名就再主页面作为一个属性存储起来，所有的权限管理都在这个页面进行
#传入当前用户名与要执行的功能名称，根据用户的identity判断用户是否能执行该功能，返回true或false
def check_permission(username, function):
    identity = get_user_identity(username)
    user_entities = {
        'Patient': {'permissions': [
                        'medical_record_search',
                        'disease_info_search',
                        'surgery_info_search',
                        'patient_info_search',
                        '病案检索',
                        '疾病信息查询',
                        '手术信息查询',
                        '患者信息查询']},
        'Doctor': {'permissions': [
                        'medical_record_create', '新建病案',
                        'medical_record_update', '修改病案',
                        'medical_record_delete', '删除病案',
                        'medical_record_borrow', '病案借阅',
                        'medical_record_return', '病案归还',
                        'medical_record_search', '病案检索',
                        'disease_info_search',   '疾病信息查询',
                        'surgery_info_search',   '手术信息查询',
                        'patient_info_search',   '患者信息查询',
                        'medical_record_borrow', '借阅信息查询',
                        'admission_info_search', '入院信息查询',
                        'discharge_info_search', '出院信息查询']},
        'Manager': {'permissions': [
                        'medical_record_create', '新建病案',
                        'medical_record_update', '修改病案',
                        'medical_record_delete', '删除病案',
                        'medical_record_borrow', '病案借阅',
                        'medical_record_return', '病案归还',
                        'borrow_approval',       '借阅审批',
                        'medical_record_search', '病案检索',
                        'disease_info_search',   '疾病信息查询',
                        'surgery_info_search',   '手术信息查询',
                        'patient_info_search',   '患者信息查询',
                        'medical_record_borrow', '借阅信息查询',
                        'admission_info_search', '入院信息查询',
                        'discharge_info_search', '出院信息查询',
                        'discharge_info_search', '医疗费用报表',
                        'unit_visit_report',     '科室就诊情况报表',
                        'disease_classification_report', '疾病分类报表',
                        'discharge_info_report', '出院病人信息报表']}
    }
    # 根据身份获取权限列表
    user_permissions = user_entities[identity]['permissions']
    # 检查用户是否有执行该功能的权限
    return function in user_permissions

def get_user_identity(username):
    conn, cursor = make_connect()
    query = "SELECT identity FROM login WHERE name = %s"
    cursor.execute(query, (username))
    result = cursor.fetchone()  # 获取查询结果的第一行
    break_connect(conn, cursor)
    if result:
        return result[0]  # 返回用户身份
    else:
        return None  # 如果没有找到，返回None
