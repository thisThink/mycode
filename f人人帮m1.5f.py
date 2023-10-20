o0o0 ='''
cron: 50 */15 8-22 * * *
new Env('f人人帮阅读');
活动入口微信打开：http://ebb.waterkafei.cloud/user/index.html?mid=1694834307044081664
下载地址：https://www.123pan.com/s/xzeSVv-IHpfv.html
公告地址：http://175.24.153.42:8881/getmsg?type=rrb

使用方法：
1.活动入口,微信打开：http://ebb.waterkafei.cloud/user/index.html?mid=1694834307044081664
2.打开活动入口，抓包http://ebb.vinse.cn/api/user/loginByWxauth接口响应体中的 un，uid，token,
或者http://ebb.vinse.cn/api/user/info接口headers请求头中的 un，uid，token。
3.青龙环境变量菜单，添加本脚本环境变量
名称 ：rrb_config
单个账户参数： ['name|un|uid|token|key|uids']
例如：['账户1|150xxxx1234|16948xxxx664|dxxxxx|xxxxx|UID_xxxx']
多个账户['name|un|uid|token|key|uids','name|un|uid|token|key|uids']
例如：['账户1|150xxxx1234|16948xxxx664|dxxxxx|xxxxx|UID_xxxx','账户2|151xxxx1234|16948xxxx664|dxxxxx|xxxxx|UID_xxxx']
参数说明与获取：
ck:打开活动入口，抓包http://ebb.vinse.cn/api/user/loginByWxauth接口响应体中的 un，uid，token，
或者http://ebb.vinse.cn/api/user/info接口headers请求头中的 un，uid，token。
key:每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送应用后，会在推送管理后台(https://wxpusher.zjiecode.com/admin/main)的'用户管理-->用户列表'中显示
用户在推送页面点击’我的-->我的UID‘也可以获取

4.青龙环境变量菜单，添加本脚wxpusher环境变量(不需要重复添加)
青名称 ：push_config
参数 ：{"printf":0,"threadingf":1,"appToken":"xxxx"}
例如：{"printf":0,"threadingf":1,"appToken":"AT_r1vNXQdfgxxxxxscPyoORYg"}
参数说明：
printf 0是不打印调试日志，1是打印调试日志
threadingf:并行运行账号参数 1并行执行，0顺序执行，并行执行优点，能够并行跑所以账号，加快完成时间，缺点日志打印混乱。
appToken 这个是填wxpusher的appToken

5.提现标准默认是3000，与需要修改，请在本脚本最下方，按照提示修改
'''#line:37
import time #line:38
import json #line:39
import random #line:40
import requests #line:41
import re #line:42
import hashlib #line:43
import os #line:44
import threading #line:45
from urllib .parse import unquote ,quote ,urlparse ,parse_qs #line:46
checkDict ={'Mzg2Mzk3Mjk5NQ==':['欢乐的小鱼儿','gh_cf733a65ca3d'],}#line:49
def getmsg ():#line:50
    O0000OOOOO00O0000 ='v1.5f'#line:51
    OO0O00OOO0O0OO0OO =''#line:52
    try :#line:53
        OO0OOO000OO0OO0OO ='http://175.24.153.42:8881/getmsg'#line:54
        OOO00000000OOOOO0 ={'type':'rrb'}#line:55
        OO0O00OOO0O0OO0OO =requests .get (OO0OOO000OO0OO0OO ,params =OOO00000000OOOOO0 )#line:56
        OOO0OOOOOOO000000 =OO0O00OOO0O0OO0OO .json ()#line:57
        OO0O00OOOO0000O00 =OOO0OOOOOOO000000 .get ('version')#line:58
        O0000OO0O00OO00OO =OOO0OOOOOOO000000 .get ('gdict')#line:59
        O00O0O00OOO000O0O =OOO0OOOOOOO000000 .get ('gmmsg')#line:60
        print ('系统公告:',O00O0O00OOO000O0O )#line:61
        print (f'最新版本{OO0O00OOOO0000O00}当前版本{O0000OOOOO00O0000}')#line:62
        print (f'系统的公众号字典{len(O0000OO0O00OO00OO)}个:{O0000OO0O00OO00OO}')#line:63
        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:64
        print ('='*50 )#line:65
    except Exception as O0OOO0O00OO00OOO0 :#line:66
        print (OO0O00OOO0O0OO0OO .text )#line:67
        print (O0OOO0O00OO00OOO0 )#line:68
        print ('公告服务器异常')#line:69
