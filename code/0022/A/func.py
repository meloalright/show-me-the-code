#a.py
from . import resize#引用成功
'''
main.py调用这一句是在A这个包初始化之后引用的
所以引用成功
'''

'''
from .. import sth#会报错
Error: attempted relative import beyond top-level package
因为函数入口main.py作为最上层不会被当做一个包
尽管文件夹中有__init__.py文件，但是该文件夹不能被python解释器视作package
'''