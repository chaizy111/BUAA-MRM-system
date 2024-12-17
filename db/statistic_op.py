import pymysql
from db.search_op import *
from pymysql import Error
import pandas as pd
import xlwt, xlrd
from xlutils.copy import copy
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
    return conn, cursor


def break_connect(conn, cursor): # 断开数据库连接
    cursor.close()
    conn.close()
##############################################################################################

def get_fee_statistic_by_day():
    conn, cursor = make_connect()
    try:
        query = """
            SELECT YEAR(m.DischargeDate) AS Year, MONTH(m.DischargeDate) AS Month, DAY(m.DischargeDate) AS Day, SUM(c.Amount) AS TotalIncome
            FROM MedicalRecord m
            JOIN Cost c ON m.MedicalRecordNumber = c.MedicalRecordID
            GROUP BY YEAR(m.DischargeDate), MONTH(m.DischargeDate), DAY(m.DischargeDate)
            ORDER BY YEAR DESC, MONTH DESC, DAY DESC;
            """
        cursor.execute(query)
        results = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get_fee_statistic_by_day.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return results

def get_fee_statistic_by_month():
    conn, cursor = make_connect()
    try:
        query = """
            SELECT YEAR(m.DischargeDate) AS Year, MONTH(m.DischargeDate) AS Month, SUM(c.Amount) AS TotalIncome
            FROM MedicalRecord m
            JOIN Cost c ON m.MedicalRecordNumber = c.MedicalRecordID
            GROUP BY YEAR(m.DischargeDate), MONTH(m.DischargeDate)
            ORDER BY Year DESC, Month DESC;
            """
        cursor.execute(query)
        results = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get_fee_statistic_by_month.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return results

def get_fee_statistic_by_year():
    conn, cursor = make_connect()
    try:
        query = """
            SELECT YEAR(m.DischargeDate) AS Year, SUM(c.Amount) AS TotalIncome
            FROM MedicalRecord m
            JOIN Cost c ON m.MedicalRecordNumber = c.MedicalRecordID
            GROUP BY YEAR(m.DischargeDate)
            ORDER BY Year DESC;
            """
        cursor.execute(query)
        results = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get_fee_statistic_by_year.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return results

#返回科室名，科室id，科室就诊总人数，0-7岁患者在该科室就诊总人数，8-18岁患者在该科室就诊总人数，
# 19-30岁思者在该科室就诊总人数，30-45岁思者在该科室就诊总人数，45-60岁思者在该科室就诊总人数，
# 60-75岁患者在该科室就诊总人数，75岁以上患者在该科室就诊总人数
def get_diagnosisInUnit_statistic():
    conn, cursor = make_connect()
    try:
        query = """
            SELECT u.Name AS DepartmentName, u.UnitID, COUNT(*) AS TotalVisits,
                SUM(CASE WHEN p.Age BETWEEN 0 AND 7 THEN 1 ELSE 0 END) AS Age0_7,
                SUM(CASE WHEN p.Age BETWEEN 8 AND 18 THEN 1 ELSE 0 END) AS Age8_18,
                SUM(CASE WHEN p.Age BETWEEN 19 AND 30 THEN 1 ELSE 0 END) AS Age19_30,
                SUM(CASE WHEN p.Age BETWEEN 31 AND 45 THEN 1 ELSE 0 END) AS Age30_45,
                SUM(CASE WHEN p.Age BETWEEN 46 AND 60 THEN 1 ELSE 0 END) AS Age45_60,
                SUM(CASE WHEN p.Age BETWEEN 61 AND 75 THEN 1 ELSE 0 END) AS Age61_75,
                SUM(CASE WHEN p.Age > 75 THEN 1 ELSE 0 END) AS Age75_Plus
            FROM MedicalRecord m
            JOIN Patient p ON m.PatientIDCardNumber = p.IDCardNumber
            JOIN Unit u ON m.UnitID = u.UnitID
            GROUP BY u.UnitID
            ORDER BY u.UnitID;
            """
        cursor.execute(query)
        results = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get_diagnosisInUnit_statistic.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return results