def push (O00OO0000OOOO0000 ,OO00O0OOO0OO0OO0O ,O0O0OOOO0000OOOOO ,OOO000O00OOO00O0O ,O0O0000O0O0OO00OO ,O000O0O0O00000000 ):#line:71
    OOOOO0OO00O000O00 ='''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>TITLE</title>
<style type=text/css>
   body {
   	background-image: linear-gradient(120deg, #fdfbfb 0%, #a5d0e5 100%);
    background-size: 300%;
    animation: bgAnimation 6s linear infinite;
}
@keyframes bgAnimation {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
</style>
</head>
<body>
<p>TEXT</p><br>
<p><a href="http://175.24.153.42:8882/lookstatus?key=KEY&type=TYPE">查看状态</a></p><br>
<p><a href="http://175.24.153.42:8882/lookwxarticle?key=KEY&type=TYPE&wxurl=LINK">点击阅读检测文章</a></p><br>
</body>
</html>
    '''#line:96
    OOOO0OO000O000OO0 =OOOOO0OO00O000O00 .replace ('TITTLE',O00OO0000OOOO0000 ).replace ('LINK',OO00O0OOO0OO0OO0O ).replace ('TEXT',O0O0OOOO0000OOOOO ).replace ('TYPE',OOO000O00OOO00O0O ).replace ('KEY',O000O0O0O00000000 )#line:98
    O00O000O00O0O0O0O ={"appToken":appToken ,"content":OOOO0OO000O000OO0 ,"summary":O00OO0000OOOO0000 ,"contentType":2 ,"uids":[O0O0000O0O0OO00OO ]}#line:105
    OO0OOO0O000OOO0OO ='http://wxpusher.zjiecode.com/api/send/message'#line:106
    try :#line:107
        O0O00O000O00OOOO0 =requests .post (url =OO0OOO0O000OOO0OO ,json =O00O000O00O0O0O0O ).text #line:108
        print (O0O00O000O00OOOO0 )#line:109
        return True #line:110
    except :#line:111
        print ('推送失败！')#line:112
        return False #line:113
def getinfo (OOO00O00O0O000O0O ):#line:115
    try :#line:116
        O0O000O000000OO00 =requests .get (OOO00O00O0O000O0O )#line:117
        OO00O0O0O00000O0O =re .sub ('\s','',O0O000O000000OO00 .text )#line:119
        OO0OOOO0OOO0OOO0O =re .findall ('varbiz="(.*?)"\|\|',OO00O0O0O00000O0O )#line:120
        if OO0OOOO0OOO0OOO0O !=[]:#line:121
            OO0OOOO0OOO0OOO0O =OO0OOOO0OOO0OOO0O [0 ]#line:122
        if OO0OOOO0OOO0OOO0O ==''or OO0OOOO0OOO0OOO0O ==[]:#line:123
            if '__biz'in OOO00O00O0O000O0O :#line:124
                OO0OOOO0OOO0OOO0O =re .findall ('__biz=(.*?)&',OOO00O00O0O000O0O )#line:125
                if OO0OOOO0OOO0OOO0O !=[]:#line:126
                    OO0OOOO0OOO0OOO0O =OO0OOOO0OOO0OOO0O [0 ]#line:127
        OO000O0000O0000OO =re .findall ('varnickname=htmlDecode\("(.*?)"\);',OO00O0O0O00000O0O )#line:128
        if OO000O0000O0000OO !=[]:#line:129
            OO000O0000O0000OO =OO000O0000O0000OO [0 ]#line:130
        OO0O0OO0OOOO00O0O =re .findall ('varuser_name="(.*?)";',OO00O0O0O00000O0O )#line:131
        if OO0O0OO0OOOO00O0O !=[]:#line:132
            OO0O0OO0OOOO00O0O =OO0O0OO0OOOO00O0O [0 ]#line:133
        OO00O0OO0OO0O0O00 =re .findall ("varmsg_title='(.*?)'\.html\(",OO00O0O0O00000O0O )#line:134
        if OO00O0OO0OO0O0O00 !=[]:#line:135
            OO00O0OO0OO0O0O00 =OO00O0OO0OO0O0O00 [0 ]#line:136
        OOOO00OOO0O00OOO0 =f'公众号唯一标识：{OO0OOOO0OOO0OOO0O}|文章:{OO00O0OO0OO0O0O00}|作者:{OO000O0000O0000OO}|账号:{OO0O0OO0OOOO00O0O}'#line:137
        print (OOOO00OOO0O00OOO0 )#line:138
        return OO000O0000O0000OO ,OO0O0OO0OOOO00O0O ,OO00O0OO0OO0O0O00 ,OOOO00OOO0O00OOO0 ,OO0OOOO0OOO0OOO0O #line:139
    except Exception as O00O0OOOOO0O00OOO :#line:140
        print (O00O0OOOOO0O00OOO )#line:141
        print ('异常')#line:142
        return False #line:143
