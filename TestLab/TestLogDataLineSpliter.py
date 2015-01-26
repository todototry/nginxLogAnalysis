#this script is created for ---- split data lines.
__author__ = 'fandongyun'

# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/Users/pset/.spyder2/.temp.py
"""

#测试数据：（get 方法   url  client）
testdata = '49.98.153.134 - - [25/Nov/2013:09:54:40 +0900] "GET /CarconCardServer/javascript/Common.js HTTP/1.1" 200 4321 "http://admin.api.itsjp.mtc-pas.jp/CarconCardServer/autoContribute_jp.html" "Mozilla/5.0 (Linux; U; Android 4.2.2; ja-jp; SC-04E Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30" "-" admin.api.itsjp.mtc-pas.jp carconcard-service 10.20.52.84:8080 - -\n'


#正常数据1：（post log）
normaldata1 = '10.20.52.31 - - [25/Nov/2013:10:57:58 +0900] "POST /CloudManagementAPI/UploadUserOperationLog HTTP/1.1" 200 37 "-" "-" "-" admin.api.itsjp.mtc-pas.jp cloudmgr-service 10.20.52.5:8080 - C8VB3EIAQlJzVOi6QDAmPiKqUkdC2jIL7Cb6M4mSiJut6n0gzIF5NDeSEclKNiwJoRXhgAPJ/zBI8X0vgNo0/IQN/7tBQ/4wej0Uzh8ohxIjELYlmz1/ck5M+TWJtD3Ke8YoRyUZ+fi4mVEpfANBeZF7X4HWUpCnIWnzWfqYwloU3ywb8ZV/FBDiKtUBABsh4nZKuGdVsEjvJETDi0o146Ppz2HM0JQllap60uDjrmLXB9rPKUBZWCHAoZYzrWByYMGSAEWwQhATxQq4rkcQdq6Zhsz+UPT1ih0joZ6n9JlPHoLxUpgX71a2IyILSCF3WuxQ5N3/4V7yemEG6BzFNg==\n'

#正常数据2：（ipro uuid  session）
normaldata2 = '49.96.7.136 - - [25/Nov/2013:14:36:21 +0900] "POST /CloudManagementAPI/GetSystemConfiguration HTTP/1.1" 200 3383 "-" "13IprAA/1.000003" "-" admin.api.itsjp.mtc-pas.jp cloudmgr-service 10.20.52.5:8080 D2OKnh101517 tDfS1y5EG4SGlSAQDSr+XKcbNNRkiBEReXg+0zjv0VU27WRyq9nEZvdhL7VtQYIrIKrlIloj6YLh2t1daeblnXTKpAYANuvHWNhwHlXrvLINbsR8GbBLc6oZs1XyHMOJ/qErbnRLocFH2TA997yQx4OGjybCXSsu1PrTI+vMPamQXUd/aR3NyfCwAB3sfB0iW8Htag4TALOpq+Fud7pMOF9d5a0WbLeMeZue8k3s7XJeEQdE31oLl8dK3lnMAsru/O3/PbkB6N3OVtPxEaO0ioNTY9aCUX9o62OraYXzVR78q4VTjrlqqEdyZCE6DPKq2Ns2gTOHeCACk9gc4av/Dg==\n'


#残缺数据： （缺失uuid  和 session） ？
brokendata = '117.55.68.188 - - [25/Nov/2013:05:53:13 +0900] "POST /CloudManagementAPI/GetSystemMessage HTTP/1.1" 200 68 "-" "13DdnAI/1.0.1.008 (384154624)" "-" admin.api.itsjp.mtc-pas.jp cloudmgr-service 10.20.52.4:8080 - -\n'

randomdata = '182.249.245.5 - - [25/Nov/2013:08:51:37 +0900] "POST /CloudManagementAPI/GetSystemMessage HTTP/1.1" 200 68 "-" "13DdnAI/1.0.1.008 (357990640)" "-" admin.api.itsjp.mtc-pas.jp cloudmgr-service 10.20.52.5:8080 - -\n'

#try to split all data.
splitedrandom = randomdata.rsplit('"')
splitedtest = testdata.rsplit('"')
splitednormal1 = normaldata1.rsplit('"')
splitednormal2 = normaldata2.rsplit('"')
splitedbroken = brokendata.rsplit('"')

#find out if the rsplit makes the right effect, ----works well for all kinds of data: no matter random ,normal ,
# or broken_data.
print len(splitedrandom)
print len(splitedtest)
print len(splitednormal1)
print len(splitednormal2)
print len(splitedbroken)

#print to analyze the splited data list.
import pprint
pprint.pprint(splitedrandom)
pprint.pprint(splitedtest)
pprint.pprint(splitednormal1)
pprint.pprint(splitednormal2)
pprint.pprint(splitedbroken)


#data format:
#$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent" "$http_x_forwarded_for" $server_name $proxy_host $upstream_addr $http_uuid $http_session_token

#data type list:

#1:    $remote_addr
#2:    -
#3:    $remote_user
#4:    [$time_local]
#5:   "$request"
#6:    $status
#7:    $body_bytes_sent
#8:   "$http_referer"
#9:   "$http_user_agent"
#10:  "$http_x_forwarded_for"
#11:  $server_name
#12:  $proxy_host
#13:  $upstream_addr
#14:  $http_uuid
#15:  $http_session_token

block0 = splitednormal1[0].split()
block1 = splitednormal1[1].split()
block2 = splitednormal1[2].split()
block3 = splitednormal1[3].split()
#block4 = splitednormal1[4].split()
block5 = splitednormal1[5].split('/')
#block6 = splitednormal1[6].split()
block7 = splitednormal1[7]
block8 = splitednormal1[8].split()


print block0

#block 0
remote_addr = block0[0]
remote_user = block0[2]
time_local = block0[3].replace('[', '')
time_zone = block0[4].replace(']', '')

#block 1
requestmethod = block1[0]
requesturl = block1[1]
requestprotocal = block1[2]

#block 2
status = block2[0]
body_bytes_sent = block2[1]

#block 3
http_referer = block3[0]

#block 4

#block 5
if len(block5) > 1:
    http_user_agent = block5[0]
    ver_additional = block5[1][:].split()
    http_user_agent_version = ver_additional[0]
    http_user_agent_addtionalinfo = ver_additional[1]
else:
    http_user_agent = '-'
    http_user_agent_version = '-'
    http_user_agent_addtionalinfo = '-'
#block 6

#block 7
http_x_forwarded_for = block7[0]

#block 8
server_name = block8[0]
proxy_host = block8[1]
upstream_addr = block8[2]
http_uuid = block8[3]
http_session_token = block8[4]


#show all info:
#block 0
print "addr:" + remote_addr
print "user:"+remote_user
print "time_local: " + time_local
print "time_zone: " + time_zone

#block 1
print "requestmethod :" + requestmethod
print "requestmethod :" + requesturl
print "requestmethod: " + requestprotocal

#block 2
print "status :" + status
print "body_bytes_sent: " + body_bytes_sent

#block 3
print "http_referer:" + http_referer

#block 4

#block 5
print "http_user_agent:" + http_user_agent
print "http_user_agent_version:" + http_user_agent_version
print "http_user_agent_addtionalinfo:" + http_user_agent_addtionalinfo

#block 6

#block 7
print "http_x_forwarded_for:" + http_x_forwarded_for

#block 8
print "server_name:" + server_name
print "proxy_host:" + proxy_host
print "upstream_addr:" + upstream_addr
print "http_uuid:" + http_uuid
print "http_session_token:" + http_session_token
