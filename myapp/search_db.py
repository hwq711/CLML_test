import pymysql


def search_drug_from_db(drug_name):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='123456',
                                 db='myproject', charset='utf8')
    cursor = connection.cursor()           #注意下一条代码中%s加上单引号
    sql1 = '''select * from myapp_relation where drug_x='%s' order by relation_value desc;''' % drug_name
    sql2 = '''select * from myapp_known_relation where relation_value=1 and drug_x='%s';''' % drug_name
    predict_results = []
    known_results = []
    try:
        cursor.execute(sql2)
        relations = cursor.fetchall()
        for relation in relations:
            gp_relation = float(relation[3])
            drug_name = relation[2]
            known_results.append({'drug_name': drug_name, 'gp_relation': gp_relation})

        cursor.execute(sql1)
        relations = cursor.fetchall()
        for relation in relations:
            gp_relation = float(relation[3])
            drug_name = relation[2]
            if gp_relation > 0.04:
                t = 1
                for j in range(len(known_results)):
                    known_result = known_results[j]
                    if drug_name == known_result['drug_name']:
                        t = 0
                        break
                if t == 1:
                    predict_results.append({'drug_name': drug_name, 'gp_relation': gp_relation})

    except Exception as e:
        print(str(e))
    connection.close()
    # predict_results = delete_duplicate_node(1, known_results, predict_results)
    # predict_results = normalization(predict_results)
    return known_results, predict_results
