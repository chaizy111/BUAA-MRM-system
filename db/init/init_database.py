# 数据库自动化生成文件（二次使用会格式化你的数据库！慎用）
import pymysql


def create_schema_if_not_exists(cursor, schema_name):
    cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{schema_name}';")
    if cursor.fetchone() is None:
        cursor.execute(f"CREATE SCHEMA `{schema_name}`;")


def drop_table_if_exists(cursor, schema_name, table_name):
    # 注意：这里我们需要指定数据库名，因为 DROP TABLE 需要知道在哪个数据库中删除表  
    # 假设我们已经在 'log_info' 数据库中工作  
    sql = "DROP TABLE IF EXISTS `{}`.`{}`;".format(schema_name, table_name)
    cursor.execute(sql)


def create_table(cursor, schema_name, table_name):
    cursor.execute(f"""  
    CREATE TABLE `{schema_name}`.`{table_name}` (  
        `uid` INT NOT NULL AUTO_INCREMENT,  
        `name` VARCHAR(45) NOT NULL,  
        `password` VARCHAR(45) NOT NULL, 
        `identity` ENUM('Patient', 'Doctor', 'Manager') NOT NULL DEFAULT 'Patient' ,
        PRIMARY KEY (`uid`)  
    );  
    """)


if __name__ == '__main__':
    s = input("输入你本地的数据库密码")
    # 连接到数据库
    conn = pymysql.connect(host='localhost', user='root', password=s)
    #conn = pymysql.connect(host='110.42.33.194', user='dba', password=s)
    try:
        with conn.cursor() as cursor:
            # 执行逻辑  
            create_schema_if_not_exists(cursor, 'medical_record_management')
            drop_table_if_exists(cursor, 'medical_record_management', 'login')
            create_table(cursor, 'medical_record_management', 'login')

            # 提交事务  
            conn.commit()
    finally:
        # 关闭连接  
        conn.close()  