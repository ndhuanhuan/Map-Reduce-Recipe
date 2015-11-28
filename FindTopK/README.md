##从log中找到访问次数最多前K个url
日志格式如下
```
10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202
10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209
```
##测试
cat ../sample_data_access_log | python mapper.py | sort | python reducer.py 
##输出
```
/	223.0
/assets/img/closelabel.gif	244.0
/assets/img/home-logo.png	249.0
/assets/img/loading.gif	249.0
/assets/js/lowpro.js	249.0
/assets/css/reset.css	253.0
/assets/css/960.css	252.0
/assets/js/lightbox.js	253.0
/assets/css/the-associates.css	256.0
/assets/js/the-associates.js	253.0
```
##最小堆
在reducer里维护了一个长度为k个最小堆
