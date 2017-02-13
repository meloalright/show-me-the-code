##调用百度语音识别接口

`执行main.py程序`   
`此时说话:"谷歌地图API"`   
`调用百度语音识别接口成功后 => 浏览器会自动打开https://google.com.hk`

```python
#百度开发者平台-[python-oauth]

ID: 9271468

API Key: jhxXtlvzv2A9FVPk4Zion0hT

Secret Key: UivRhZbUBPGuiR1nVsHalMQMMM10S10K


#语音-[python-oauth]

App ID: 9271468

API Key: jhxXtlvzv2A9FVPk4Zion0hT

Secret Key: UivRhZbUBPGuiR1nVsHalMQMMM10S10K

```


```shell
>>> python3 main.py
* recording
* done recording
request api ing...

{'sn': '197061159531486965239', 'corpus_no': '6386467072560171530', 'result': ['谷歌地图ａｐｉ，'], 'err_no': 0, 'err_msg': 'success.'}
```
   

[百度语音开放平台](http://yuyin.baidu.com/)