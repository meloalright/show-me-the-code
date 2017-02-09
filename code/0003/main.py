#main.py
import redis
from create_code import cr_200_code


conn = redis.Redis(host='127.0.0.1', port=6379)


'''
cr_200_code() => 200个激活码
'''
code_arr = cr_200_code()


'''
压入数据库
'''

'''
依次存入会话
'''
for i in range(len(code_arr)):
  conn.set(i, code_arr[i])
  print("id: %s ,str: %s " % (i, code_arr[i]))

'''
会话提交数据库
'''