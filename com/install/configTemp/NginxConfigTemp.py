#! /usr/bin/env python
# --coding:utf-8--
# coding: utf-8
# ━━━━━━神兽出没━━━━━━
#  　　　┏┓　　　┏┓
#  　　┏┛┻━━━┛┻┓
#  　　┃　　　　　　　┃
#  　　┃　　　━　　　┃
#  　　┃　┳┛　┗┳　┃
#  　　┃　　　　　　　┃
#  　　┃　　　┻　　　┃
#  　　┃　　　　　　　┃
#  　　┗━┓　　　┏━┛
#  　　　　┃　　　┃神兽保佑, 永无BUG!
#  　　　　┃　　　┃Code is far away from bug with the animal protecting
#  　　　　┃　　　┗━━━┓
#  　　　　┃　　　　　　　┣┓
#  　　　　┃　　　　　　　┏┛
#  　　　　┗┓┓┏━┳┓┏┛
#  　　　　　┃┫┫　┃┫┫
#  　　　　　┗┻┛　┗┻┛
#  ━━━━━━感觉萌萌哒━━━━━━
#  Module Desc:clover
#  User: z.mm | 2428922347@qq.com
#  Date: 2016/1/5
#  Time: 17:34


__author__ = 'Administrator'


class NginxConfigTemp(object):
    staticFile = '''
              location ~ .*\.(html|htm|gif|jpg|jpeg|bmp|png|ico|txt|js|css)$  {
                        root  {0};
				        expires     {1}d;
      }
    '''
    upStream = '''
             location {0} {
                proxy_pass  http://{1};
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $remote_addr;
                proxy_set_header   X-Forwarded-Proto $scheme;
                proxy_set_header   X-Real-IP        $remote_addr;
                proxy_redirect default;
      }
    '''

    upStreamItem = '''
         server {0}:{1} max_fails=3 fail_timeout=30s;
    '''

    @staticmethod
    def getStaticFileTemp(rootPath, expiresDays):
        return '''
              location ~ .*\.(html|htm|gif|jpg|jpeg|bmp|png|ico|txt|js|css)$  {
                        root  ''' + rootPath + ''';
				        expires     ''' + expiresDays + '''d;
      }
    '''

    @staticmethod
    def getUpStreamFileTemp(name, ipAndPort, balancing="ip_hash"):
        '''
            ipAndPort=[{"host":"xxx","port":"3306"}]
        '''
        servers = ""
        for item in ipAndPort:
            servers += NginxConfigTemp.upStreamItem.format(item["host"], item["port"])
        return '''upstream ''' + name + ''' {''' + balancing + ''';''' + servers + '''} '''

    @staticmethod
    def getIndexFiletemp(indexPath):
        return '''location = / {rewrite ^(.*)$   $1/''' + indexPath + ''';}'''

    '''
        server为完整的server配置，如果是多个server，也一起传入
    '''

    @staticmethod
    def getNginxConfig(wokerNum, upstream, serverConfig, logPath="logs/error.log", logLevel="info"):
        return '''
        worker_processes ''' + str(wokerNum) + ''';
        error_log  ''' + logPath + " " + logLevel + ''' ;
        events {
            worker_connections  1024;
        }
        http {
            include       mime.types;
            default_type  application/octet-stream;
              ''' + upstream + '''
            log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                              '$status $body_bytes_sent "$http_referer" '
                              '"$http_user_agent" "$http_x_forwarded_for"';
            access_log  logs/access.log  main;
            sendfile        on;
            #tcp_nopush     on;
            #keepalive_timeout  0;
            keepalive_timeout  65;
            server_tokens off;
            gzip on;
            gzip_disable "msie6";
            gzip_proxied any;
            gzip_min_length 1000;
            gzip_comp_level 4;
            gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;
            ''' + serverConfig + '''

            }
    '''

    @staticmethod
    def getServer(serverConfig):
        return '''server { ''' + serverConfig + '''} '''

    @staticmethod
    def getUpStreamLocation(match, upStreamName):
        return '''
             location ''' + match + ''' {
                proxy_pass  http://''' + upStreamName + ''';
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $remote_addr;
                proxy_set_header   X-Forwarded-Proto $scheme;
                proxy_set_header   X-Real-IP        $remote_addr;
                proxy_redirect default;
      }'''

    @staticmethod
    def getDefaultConfig(wokerNum, indexFile, upStreamName, ServerList, upStreamMatchLocation, upStreamMatchName,
                         logPath="logs/error.log", logLevel="info"):
        serverConfig = ""
        serverConfig += NginxConfigTemp.getIndexFiletemp(indexFile)
        up = NginxConfigTemp.getUpStreamFileTemp(upStreamName, ServerList)
        serverConfig += NginxConfigTemp.getUpStreamLocation(upStreamMatchLocation, upStreamMatchName)
        return NginxConfigTemp.getNginxConfig(wokerNum, up, NginxConfigTemp.getServer(serverConfig),
                                              logPath=logPath, logLevel=logLevel)
