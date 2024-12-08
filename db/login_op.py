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
def sign():
    conn, cursor = make_connect()
    break_connect(conn, cursor)
