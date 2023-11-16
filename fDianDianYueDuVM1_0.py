oo0o ='''
cron: 30 */30 8-22 * * *
new Env('f点点阅读');
活动入口：http://zs.87953708037.api.87953708037.87953708037.shuxiangby8.top/index/mob/index.html?pid=4318
使用方法：
1.入口,WX打开：http://zs.87953708037.api.87953708037.87953708037.shuxiangby8.top/index/mob/index.html?pid=4318
'''#line:7
'''
2.打开活动入口，抓包的任意接口cookie参数
3.青龙环境变量菜单或者配置文件，添加本脚本环境变量
填写变量参数时为方便填写可以随意换行
青龙添加环境变量名称 ：ddydconfig
方式一：青龙添加环境变量参数 ：
单账户：[{'name':'备注名','cookie': 'PHPSESSID=xxxx','key':'xxxxxxx','uids':'xxxxxxx'}]
多账户：[{'name':'备注名','cookie': 'PHPSESSID=xxxx','key':'xxxxxxx','uids':'xxxxxxx'},{'name':'备注名','cookie': 'PHPSESSID=xxxx','key':'xxxxxxx','uids':'xxxxxxx'}]

方式二：配置文件添加
单账户：export ddydconfig="[{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'}]"
多账户：export ddydconfig="[
{'name':'备注名','cookie': 'PHPSESSID=xxxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx','key':'xxxxxxx','uids':'xxxxxxx'}
]"
参数说明：
name:备注名随意填写
cookie:打开活动入口，抓包的任意接口headers中的cookie参数
key：每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey(全部脚本key通用，一个微信号一个key)
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送应用后，会在推送管理后台(https://wxpusher.zjiecode.com/admin/main)的'用户管理-->用户列表'中显示
用户在推送页面点击’我的-->我的UID‘也可以获取

4.青龙环境变量菜单，添加本脚wxpusher环境变量(不需要重复添加)
方式一：青龙添加环境变量参数 ：
名称 ：push_config
参数 ：{"printf":0,"threadingf":1,"appToken":"xxxx"}
方式二：配置文件添加
export push_config="{'printf':'0','threadingf':'1','appToken':'xxxx'}"
参数说明：
printf:0是不打印调试日志，1是打印调试日志
threadingf:并行运行账号参数 1并行执行，0顺序执行，并行执行优点，能够并行跑所以账号，加快完成时间，缺点日志打印混乱。
appToken 这个是填wxpusher的appToken,找不到自己百度

5.本地电脑python运行
在本脚本最下方代码if __name__ == '__main__':下填写
例如
loc_push_config={"printf":0,"threadingf":1,"appToken":"xxxx"}
loc_klydconfig=[
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'}
]
定时运行每半个小时一次
'''#line:55
import requests #line:56
import re #line:57
import random #line:58
import os #line:59
import threading #line:60
import json #line:61
import time #line:62
from urllib .parse import urlparse ,parse_qs #line:63
checkDict ={'oneischeck':['第一篇文章','过检测'],}#line:66
def getmsg ():#line:67
    OO0OO0OOOO0O00O00 ='v1.0f'#line:68
    OOOO0OOOOO000OO00 =''#line:69
    try :#line:70
        OOO0O00O00O0O0OOO ='http://175.24.153.42:8881/getmsg'#line:71
        OOO00OO00O000O0O0 ={'type':'ybxkhh'}#line:72
        OOOO0OOOOO000OO00 =requests .get (OOO0O00O00O0O0OOO ,params =OOO00OO00O000O0O0 )#line:73
        OOO0O0OOO00O0000O =OOOO0OOOOO000OO00 .json ()#line:74
        OO00O0OO00OO0O0OO =OOO0O0OOO00O0000O .get ('version')#line:75
        O000OOOO0O000OOO0 =OOO0O0OOO00O0000O .get ('gdict')#line:76
        O0O0O00O00O00O0O0 =OOO0O0OOO00O0000O .get ('gmmsg')#line:77
        print ('系统公告:',O0O0O00O00O00O0O0 )#line:78
        print (f'最新版本{OO00O0OO00OO0O0OO},当前版本{OO0OO0OOOO0O00O00}')#line:79
        print (f'系统的公众号字典{len(O000OOOO0O000OOO0)}个:{O000OOOO0O000OOO0}')#line:80
        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:81
        print ('='*50 )#line:82
    except Exception as O00OOO0OO0OOOOOO0 :#line:83
        print (OOOO0OOOOO000OO00 .text )#line:84
        print (O00OOO0OO0OOOOOO0 )#line:85
        print ('公告服务器异常')#line:86
