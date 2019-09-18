import pymysql


class User:
    def __init__(self, database):
        self.db=pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='123456',
                                database=database,
                                charset='utf8'
                                )
        self.cur=self.db.cursor()

    def register(self, name, passwd):
        sql="select * from user where name=%s"
        self.cur.execute(sql, [name])
        r=self.cur.fetchone()

        # 查找到说明用户存在
        if r:
            return False

        # 插入用户名密码
        sql="insert into user (name,passwd) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except:
            print("注册失败")
            self.db.rollback()

    def login(self, name, passwd):
        sql="select * from user where name=%s and passwd=%s"
        self.cur.execute(sql, [name, passwd])
        r=self.cur.fetchone()
        if r:
            return True

if __name__ == '__main__':
    while True:
        name=input("请输入用户名：")
        pwd=input("请输入密码：")
        user=User('stu')
        if user.register(name, pwd):
            print('注册成功')
        if user.login(name, pwd):
            print('登录成功')

