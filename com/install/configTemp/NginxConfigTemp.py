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
             location / {
                proxy_pass  http://{0};
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $remote_addr;
                proxy_set_header   X-Forwarded-Proto $scheme;
                proxy_set_header   X-Real-IP        $remote_addr;
                proxy_redirect default;
      }
    '''

    index = '''
           location = / {
                    rewrite ^(.*)$ $1/{0};
       }
    '''

    upstreamServer = '''
     upstream school {
          {0};
               {1}

    }
    '''
    upStreamItem = '''
         server {0}:{1} max_fails=3 fail_timeout=30s;
    '''

    @staticmethod
    def getStaticFileTemp(rootPath, expiresDays):
        return NginxConfigTemp.staticFile.format(rootPath, expiresDays)

    '''
        ipAndPort=[{"host":"xxx","port":"3306"}]
    '''

    @staticmethod
    def getUpStreamFileTemp(ipAndPort, balancing="ip_hash"):
        servers = ""
        for item in ipAndPort:
            servers += NginxConfigTemp.upStreamItem.format(item["host"], item["port"])
        return NginxConfigTemp.upstreamServer.format(balancing, servers)

    @staticmethod
    def getIndexFiletemp(indexPath):
        return NginxConfigTemp.index.format(indexPath)