class WXYD :#line:144
    def __init__ (O0000O0O00O00OOOO ,OO00O000O00OO0OO0 ):#line:145
        print (OO00O000O00OO0OO0 )#line:146
        O0000O0O00O00OOOO .name =OO00O000O00OO0OO0 [0 ]#line:147
        O0000O0O00O00OOOO .un =OO00O000O00OO0OO0 [1 ]#line:148
        O0000O0O00O00OOOO .uid =OO00O000O00OO0OO0 [2 ]#line:149
        O0000O0O00O00OOOO .token =OO00O000O00OO0OO0 [3 ]#line:150
        O0000O0O00O00OOOO .key =OO00O000O00OO0OO0 [4 ]#line:151
        O0000O0O00O00OOOO .o000oo0o0o ='%e4%bd%a0%'#line:152
        O0000O0O00O00OOOO .tsuids =OO00O000O00OO0OO0 [5 ]#line:153
        O0000O0O00O00OOOO .headers ={'Host':'ebb.vinse.cn','un':O0000O0O00O00OOOO .un ,'mid':'1694834307044081664','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Content-Type':'application/json; charset=UTF-8','Accept':'application/json, text/javascript, */*; q=0.01','uid':O0000O0O00O00OOOO .uid ,'platform':'0','token':O0000O0O00O00OOOO .token ,'Origin':'http://ebb10.twopinkone.cloud','Referer':'http://ebb10.twopinkone.cloud/',}#line:166
    def setstatus (O0000OO00000OOOOO ):#line:168
        try :#line:169
            OOOO0O0O0O0OO0000 ='http://175.24.153.42:8882/setstatus'#line:170
            OO0O0O0OO0O0OO0OO ={'key':O0000OO00000OOOOO .key ,'type':'rrb','val':'1'}#line:171
            O0000OOOO00O000O0 =requests .get (OOOO0O0O0O0OO0000 ,params =OO0O0O0OO0O0OO0OO ,timeout =10 )#line:172
            print (O0000OO00000OOOOO .name ,O0000OOOO00O000O0 .text )#line:173
        except Exception as O00O000O00OOOOOOO :#line:174
            print ('设置状态异常')#line:175
            print (O00O000O00OOOOOOO )#line:176
    def getstatus (OO00OOO00O0O0OO0O ):#line:178
        try :#line:179
            OO00000OO00OOOO00 ='http://175.24.153.42:8882/getstatus'#line:180
            O0O0O00O0000O00OO ={'key':OO00OOO00O0O0OO0O .key ,'type':'rrb'}#line:181
            OO0OOOOO00O0O0OO0 =requests .get (OO00000OO00OOOO00 ,params =O0O0O00O0000O00OO ,timeout =3 )#line:182
            return OO0OOOOO00O0O0OO0 .text #line:183
        except Exception as OO0OO0000OO0000OO :#line:184
            print ('查询状态异常',OO0OO0000OO0000OO )#line:185
            return False #line:186
    def printjson (OO00O0O0OOO00000O ,OO0000O0OO00OO0O0 ):#line:188
        if printf ==0 :#line:189
            return #line:190
        print (OO00O0O0OOO00000O .name ,OO0000O0OO00OO0O0 )#line:191
    def userinfo (OO0OOOOO0O00000OO ):#line:193
        OO0OOOOO0O00000OO .o0o000o0o0 ='e4%bd%bf%e7%94%a8%e7%9a%84%e8%84%9a%e6%9c%ac%e4%'#line:194
        O0O000000000OOO00 =f"http://ebb.vinse.cn/api/user/info"#line:195
        OO00OO00O00O0OO00 ={"pageSize":10 }#line:196
        OO0OOOOO0O00000OO .o0userkey =hashlib .md5 (o0o0 .encode ()).hexdigest ()#line:197
        O0O0OOO0000O0OO00 =requests .post (O0O000000000OOO00 ,headers =OO0OOOOO0O00000OO .headers ,json =OO00OO00O00O0OO00 )#line:198
        OO0OOOOO0O00000OO .o0oo0000oo =OO0OOOOO0O00000OO .o000oo0o0o +OO0OOOOO0O00000OO .o0o000o0o0 #line:199
        O000OO0000OO0O00O =O0O0OOO0000O0OO00 .json ()#line:200
        if O000OO0000OO0O00O .get ('code')==0 :#line:201
            O0O00000O0OO0O000 =O000OO0000OO0O00O .get ('result').get ('nickName')#line:202
            OO0OOOOO0O00000OO .oo0oo00oo0 ='b8%8d%e6%98%af%e5%8e%9f%e7%89%88%ef'#line:203
            OO0OOOOO0O00000OO .moneyCurrent =O000OO0000OO0O00O .get ('result').get ('integralCurrent')#line:204
            print (f'{O0O00000O0OO0O000}帮豆：{OO0OOOOO0O00000OO.moneyCurrent}')#line:205
            OO0OOOOO0O00000OO .oo00o000oo ='%bc%8c%e8%af%b7%e4%bd%bf%e7%94%a8%e5%8e%9f%e7%89'#line:206
            OO0OOOOO0O00000OO .o0000o =OO0OOOOO0O00000OO .getUserKey (OO0OOOOO0O00000OO .o0userkey )#line:207
            return True #line:208
        print (OO0OOOOO0O00000OO .name ,O0O0OOO0000O0OO00 .text )#line:209
        return False #line:210
    def getUserKey (OO0O000O0O0O0O000 ,OOO0O0000O00OO0O0 ):#line:211
        OOO00O00OO0O00OO0 =[]#line:212
        OO0O000O0O0O000OO =[]#line:213
        for O00O00O000OO0000O in range (len (OOO0O0000O00OO0O0 )):#line:214
            if O00O00O000OO0000O %2 ==0 :#line:215
                OO0O000O0O0O000OO .append (OOO0O0000O00OO0O0 [O00O00O000OO0000O ])#line:216
            else :#line:217
                OOO00O00OO0O00OO0 .append (OOO0O0000O00OO0O0 [O00O00O000OO0000O ])#line:218
        O0O00OOO0OO0O0OO0 =''.join (OO0O000O0O0O000OO )+''.join (OOO00O00OO0O00OO0 )#line:219
        O0OOO0OOOO0O00OOO =hashlib .md5 (O0O00OOO0OO0O0OO0 .encode ()).hexdigest ()#line:220
        return O0OOO0OOOO0O00OOO #line:221
    def getUserSignDays (O0O00O00O0OO0O0OO ):#line:222
        O0O00O00O0OO0O0OO .oo00000oo0 =O0O00O00O0OO0O0OO .oo0oo00oo0 +O0O00O00O0OO0O0OO .oo00o000oo #line:223
        O0OOOO0OOOOOO0OOO =f"http://ebb.vinse.cn/api/user/sign"#line:224
        O00O0OOOOO00O0OO0 ={"pageSize":10 }#line:225
        O0O00O00O0OO0O0OO .oo00000oo0 +=O0O00O00O0OO0O0OO .o000o00o00 #line:226
        OOOO0OO000OOOOO0O =requests .post (O0OOOO0OOOOOO0OOO ,headers =O0O00O00O0OO0O0OO .headers ,json =O00O0OOOOO00O0OO0 )#line:227
        O0O000O0O000O00O0 =OOOO0OO000OOOOO0O .json ()#line:228
        if O0O00O00O0OO0O0OO .o0000o !='2d2c8c9e54d8ca815bfb47231fe0ea73':print (unquote (O0O00O00O0OO0O0OO .o0oo0000oo +O0O00O00O0OO0O0OO .oo00000oo0 ));return False #line:229
        if O0O000O0O000O00O0 .get ('code')==0 :#line:230
            print (f'签到成功，获得{O0O000O0O000O00O0.get("result").get("point")}帮豆')#line:231
        print (O0O00O00O0OO0O0OO .name ,OOOO0OO000OOOOO0O .text )#line:232
        print (O0O00O00O0OO0O0OO .name ,f'签到失败:{O0O000O0O000O00O0.get("msg")}')#line:233
        return True #line:234
    def getEntryUrl (OOO0O0O0O0OOO0OO0 ):#line:235
        OO00O000OO000OOO0 =OOO0O0O0O0OOO0OO0 .headers .copy ()#line:236
        OO00O000OO000OOO0 .update ({'Host':'u.cocozx.cn'})#line:237
        O0O0O000O0OO0O000 =f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={OOO0O0O0O0OOO0OO0.uid}'#line:238
        O0OO00000OO0OO0OO =requests .get (O0O0O000O0OO0O000 ,headers =OO00O000OO000OOO0 )#line:239
        print (O0OO00000OO0OO0OO .text )#line:240
    def getbd (OOO0OOO0O0O00O0O0 ):#line:241
        O0O0O0O0O00OOOOO0 ='http://ebb.vinse.cn/api/user/receiveOneDivideReward'#line:242
        O0O0000OOOOO0OO0O ='http://ebb.vinse.cn/api/user/receiveTwoDivideReward'#line:243
        OOOOOOO0OO00OOOO0 ={"pageSize":10 }#line:244
        O00O00OOOO00O000O =requests .post (O0O0O0O0O00OOOOO0 ,headers =OOO0OOO0O0O00O0O0 .headers ,json =OOOOOOO0OO00OOOO0 )#line:245
        O0OO00O0O0O00OOOO =O00O00OOOO00O000O .json ()#line:246
        print ('领取一级帮豆',O0OO00O0O0O00OOOO .get ('msg'))#line:247
        time .sleep (1 )#line:248
        O00O00OOOO00O000O =requests .post (O0O0000OOOOO0OO0O ,headers =OOO0OOO0O0O00O0O0 .headers ,json =OOOOOOO0OO00OOOO0 )#line:249
        O0OO00O0O0O00OOOO =O00O00OOOO00O000O .json ()#line:250
        print ('领取二级帮豆',O0OO00O0O0O00OOOO .get ('msg'))#line:251
    def read (OOOOOO0OOO0O0O000 ):#line:252
        OO0O000OOO000000O =OOOOOO0OOO0O0O000 .headers .copy ()#line:253
        OO0O000OOO000000O .update ({'Host':'u.cocozx.cn'})#line:254
        while True :#line:255
            print ('-'*50 )#line:256
            OOO0O0000OOO00O00 =f'http://u.cocozx.cn/ipa/read/read'#line:257
            O0O0O0O0O00OO0O00 ={"fr":"ebb0726","uid":OOOOOO0OOO0O0O000 .uid ,"un":None ,"token":None ,"pageSize":20 }#line:258
            O00OOO0OOO0O0O000 =requests .post (OOO0O0000OOO00O00 ,headers =OO0O000OOO000000O ,json =O0O0O0O0O00OO0O00 )#line:259
            OOOOOO0OOO0O0O000 .printjson (O00OOO0OOO0O0O000 .text )#line:260
            O0O0OOOO000O0OO00 =O00OOO0OOO0O0O000 .json ()#line:261
            if O0O0OOOO000O0OO00 .get ('code')==0 :#line:262
                OOOO000OOO00O0OOO =O0O0OOOO000O0OO00 .get ('result').get ('status')#line:263
                if OOOO000OOO00O0OOO ==10 :#line:264
                    O0O000OO00OO000O0 =O0O0OOOO000O0OO00 .get ('result').get ('url')#line:265
                    OOOOOO0OOO0O0O000 .uuk =OOOOOO0OOO0O0O000 .getUserKey (O0O000OO00OO000O0 )#line:266
                    OO00000OO0OOOO000 =getinfo (O0O000OO00OO000O0 )#line:267
                    if OOOOOO0OOO0O0O000 .testCheck (OO00000OO0OOOO000 ,O0O000OO00OO000O0 )==False :#line:268
                        return False #line:269
                    print ('获取文章成功，准备阅读')#line:270
                    O00OOO0O00OO00000 =random .randint (7 ,10 )#line:271
                    print (f'本次模拟读{O00OOO0O00OO00000}秒')#line:272
                    time .sleep (O00OOO0O00OO00000 )#line:273
                    OOOOOO0OOO000O0O0 =OOOOOO0OOO0O0O000 .submit ()#line:274
                    if OOOOOO0OOO000O0O0 ==True :return True #line:275
                    if OOOOOO0OOO000O0O0 ==False :return False #line:276
                elif OOOO000OOO00O0OOO ==30 :#line:277
                    print ('未知情况')#line:278
                    time .sleep (2 )#line:279
                    continue #line:280
                elif OOOO000OOO00O0OOO ==50 or OOOO000OOO00O0OOO ==80 :#line:281
                    print ('您的阅读暂时失效，请明天再来')#line:282
                    return False #line:283
                else :#line:284
                    print ('本次推荐文章已全部读完')#line:285
                    return True #line:286
            else :#line:287
                print ('read err')#line:288
                return False #line:289
    def testCheck (O000O0OO0000O0000 ,O000OOO00O0O0OOO0 ,OO0O00OO00O0O0000 ):#line:290
        if O000OOO00O0O0OOO0 ==False :#line:291
            print (O000O0OO0000O0000 .name ,'解析文章链接失败')#line:292
            return True #line:293
        if O000OOO00O0O0OOO0 [4 ]==[]:#line:294
            print (O000O0OO0000O0000 .name ,'这个链接没有获取到微信号id',OO0O00OO00O0O0000 )#line:295
            return True #line:296
        if checkDict .get (O000OOO00O0O0OOO0 [4 ])!=None :#line:297
            O000O0OO0000O0000 .setstatus ()#line:298
            for O0OOO0OO00O0OOOOO in range (60 ):#line:299
                if O0OOO0OO00O0OOOOO %30 ==0 :#line:300
                    push ('人人帮过检测',OO0O00OO00O0O0000 ,O000OOO00O0O0OOO0 [3 ],'rrb',O000O0OO0000O0000 .tsuids ,O000O0OO0000O0000 .key )#line:301
                OO0OO0OOOOO00O000 =O000O0OO0000O0000 .getstatus ()#line:302
                if OO0OO0OOOOO00O000 =='0':#line:303
                    print ('过检测文章已经阅读')#line:304
                    return True #line:305
                elif OO0OO0OOOOO00O000 =='1':#line:306
                    print (f'正在等待过检测文章阅读结果{O0OOO0OO00O0OOOOO}秒。。。')#line:307
                    time .sleep (1 )#line:308
                else :#line:309
                    print ('服务器异常')#line:310
                    return False #line:311
            print ('过检测超时中止脚本防止黑号')#line:312
            return False #line:313
        else :return True #line:314
    def submit (OOO0O0O0O0O00000O ):#line:315
        O0OOO000O0OOO00OO =OOO0O0O0O0O00000O .headers .copy ()#line:316
        O0OOO000O0OOO00OO .update ({'Host':'u.cocozx.cn'})#line:317
        O00OOOOOO00O00O0O =f'http://u.cocozx.cn/ipa/read/submit'#line:318
        O0000OO0OOO000O00 ={"fr":"ebb0726","uid":OOO0O0O0O0O00000O .uid ,"un":None ,"token":None ,"pageSize":20 }#line:319
        OO00OOO000OOOOOOO =requests .post (O00OOOOOO00O00O0O ,headers =O0OOO000O0OOO00OO ,json =O0000OO0OOO000O00 )#line:320
        OOO0O0O0O0O00000O .printjson (OO00OOO000OOOOOOO .text )#line:321
        OOO0O000OO0O00O00 =OO00OOO000OOOOOOO .json ()#line:322
        if OOO0O000OO0O00O00 .get ('code')==0 :#line:323
            OO0OOO00OO0OO0000 =OOO0O000OO0O00O00 .get ('result')#line:324
            print (f'获得200帮豆')#line:325
            O00000000OOOOOO00 =OO0OOO00OO0OO0000 .get ('progress')#line:326
            if O00000000OOOOOO00 >0 :#line:327
                print (f'本轮剩余{O00000000OOOOOO00}篇文章，继续阅读阅读')#line:328
            else :#line:329
                print ('阅读已完成')#line:330
                print ('-'*50 )#line:331
                return True #line:332
        else :#line:333
            print (OOO0O0O0O0O00000O .name ,OO00OOO000OOOOOOO .text )#line:334
            print ('异常,尝试继续阅读')#line:335
    def withdraw (OOO0OO00OOOO0O0OO ):#line:338
        if OOO0OO00OOOO0O0OO .moneyCurrent <txbz :#line:339
            print (OOO0OO00OOOO0O0OO .name ,'没有达到提现标准')#line:340
            return False #line:341
        elif 3000 <=OOO0OO00OOOO0O0OO .moneyCurrent <10000 :#line:342
            O0O00OO0O0O00O00O =3000 #line:343
        elif 10000 <=OOO0OO00OOOO0O0OO .moneyCurrent <50000 :#line:344
            O0O00OO0O0O00O00O =10000 #line:345
        elif 50000 <=OOO0OO00OOOO0O0OO .moneyCurrent <100000 :#line:346
            O0O00OO0O0O00O00O =50000 #line:347
        else :#line:348
            O0O00OO0O0O00O00O =100000 #line:349
        O0OO0O0OO0O00OO0O =f"http://ebb.vinse.cn/apiuser/aliWd"#line:350
        O0O0O0O0OO00O0O00 ={"val":O0O00OO0O0O00O00O ,"pageSize":10 }#line:351
        OOOO0000OO000OOOO =requests .post (O0OO0O0OO0O00OO0O ,headers =OOO0OO00OOOO0O0OO .headers ,json =O0O0O0O0OO00O0O00 )#line:352
        print (OOO0OO00OOOO0O0OO .name ,OOOO0000OO000OOOO .text )#line:353
    def run (OO000O0OOOO000OO0 ):#line:355
        OO000O0OOOO000OO0 .o000o00o00 ='%88%ef%bc%81'#line:356
        if OO000O0OOOO000OO0 .userinfo ()and OO000O0OOOO000OO0 .getUserSignDays ():#line:357
            time .sleep (2 )#line:358
            OO000O0OOOO000OO0 .getEntryUrl ()#line:359
            OO000O0OOOO000OO0 .read ()#line:360
            time .sleep (2 )#line:361
            OO000O0OOOO000OO0 .getbd ()#line:362
            time .sleep (2 )#line:363
            OO000O0OOOO000OO0 .userinfo ()#line:364
            time .sleep (2 )#line:365
            OO000O0OOOO000OO0 .withdraw ()#line:366
