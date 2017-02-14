##相对导入   
    
`0005任务的resize函数依然可以复用`    
`本任务用于练习相对导入知识点`    

```python
(-)0022
    (-)A
        __init__.py
        func.py
        resize.py

    (+)img

    __init__.py
    main.py
    sth.py

>>> python3 main.py
#from A import func
[main.py]从[A]中导入[func.py]
导入成功原因: [A]中含有[__init__.py]会被解释器解释为一个包

#from . import resize
[func.py]从[.当前目录]中导入[resize.py]
导入成功原因: 因为是在0022目录下执行的main.py, 上一步[A]先被解释为一个包了
            所以这一步[.当前目录]就是被成功解释的包, 可以引用[resize.py]
```