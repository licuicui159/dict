import pymysql

f=open('dict.txt')

# 1. 建立数据库连接(db = pymysql.connect(...))
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='dict',
                   charset='utf8'
                   )

# 2. 创建游标对象(cur = db.cursor())
cur=db.cursor()

#插入单词表
# sql="insert into words (word,mean) values (%s,%s);"
# for line in f:
#     tmp=line.split(' ',1)
#     word=tmp[0]
#     mean=tmp[1].strip()
#     cur.execute(sql,[word,mean])

# 4. 提交到数据库:db.commit()
db.commit()

sql="select * from words;"
cur.execute(sql)

# 或者获取数据:cur.fetchall()
r=cur.fetchall()
print(r)

# for i in cur:
#     print(i)

# 5. 关闭游标对象 :
cur.close()
# 6. 断开数据库连接 :
db.close()
