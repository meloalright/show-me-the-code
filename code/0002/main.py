#main.py
from sqlalchemy import *
from sqlalchemy.orm import mapper, sessionmaker,scoped_session
from create_code import cr_200_code

'''
与pgsql数据库相连接
'''
db = create_engine('postgresql://postgres:postgres@localhost:5432/', echo=True)


'''
创建对象元类
'''
metadata = MetaData(db)
codes = Table('codes', metadata,
    Column('id',Integer,primary_key=True),
    Column('str',String))


'''
手动实现一个codes类orm
'''
class Codes_Entity(object):
    __table__ = "codes"
    def __init__(self, id, str):
        self.id = id
        self.str = str
    def __repr__(self):
        return "The {0}th activation code: {1}".format(self.id, self.str)


'''
将codes类与orm相映射
'''
mapper(Codes_Entity, codes)

'''
创建数据库
'''
metadata.drop_all(db)
metadata.create_all(db)



'''
创建session
'''
sm = sessionmaker(bind=db, autocommit=False, expire_on_commit=True)
session = scoped_session(sm)

'''
cr_200_code() => 200个激活码
'''
code_arr = cr_200_code()

'''
依次存入会话
'''
for i in range(len(code_arr)):
    c = Codes_Entity(i, code_arr[i])
    session.add(c)

'''
会话提交数据库
'''
session.commit()

'''
>>> SELECT * FROM codes;

 id  |    str     
-----+------------
   0 | 9cgtygumva
   1 | fiumklj3z1
   2 | k7e5azx2nm
   3 | dooi12cmey
   4 | gwp8bgsznp
   5 | hnn85dwjq0
   6 | 8vntd15p4p
   7 | hwi08s1ita
   8 | u16dal3l9d
   9 | uxzqngzrqe
  10 | x3ixtzopq3
  11 | 7hn9bemhqp
  12 | f80um4nwea
  13 | tmmc5zewd4
  14 | yc5hcr0kh3
  ...
  ...
 199 | wwoml3cshb
(200 rows)

'''