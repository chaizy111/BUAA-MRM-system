import pymysql

#################################### 数据库操作 ##############################################
def make_connect():     # 建立数据库连接
    conn = pymysql.connect(
        host='localhost',		# 主机名（或IP地址）
        port=3306,				# 端口号，默认为3306
        user='root',			# 用户名
        password='2003',	    # 你本地的数据库密码,请自行更改
        charset='utf8mb4'  		# 设置字符编码
    )
    conn.select_db("medical_record_management") # 选择数据库
    cursor = conn.cursor() # 创建游标对象
    # 获取mysql服务信息（测试连接，输出MySQL版本号）
    # print(conn.get_server_info())
    return conn, cursor


def break_connect(conn, cursor): # 断开数据库连接
    cursor.close()
    conn.close()
##############################################################################################

def get_fee_statistic():
    conn, cursor = make_connect()
    break_connect(conn, cursor)

def get_diagnosisInUnit_statistic():
    conn, cursor = make_connect()
    break_connect(conn, cursor)

def get_disease_statistic():
    conn, cursor = make_connect()
    break_connect(conn, cursor)

def get_departurePatient_statistic():
    conn, cucrsor = make_connect()
    break_connect(conn, cucrsor)