if __name__ =='__main__':#line:369
    pushconfig =os .getenv ('push_config')#line:370
    if pushconfig ==None :#line:371
        print ('请检查你的推送变量名称是否填写')#line:372
        exit (0 )#line:373
    try :#line:374
        pushconfig =json .loads (pushconfig .replace ("'",'"'))#line:375
    except Exception as e :#line:376
        print (e )#line:377
        print (pushconfig )#line:378
        print ('请检查你的推送变量参数是否填写正确')#line:379
        exit (0 )#line:380
    rrbconfig =os .getenv ('rrb_config')#line:381
    if rrbconfig ==None :#line:382
        print ('请检查你的人人帮脚本变量名称是否填写')#line:383
        exit (0 )#line:384
    try :#line:385
        rrbconfig =json .loads (rrbconfig .replace ("'",'"'))#line:386
    except Exception as e :#line:387
        print (e )#line:388
        print (rrbconfig )#line:389
        print ('请检查你的人人帮脚本变量参数是否填写正确')#line:390
        exit (0 )#line:391
    printf =pushconfig ['printf']#line:392
    appToken =pushconfig ['appToken']#line:393
    threadingf =pushconfig ['threadingf']#line:394
    getmsg ()#line:395
    txbz =3000 #line:396
    tl =[]#line:397
    if threadingf ==1 :#line:398
        for i in rrbconfig :#line:399
            cg =i .split ('|')#line:400
            print ('*'*50 )#line:401
            print (f'开始执行{i[0]}')#line:402
            api =WXYD (cg )#line:403
            t =threading .Thread (target =api .run ,args =())#line:404
            tl .append (t )#line:405
            t .start ()#line:406
            time .sleep (0.5 )#line:407
        for t in tl :#line:408
            t .join ()#line:409
    elif threadingf ==0 :#line:410
        for i in rrbconfig :#line:411
            cg =i .split ('|')#line:412
            print ('*'*50 )#line:413
            print (f'开始执行{cg[0]}')#line:414
            api =WXYD (cg )#line:415
            api .run ()#line:416
            print (f'{cg[0]}执行完毕')#line:417
            time .sleep (3 )#line:418
    else :#line:419
        print ('请确定推送变量中threadingf参数是否正确')#line:420
    print ('全部账号执行完成')#line:421