#返回疾病名，疾病id，患该病总人数，0-7岁患该病总人数，8-18岁患该病总人数，
# 19-30岁患该病总人数，30-45岁患该病总人数，45-60岁患该病总人数，
# 60-75岁患该病总人数，75岁以上患该病总人数。
# 注意，病案中的门诊诊断，出院诊断，病理诊断如果出现相同的疾病id，则只统计一次
def get_disease_statistic():
    conn, cursor = make_connect()
    try:
        query = """
            SELECT d.Description AS DiseaseName, d.DiseaseID, COUNT(DISTINCT(m.MedicalRecordNumber)) AS TotalCases,
                SUM(CASE WHEN p.Age BETWEEN 0 AND 7 THEN 1 ELSE 0 END) AS Age0_7,
                SUM(CASE WHEN p.Age BETWEEN 8 AND 18 THEN 1 ELSE 0 END) AS Age8_18,
                SUM(CASE WHEN p.Age BETWEEN 19 AND 30 THEN 1 ELSE 0 END) AS Age19_30,
                SUM(CASE WHEN p.Age BETWEEN 31 AND 45 THEN 1 ELSE 0 END) AS Age30_45,
                SUM(CASE WHEN p.Age BETWEEN 46 AND 60 THEN 1 ELSE 0 END) AS Age45_60,
                SUM(CASE WHEN p.Age BETWEEN 61 AND 75 THEN 1 ELSE 0 END) AS Age61_75,
                SUM(CASE WHEN p.Age > 75 THEN 1 ELSE 0 END) AS Age75_Plus
            FROM Disease d
            LEFT JOIN MedicalRecord m ON d.DiseaseID IN (m.AdmissionDiagnosisID, m.DischargeDiagnosisID, m.PathologicalDiagnosisID)
            JOIN Patient p ON m.PatientIDCardNumber = p.IDCardNumber
            GROUP BY d.DiseaseID
            ORDER BY d.DiseaseID;
            """
        cursor.execute(query)
        results = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get_disease_statistic.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return results

def get_departurePatient_statistic(start_date, end_date):
    conn, cursor = make_connect()
    try:
        query = """
            SELECT 
                COUNT(*) AS TotalDischarges, AVG(DATEDIFF(m.DischargeDate, m.AdmissionDate)) AS AverageHospitalizationDays
            FROM MedicalRecord m
            WHERE m.DischargeDate BETWEEN %s AND %s
            """
        cursor.execute(query, (start_date, end_date))
        results = cursor.fetchall()
    except Error as e:
        conn.rollback()  # 回滚事务，以防部分删除操作成功
        print(f"The error '{e}' occurred when get_departurePatient_statistic.")
        break_connect(conn, cursor)
        return []
    break_connect(conn, cursor)
    return results, search_discharge_info(start_date=start_date, end_date=end_date)

def get_pdf_fee_statistic_by_year():
    data = get_fee_statistic_by_year()
    from xlwt import Workbook
    # 创建工作簿
    wb = Workbook()
    # 添加工作表
    ws = wb.add_sheet('Sheet1')
    titles = ['Year', 'TotalIncome']
    for index, title in enumerate(titles):
        ws.write(0, index, title)
    # 写入数据
    for row in range(len(data)):
        # print(row)
        for col in range(len(data[row])):
            ws.write(row + 1, col, data[row][col])
    # 保存为 .xls 格式
    wb.save('result/fee_statistic_by_year.xls')

    xlsx_handler = xlrd.open_workbook('result/fee_statistic_by_year.xls')
    workbook = copy(xlsx_handler)
    sheet = workbook.get_sheet(0)
    workbook.save('result/fee_statistic_by_year.pdf')

def get_pdf_fee_statistic_by_month():
    data = get_fee_statistic_by_month()
    from xlwt import Workbook
    # 创建工作簿
    wb = Workbook()
    # 添加工作表
    ws = wb.add_sheet('Sheet1')
    titles = ['Year','Month', 'TotalIncome']
    for index, title in enumerate(titles):
        ws.write(0, index, title)
    # 写入数据
    for row in range(len(data)):
        # print(row)
        for col in range(len(data[row])):
            ws.write(row + 1, col, data[row][col])
    # 保存为 .xls 格式
    wb.save('result/fee_statistic_by_month.xls')

    xlsx_handler = xlrd.open_workbook('result/fee_statistic_by_month.xls')
    workbook = copy(xlsx_handler)
    sheet = workbook.get_sheet(0)
    workbook.save('result/fee_statistic_by_month.pdf')

