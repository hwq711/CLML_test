import xlrd
import pymysql


# 存drug数据
def drug_to_db(drug, connection):
    cursor = connection.cursor()
    try:
        cursor.executemany('INSERT INTO `myapp_drug` (`drug_name`) VALUES (%s)', drug)
        connection.commit()
    except Exception as e:
        print(e)
        connection.rollback()
    print('drug insert complete!')


# 存预测的关联数据
def relation_to_db(relation, connection):
    cursor = connection.cursor()
    try:
        cursor.executemany('INSERT INTO `myapp_relation` (`drug_x`, `drug_y`, `relation_value`) VALUES (%s, %s, %s)', relation)
        connection.commit()
    except Exception as e:
        print(e)
        connection.rollback()
    print('relation insert complete!')


# 存已有的关联数据
def known_relation_to_db(known_relation, connection):
    cursor = connection.cursor()
    try:
        cursor.executemany('INSERT INTO `myapp_known_relation` (`drug_x`, `drug_y`, `relation_value`) VALUES (%s, %s, %s)', known_relation)
        connection.commit()
    except Exception as e:
        print(e)
        connection.rollback()
    print('known_relation insert complete!')

def data_to_db():
    drug = []
    x1 =xlrd.open_workbook(r'CLMl/drugID.xlsx')
    table = x1.sheets()[0]
    rownum = table.nrows
    for i in range(rownum):
        row = table.row_values(i)
        row1 = "".join(row)
        drug.append(row1)

    relation = []
    x2 = xlrd.open_workbook(r'CLMl/predictData.xlsx')
    table2 = x2.sheets()[0]
    rowNum = table2.nrows
    colNum = table2.ncols
    for i in range(rowNum):
        for j in range(colNum):
            r = table2.cell_value(i, j)
            temp = (drug[i], drug[j], r)
            relation.append(temp)

    known_relation = []
    x3 = xlrd.open_workbook(r'CLMl/D.xlsx')
    table3 = x3.sheets()[0]
    rowNumm = table3.nrows
    colNumm = table3.ncols
    for i in range(rowNumm):
        for j in range(colNumm):
            r1 = table3.cell_value(i, j)
            temp1 = (drug[i], drug[j], r1)
            known_relation.append(temp1)

    # 打开数据库连接
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='123456',
                                 db='myproject',
                                 charset='utf8')

    drug_to_db(drug, connection)
    relation_to_db(relation, connection)
    known_relation_to_db(known_relation,connection)
    connection.close()