def push (O00O000O00000O0O0 ,OOO000000O0OO0OO0 ,OOOO0OOOOOOO00OO0 ,OOOO0OOOOOOOO0O00 ,O0OOOOO00O0OO0OO0 ,OOO0O000O0O000O00 ):#line:87
    O000O0OOO0OO000OO ='''<!DOCTYPE html>
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
    '''#line:112
    O000O0OOOOOO0O00O =O000O0OOO0OO000OO .replace ('TITTLE',O00O000O00000O0O0 ).replace ('LINK',OOO000000O0OO0OO0 ).replace ('TEXT',OOOO0OOOOOOO00OO0 ).replace ('TYPE',OOOO0OOOOOOOO0O00 ).replace ('KEY',OOO0O000O0O000O00 )#line:114
    OOOOOO00OOOOOOOOO ={"appToken":appToken ,"content":O000O0OOOOOO0O00O ,"summary":O00O000O00000O0O0 ,"contentType":2 ,"uids":[O0OOOOO00O0OO0OO0 ]}#line:121
    O0OO0OOOO000O0O0O ='http://wxpusher.zjiecode.com/api/send/message'#line:122
    try :#line:123
        O0OOOO0O00OOOOO00 =requests .post (url =O0OO0OOOO000O0O0O ,json =OOOOOO00OOOOOOOOO ).text #line:124
        print (O0OOOO0O00OOOOO00 )#line:125
        return True #line:126
    except :#line:127
        print ('推送失败！')#line:128
        return False #line:129
def getinfo (OO0O0O0OOOOOO0OO0 ):#line:130
    try :#line:131
        OOO0OO0OOO000OOOO =requests .get (OO0O0O0OOOOOO0OO0 )#line:132
        OOOO00O000O0O0O0O =re .sub ('\s','',OOO0OO0OOO000OOOO .text )#line:134
        O0O0000O0OOOOO000 =re .findall ('varbiz="(.*?)"\|\|',OOOO00O000O0O0O0O )#line:135
        if O0O0000O0OOOOO000 !=[]:#line:136
            O0O0000O0OOOOO000 =O0O0000O0OOOOO000 [0 ]#line:137
        if O0O0000O0OOOOO000 ==''or O0O0000O0OOOOO000 ==[]:#line:138
            if '__biz'in OO0O0O0OOOOOO0OO0 :#line:139
                O0O0000O0OOOOO000 =re .findall ('__biz=(.*?)&',OO0O0O0OOOOOO0OO0 )#line:140
                if O0O0000O0OOOOO000 !=[]:#line:141
                    O0O0000O0OOOOO000 =O0O0000O0OOOOO000 [0 ]#line:142
        OO00OO000O0O00000 =re .findall ('varnickname=htmlDecode\("(.*?)"\);',OOOO00O000O0O0O0O )#line:143
        if OO00OO000O0O00000 !=[]:#line:144
            OO00OO000O0O00000 =OO00OO000O0O00000 [0 ]#line:145
        OO0000O0OO0O0OOOO =re .findall ('varuser_name="(.*?)";',OOOO00O000O0O0O0O )#line:146
        if OO0000O0OO0O0OOOO !=[]:#line:147
            OO0000O0OO0O0OOOO =OO0000O0OO0O0OOOO [0 ]#line:148
        OO000O0O0O0000O00 =re .findall ("varmsg_title='(.*?)'\.html\(",OOOO00O000O0O0O0O )#line:149
        if OO000O0O0O0000O00 !=[]:#line:150
            OO000O0O0O0000O00 =OO000O0O0O0000O00 [0 ]#line:151
        OOO0O0000O0OOO00O =f'公众号唯一标识：{O0O0000O0OOOOO000}|文章:{OO000O0O0O0000O00}|作者:{OO00OO000O0O00000}|账号:{OO0000O0OO0O0OOOO}'#line:152
        print (OOO0O0000O0OOO00O )#line:153
        return OO00OO000O0O00000 ,OO0000O0OO0O0OOOO ,OO000O0O0O0000O00 ,OOO0O0000O0OOO00O ,O0O0000O0OOOOO000 #line:154
    except Exception as O0OOOOOO00O000O00 :#line:155
        print (O0OOOOOO00O000O00 )#line:156
        print ('异常')#line:157
        return False #line:158
