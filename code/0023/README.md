#0023-tornado+mongo实现留言板   
   
```shell
vue部分dev方法
>>> cd my-project
>>> npm install
>>> npm run dev
```   
   
```shell
vue部分build方法
>>> cd my-project
>>> npm run build
```   
   
```shell
迁移静态文件shell
>>> ./mv.sh
```
         
```shell
开启mongo
>>> /usr/local/Cellar/mongodb/3.4.2/bin/mongod
```
      
```shell
>>> python3 main.py
```
   
   
   
   
   
###访问 / = 阻塞
```shell   
starting fetch index
end fetch index
[I 170301 11:05:31 web:1946] 304 GET / (10.0.119.120) 1.07ms
starting fetch index
end fetch index
[I 170301 11:05:31 web:1946] 200 GET / (10.0.120.100) 1.25ms
starting fetch index
end fetch index
[I 170301 11:05:32 web:1946] 200 GET / (10.0.120.100) 2.52ms
```
   
   
   
   
   
###访问 /fetch-weather/ = 非阻塞   
```shell   
starting fetch weather
starting fetch weather
starting fetch weather
end fetch weather
[I 170301 11:06:41 web:1946] 200 GET /fetch-weather/ (10.0.120.100) 498.63ms
end fetch weather
[I 170301 11:06:41 web:1946] 304 GET /fetch-weather/ (10.0.119.120) 128.04ms
end fetch weather
[I 170301 11:06:41 web:1946] 200 GET /fetch-weather/ (10.0.120.100) 255.30ms
```