def get_pdf_fee_statistic_by_day():
    data = get_fee_statistic_by_day()
    from xlwt import Workbook
    # 创建工作簿
    wb = Workbook()
    # 添加工作表
    ws = wb.add_sheet('Sheet1')
    titles = ['Year', 'month', 'day' ,'TotalIncome']
    for index, title in enumerate(titles):
        ws.write(0, index, title)
    # 写入数据
    for row in range(len(data)):
        # print(row)
        for col in range(len(data[row])):
            ws.write(row + 1, col, data[row][col])
    # 保存为 .xls 格式
    wb.save('result/fee_statistic_by_day.xls')

    xlsx_handler = xlrd.open_workbook('result/fee_statistic_by_day.xls')
    workbook = copy(xlsx_handler)
    sheet = workbook.get_sheet(0)
    workbook.save('result/fee_statistic_by_day.pdf')

def get_pdf_disease_statistic():
    data = get_disease_statistic()
    from xlwt import Workbook
    # 创建工作簿
    wb = Workbook()
    # 添加工作表
    ws = wb.add_sheet('Sheet1')
    titles = ['疾病名', '疾病编号', '0-7岁患病人数', '8-18岁患病人数', '19-30岁患病人数', '31-45岁患病人数', '46-60岁患病人数', '61-75岁患病人数', '75岁以上患病人数']
    for index, title in enumerate(titles):
        ws.write(0, index, title)
    # 写入数据
    for row in range(len(data)):
        # print(row)
        for col in range(len(data[row])):
            ws.write(row + 1, col, data[row][col])
    # 保存为 .xls 格式
    wb.save('result/disease_statistic.xls')

    xlsx_handler = xlrd.open_workbook('result/disease_statistic.xls')
    workbook = copy(xlsx_handler)
    sheet = workbook.get_sheet(0)
    workbook.save('result/disease_statistic.pdf')

def get_pdf_diagnosisInUnit_statistic():
    data = get_diagnosisInUnit_statistic()
    from xlwt import Workbook
    # 创建工作簿
    wb = Workbook()
    # 添加工作表
    ws = wb.add_sheet('Sheet1')
    titles = ['科室', '科室号', '就诊总人数', '0-7岁就诊人数', '8-18岁就诊人数', '19-30岁就诊人数', '31-45岁就诊人数', '46-60岁就诊人数', '61-75岁就诊人数', '75岁以上就诊人数']
    for index, title in enumerate(titles):
        ws.write(0, index, title)
    # 写入数据
    for row in range(len(data)):
        # print(row)
        for col in range(len(data[row])):
            ws.write(row + 1, col, data[row][col])
    # 保存为 .xls 格式
    wb.save('result/diagnosisInUnit_statistic.xls')

    xlsx_handler = xlrd.open_workbook('result/diagnosisInUnit_statistic.xls')
    workbook = copy(xlsx_handler)
    sheet = workbook.get_sheet(0)
    workbook.save('result/diagnosisInUnit_statistic.pdf')

def get_pdf_departurePatient_statistic(start_time, end_time):
    result, data = get_departurePatient_statistic(start_time, end_time)
    from xlwt import Workbook
    # 创建工作簿
    wb = Workbook()
    # 添加工作表
    ws = wb.add_sheet('Sheet1')
    titles = ['住院总人数', '平均时间', '病历号', '患者姓名', '性别', '科室名', '支付金额', '入院时间', '出院时间', '住院时长']
    for index, title in enumerate(titles):
        ws.write(0, index, title)
    # 写入数据
    for row in range(len(data)):
        ws.write(row + 1, 0, str(result[0][0]))
        ws.write(row + 1, 1, str(result[0][1]))
        # print(row)
        for col in range(len(data[row])):
            ws.write(row + 1, col+2, data[row][col])
    # 保存为 .xls 格式
    wb.save('result/departurePatient_statistic.xls')

    xlsx_handler = xlrd.open_workbook('result/departurePatient_statistic.xls')
    workbook = copy(xlsx_handler)
    sheet = workbook.get_sheet(0)
    workbook.save('result/departurePatient_statistic.pdf')