class WXYD :#line:159
    def __init__ (OOOO000O0OO0O00O0 ,O00O0O0OOO0OOO00O ):#line:160
        OOOO000O0OO0O00O0 .name =O00O0O0OOO0OOO00O ['name']#line:161
        OOOO000O0OO0O00O0 .key =O00O0O0OOO0OOO00O ['key']#line:162
        OOOO000O0OO0O00O0 .uids =O00O0O0OOO0OOO00O ['uids']#line:163
        OOOO000O0OO0O00O0 .headers ={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6','Cache-Control':'max-age=0','Cookie':'PHPSESSID=fbb90c8cd1eb3002d025759f68b2bba1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',}#line:172
    def printjson (O0OOOO0OOO000000O ,OOOO00O000OO00OO0 ):#line:173
        if printf ==0 :#line:174
            return #line:175
        print (O0OOOO0OOO000000O .name ,OOOO00O000OO00OO0 )#line:176
    def setstatus (OOOOOO00O00OO0O00 ):#line:177
        try :#line:178
            OO0OOO0O000OO000O ='http://175.24.153.42:8882/setstatus'#line:179
            O00O0OOOO0OO00O0O ={'key':OOOOOO00O00OO0O00 .key ,'type':'ybxkhh','val':'1','ven':oo0o }#line:180
            OOO0OO0O00OOOOOOO =requests .get (OO0OOO0O000OO000O ,params =O00O0OOOO0OO00O0O ,timeout =10 )#line:181
            print (OOOOOO00O00OO0O00 .name ,OOO0OO0O00OOOOOOO .text )#line:182
            if '无效'in OOO0OO0O00OOOOOOO .text :#line:183
                exit (0 )#line:184
        except Exception as OO0O00O0O0O000OOO :#line:185
            print (OOOOOO00O00OO0O00 .name ,'设置状态异常')#line:186
            print (OOOOOO00O00OO0O00 .name ,OO0O00O0O0O000OOO )#line:187
    def getstatus (O000OO0O0OOOO0000 ):#line:189
        try :#line:190
            O0O0O0O0O0O0OO0OO ='http://175.24.153.42:8882/getstatus'#line:191
            OO0OO0OO0O0O0O0O0 ={'key':O000OO0O0OOOO0000 .key ,'type':'ybxkhh'}#line:192
            OOOO0000O0O00O0O0 =requests .get (O0O0O0O0O0O0OO0OO ,params =OO0OO0OO0O0O0O0O0 ,timeout =3 )#line:193
            return OOOO0000O0O00O0O0 .text #line:194
        except Exception as O00O000O0O0O00O0O :#line:195
            print (O000OO0O0OOOO0000 .name ,'查询状态异常',O00O000O0O0O00O0O )#line:196
            return False #line:197
    def tuijian (O000O0O00O0000OO0 ):#line:198
        O0OO000O0OOOO00O0 ='http://ab1115131510.c1315101115.ww1112001.cn/tuijian'#line:199
        O000OOO00OOO0OO0O =requests .get (O0OO000O0OOOO00O0 ,headers =O000O0O00O0000OO0 .headers )#line:200
        try :#line:201
            O0O00OO00OO0O0O00 =O000OOO00OOO0OO0O .json ()#line:202
            if O0O00OO00OO0O0O00 .get ('code')==0 :#line:203
                O00O0OOOO0O0O0OO0 =O0O00OO00OO0O0O00 ['data']['user']['username']#line:204
                O0OO00OO000OO0O0O =float (O0O00OO00OO0O0O00 ['data']['user']['score'])/100 #line:205
                print (f'{O00O0OOOO0O0O0OO0}:当前剩余{O0OO00OO000OO0O0O}元')#line:206
            else :#line:207
                print (O0O00OO00OO0O0O00 )#line:208
                print ('账号异常0')#line:209
                exit (0 )#line:210
        except Exception as OO00O0O000O000OOO :#line:211
            print (OO00O0O000O000OOO )#line:212
            print ('账号异常1')#line:213
            exit (0 )#line:214
    def index (OO0OO00OO00000OO0 ):#line:215
        OOO0O00O00OO0OOO0 ='http://17428000109.read.shuxiangby.cn/index/mob/index.html'#line:216
        O00OOO0O0OO0O000O =requests .get (OOO0O00O00OO0OOO0 ,headers =OO0OO00OO00000OO0 .headers )#line:217
        OO000OO0O0O00O0O0 =re .sub ('\s','',O00OOO0O0OO0O000O .text )#line:218
        try :#line:219
            O0OO00O0000OO000O =re .findall ('<divclass="fen"><divclass="jifen">可用积分：(.*?)<text>>',OO000OO0O0O00O0O0 )[0 ]#line:220
            OOO000OO0O00O0O00 =re .findall ('<divclass="nickname">(.*?)</div>',OO000OO0O0O00O0O0 )[0 ]#line:221
            OO0OO00OO00000OO0 .userid =re .findall ('<divclass="userid">用户ID：(.*?)</div>',OO000OO0O0O00O0O0 )[0 ]#line:222
            print (f'{OOO000OO0O00O0O00}剩余积分：{O0OO00O0000OO000O}分')#line:223
            return True #line:224
        except :#line:225
            print (OO000OO0O0O00O0O0 )#line:226
            print ('获取用户积分失败，请查看更新ck或者查看正好是否正常')#line:227
            return False #line:228
    def get_read_code (OOO0OOOO0O0OO0O0O ):#line:229
        OOO0O00OOOOO000OO =f'http://17428000109.read.shuxiangby.cn/index/mob/get_read_qr.html'#line:230
        O0000000O000OOOOO =requests .get (OOO0O00OOOOO000OO ,headers =OOO0OOOO0O0OO0O0O .headers )#line:231
        O00O0O00O00OO0OO0 =O0000000O000OOOOO .json ()#line:232
        if O00O0O00O00OO0OO0 .get ('code')==1 :#line:233
            OO0OO0OO0O00OO0O0 =O00O0O00O00OO0OO0 ['data']#line:234
            OO0OOOOO000OO000O =re .findall ('qr/(.*?)\.png',OO0OO0OO0O00OO0O0 )[0 ]#line:235
            return OO0OOOOO000OO000O #line:236
        else :#line:237
            return False #line:238
    def do_read (O0OO00O0OO0O0OO00 ):#line:240
        O000O00O000OO0000 =O0OO00O0OO0O0OO00 .get_read_code ()#line:241
        if O000O00O000OO0000 ==False :return False #line:242
        OO0OOOOOOOOO0OO00 =0 #line:243
        OO00OOOOO0O0O0O0O ={'Accept':'*/*','X-Requested-With':'XMLHttpRequest','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309080f) XWEB/8461 Flue','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Origin':'http://wxread-index-9699272255.cos-website.ap-beijing.9699272255.abqabq.sbs','Referer':'http://wxread-index-9699272255.cos-website.ap-beijing.9699272255.abqabq.sbs/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','Cookie':'thinkphp_show_page_trace=0|0',}#line:254
        while True :#line:255
            print ('-'*50 )#line:256
            O0O000O0OOOO0OO00 ='http://wxread-index-9699272255.cos-website.ap-beijing.9699272255.abqabq.sbs/index/index/get_article.html'#line:257
            OO0OOOOOO000OOOO0 =f'code={O000O00O000OO0000}&uid={O0OO00O0OO0O0OO00.userid}'#line:258
            O00O00OO0O0OOO0OO =requests .post (O0O000O0OOOO0OO00 ,headers =OO00OOOOO0O0O0O0O ,data =OO0OOOOOO000OOOO0 )#line:259
            OOOO000OOOOO0OOOO =O00O00OO0O0OOO0OO .json ()#line:260
            if OOOO000OOOOO0OOOO .get ('code')==0 :#line:261
                print ('未知情况')#line:262
                time .sleep (1.5 )#line:263
            if OOOO000OOOOO0OOOO .get ('code')==1 :#line:264
                OOOOOO0O00O0OO00O =OOOO000OOOOO0OOOO ['data']['info']['link']#line:265
                O000OO0OOOOO0000O =OOOO000OOOOO0OOOO ['data']['info']['rid']#line:266
                O00000OO0OO0O00OO =getinfo (OOOOOO0O00O0OO00O )#line:267
                if OO0OOOOOOOOO0OO00 ==0 or O0OO00O0OO0O0OO00 .flag ==1 :#line:268
                    OO0OO00O00OO0OO00 =list (O00000OO0OO0O00OO )#line:269
                    OO0OO00O00OO0OO00 [4 ]='oneischeck'#line:270
                    if O0OO00O0OO0O0OO00 .testCheck (OO0OO00O00OO0OO00 ,OOOOOO0O00O0OO00O )==False :#line:271
                        return False #line:272
                    OO0OOOOOOOOO0OO00 =1 #line:273
                if O0OO00O0OO0O0OO00 .testCheck (O00000OO0OO0O00OO ,OOOOOO0O00O0OO00O )==False :#line:274
                    return False #line:275
                print ('开始本次阅读')#line:276
                OO0OO00O0O000O0OO =random .randint (6 ,9 )#line:277
                print (f'本次模拟读{OO0OO00O0O000O0OO}秒')#line:278
                time .sleep (OO0OO00O0O000O0OO )#line:279
                OOO0000OOOO000O0O ='http://wxread-index-9699272255.cos-website.ap-beijing.9699272255.abqabq.sbs/index/index/auth_record.html'#line:280
                OOOO00OO0OO00O0O0 =f'rid={O000OO0OOOOO0000O}&time_is_gou=1'#line:281
                O0O0O00OOOOOO0OO0 =requests .post (OOO0000OOOO000O0O ,headers =OO00OOOOO0O0O0O0O ,data =OOOO00OO0OO00O0O0 )#line:282
                O00OO00000O0000O0 =O0O0O00OOOOOO0OO0 .json ()#line:283
                if O00OO00000O0000O0 .get ('code')!=0 :#line:284
                    print ('阅读进度',O00OO00000O0000O0 ['txt'])#line:285
                if O00OO00000O0000O0 .get ('code')==0 :#line:286
                    print ('未知情况',)#line:287
                    continue #line:288
                if O00OO00000O0000O0 .get ('code')==1 :#line:289
                    O0OO00O0OO0O0OO00 .flag =0 #line:290
                if O00OO00000O0000O0 .get ('code')==2 :#line:291
                    O0OO00O0OO0O0OO00 .flag =1 #line:292
                    print ('过检测异常重新过检测')#line:293
                    time .sleep (1.2 )#line:294
                if O00OO00000O0000O0 .get ('code')==3 :#line:295
                    print ('阅读结束')#line:296
                    time .sleep (1.2 )#line:297
                    O0OO00O0OO0O0OO00 .read_result (O000O00O000OO0000 ,OO00OOOOO0O0O0O0O )#line:298
                    return True #line:299
            if OOOO000OOOOO0OOOO .get ('code')==3 :#line:300
                time .sleep (1.2 )#line:301
                O0OO00O0OO0O0OO00 .read_result (O000O00O000OO0000 ,OO00OOOOO0O0O0O0O )#line:302
                return True #line:303
    def read_result (O000O0OOO00OOOO00 ,O0OO000O0O0000OO0 ,O0O0OO000O0O0O000 ):#line:304
        O00OOOO0000OOOOO0 ='http://wxread-index-9699272255.cos-website.ap-beijing.9699272255.abqabq.sbs/index/index/read_result.html'#line:305
        O00O0OOO000OOOO00 =f'code={O0OO000O0O0000OO0}'#line:306
        O0O0OOOOO00OO0OOO =requests .post (O00OOOO0000OOOOO0 ,headers =O0O0OO000O0O0O000 ,data =O00O0OOO000OOOO00 )#line:307
        print ('阅读结算结果',O0O0OOOOO00OO0OOO .text )#line:308
    def testCheck (O00O0O0O00OOO00OO ,OOO0OOOO00OO0O00O ,OO000O00O0000O0O0 ):#line:309
        if OOO0OOOO00OO0O00O [4 ]==[]:#line:310
            print (O00O0O0O00OOO00OO .name ,'这个链接没有获取到微信号id',OO000O00O0000O0O0 )#line:311
            return True #line:312
        if checkDict .get (OOO0OOOO00OO0O00O [4 ])!=None :#line:313
            O00O0O0O00OOO00OO .setstatus ()#line:314
            for OOOO0OO00O0O000O0 in range (60 ):#line:315
                if OOOO0OO00O0O000O0 %30 ==0 :#line:316
                    push (f'点点阅读过检测:{O00O0O0O00OOO00OO.name}',OO000O00O0000O0O0 ,OOO0OOOO00OO0O00O [3 ],'ybxkhh',O00O0O0O00OOO00OO .uids ,O00O0O0O00OOO00OO .key )#line:317
                O00O0000OOO000000 =O00O0O0O00OOO00OO .getstatus ()#line:318
                if O00O0000OOO000000 =='0':#line:319
                    print (O00O0O0O00OOO00OO .name ,'过检测文章已经阅读')#line:320
                    return True #line:321
                elif O00O0000OOO000000 =='1':#line:322
                    print (O00O0O0O00OOO00OO .name ,f'正在等待过检测文章阅读结果{OOOO0OO00O0O000O0}秒。。。')#line:323
                    time .sleep (1 )#line:324
                else :#line:325
                    print (O00O0O0O00OOO00OO .name ,O00O0000OOO000000 )#line:326
                    print (O00O0O0O00OOO00OO .name ,'服务器异常')#line:327
                    return False #line:328
            print (O00O0O0O00OOO00OO .name ,'过检测超时中止脚本防止黑号')#line:329
            return False #line:330
        else :#line:331
            return True #line:332
    def withdrawal (OO00OOO0OO0O000OO ):#line:333
        pass #line:334
    def run (O00OOOOOOOO0OO000 ):#line:335
        if O00OOOOOOOO0OO000 .index ():#line:336
            time .sleep (2 )#line:337
            O00OOOOOOOO0OO000 .do_read ()#line:338
            time .sleep (2 )#line:339
            O00OOOOOOOO0OO000 .index ()#line:340
def getEnv (O0OO0OOO0O0OOOOOO ):#line:341
    O0000O0O0O0O0OO00 =os .getenv (O0OO0OOO0O0OOOOOO )#line:342
    if O0000O0O0O0O0OO00 ==None :#line:343
        print (f'{O0OO0OOO0O0OOOOOO}没有获取到，使用本地参数')#line:344
        return False #line:345
    try :#line:346
        O0000O0O0O0O0OO00 =json .loads (O0000O0O0O0O0OO00 .replace ("'",'"').replace ("\n","").replace (" ","").replace ("\t",""))#line:347
        return O0000O0O0O0O0OO00 #line:348
    except Exception as OO0O0OOOOO00OOO00 :#line:349
        print ('错误:',OO0O0OOOOO00OOO00 )#line:350
        print ('你填写的变量是:',O0000O0O0O0O0OO00 )#line:351
        print ('请检查变量参数是否填写正确')#line:352
        print (f'{O0OO0OOO0O0OOOOOO}使用本地参数')#line:353
if __name__ =='__main__':#line:354
    loc_push_config = {"printf": 1, "threadingf": 0, "appToken": "AT_9KCY75ixxxxu6JC"}
    loc_ddydconfig = [
        {'name': '备注名', 'cookie': 'PHPSESSID=fbbxxxxba1','key': '4e9b9xxxxxx451f2a78a', 'uids': 'UID_11ZHxxxxxx2lncQ'},
        # {'name': '备注名', 'cookie': 'PHPSESSID=xxxx','key': '4e9b9xxxxxx451f2a78a', 'uids': 'UID_11ZHxxxxxx2lncQ'},
        # {'name': '备注名', 'cookie': 'PHPSESSID=xxxx','key': '4e9b9xxxxxx451f2a78a', 'uids': 'UID_11ZHxxxxxx2lncQ'}
    ]
    # --------------------------------------------------------
    push_config = getEnv('push_config')
    if push_config == False: push_config = loc_push_config
    print(push_config)
    ddydconfig = getEnv('ddydconfig')
    if ddydconfig == False: ddydconfig = loc_ddydconfig
    print(ddydconfig)
    printf = push_config['printf']  # 打印调试日志0不打印，1打印，若运行异常请打开调试
    appToken = push_config['appToken']  # 这个是填wxpusher的appToken
    threadingf = push_config['threadingf']
    getmsg()
    tl = []
    getmsg()
    if threadingf == 1:
        tl = []
        for cg in ddydconfig:
            print('*' * 50)
            print(f'开始执行{cg["name"]}')
            api = WXYD(cg)
            t = threading.Thread(target=api.run, args=())
            tl.append(t)
            t.start()
            time.sleep(0.5)
        for t in tl:
            t.join()
    elif threadingf == 0:
        for cg in ddydconfig:
            print('*' * 50)
            print(f'开始执行{cg["name"]}')
            api = WXYD(cg)
            api.run()
            print(f'{cg["name"]}执行完毕')
            time.sleep(3)
    else:
        print('请确定推送变量中threadingf参数是否正确')
    print('全部账号执行完成')
    time.sleep(15)
