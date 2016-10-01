#!/usr/bin/python
#encoding=utf-8
import os
import time
import thread
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import shutil
def execute(cmd):
    os.system(cmd)
cmd = "curl node77/phpworld.php > /dev/null 1> /dev/null 2> /dev/null"
class MyHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):  # 响应GET请求
         print self.path  # 打印客户端请求GET的路径
         self.send_response(200)  # 发送200状态码，表示处理正常
         for i in range(0, 10000):
            try:
               thread.start_new_thread(execute, (cmd, ))
            except Exception, e:
               print e
httpd = HTTPServer(('', 8080), MyHttpHandler)
print("Server started port 8080.....")
httpd.serve_forever()  # 启动http服务器
