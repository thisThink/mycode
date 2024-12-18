'''
不想抽奖后自动领取的就注释掉isRun = True
    isRun = False#isRun为false抽奖后不直接领取
    isRun = True#isRun为true抽奖后直接领取    不领取把这行注释掉
变量:
    青龙变量为
        chinaUnicomCookie
    本地运行替换
        token1&token2&token3
至于多token格式支持多种并且可混用   & ^  %  回车  如果想自己添加其他自己改。

登录失败也会有,自己加同ip下appid 或者同ip下登录app再运行。多次失败或者502那就换个时间段运行吧。


    &方式:token1&token2&token3

    %方式:token1%token2%token3
    
    ^方式:token1^token2^token3

    回车方式:
    token1
    token2
    token3

助力只有一次 根据当前目录下的助力码.log里面的param值去助力
自己多号或者加其他的也可参考(https://contact.bol.wo.cn/market-act/js/app.js)接口 

by:翼城

'''


import os
import re
import ssl
import json
import httpx
import asyncio
import aiohttp
import certifi
import logging
import datetime
import pandas as pd
from prettytable import PrettyTable

from urllib.parse import urlparse, parse_qs
class AsyncSessionManager:
    def __init__(self, timeout=None):
        self.client = None
        self.timeout = timeout

    async def __aenter__(self):
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        ssl_context.set_ciphers('DEFAULT@SECLEVEL=1')
        
        if self.timeout:
            self.client = httpx.AsyncClient(
                verify=ssl_context,
                limits=httpx.Limits(max_connections=1000),
                timeout=self.timeout
            )
        else:
            self.client = httpx.AsyncClient(
                verify=ssl_context,
                limits=httpx.Limits(max_connections=1000)
            )
        return self.client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()
async def mask_middle_four(value):
    if isinstance(value, str):
        if len(value) >= 11:
            return value[:3] + "####" + value[-4:]
        else:
            raise ValueError("输入的字符串长度不足以截取中间四位")
    else:
        raise TypeError("输入类型错误，应为字符串")
    
# class NoDuplicatesFilter(logging.Filter):
#     def __init__(self):
#         self._logged = set()

#     def filter(self, record):
#         msg = record.getMessage()
#         if msg in self._logged:
#             return False
#         self._logged.add(msg)
#         return True
class NoDuplicatesFilter(logging.Filter):
    def __init__(self):
        self._logged = set()

    def filter(self, record):
        msg = record.getMessage()
        # 使用正则表达式提取电话号码和param值
        # match = re.match(r'(\d{3}####\d{4}) (.*)', msg)
        match = re.match(r'(\d{11}) (.*)', msg)

        if match:
            phone = match.group(1)
            friend_info_str = match.group(2)
            try:
                # 尝试将friend_info字符串转换为字典
                friend_info = eval(friend_info_str)
                param = friend_info.get('param')
                # 将电话号码和param值组合作为键
                unique_key = (phone, param)
                if unique_key in self._logged:
                    return False
                self._logged.add(unique_key)
            except (SyntaxError, NameError):
                # 如果friend_info字符串不是有效的字典格式，允许记录
                pass
        return True

class TaskProcessor:
    def __init__(self, ltToken):
        self.ltToken = ltToken
        self.userToken = None
        self.ecs_token = None
        self.wxarrKey = None
        self.friendsKey = None
        self.currPhone = None
        self.Phones = None
        self.sharewxarr = []
        self.sharefriends = []

        self.urls = {
            'onLine': "https://m.client.10010.com/mobileService/onLine.htm",
            'ticket': "https://m.client.10010.com/mobileService/openPlatform/openPlatLineNew.htm?to_url=https://contact.bol.wo.cn/market",
            'marketUnicomLogin': "https://backward.bol.wo.cn/prod-api/auth/marketUnicomLogin",
            'getAllActivityTasks': "https://backward.bol.wo.cn/prod-api/promotion/activityTask/getAllActivityTasks?activityId=12",
            'yearEndActivities': "https://backward.bol.wo.cn/market-act/yearEndActivities",
            'checkShare': "https://backward.bol.wo.cn/prod-api/promotion/activityTaskShare/checkShare",
            'checkHelp': "https://backward.bol.wo.cn/prod-api/promotion/activityTaskShare/checkHelp",
            'bdyearEndActivities': "https://suggestion.baidu.com/su?wd=https://contact.bol.wo.cn/market-act/yearEndActivities",
            'getUserRaffleCount': "https://backward.bol.wo.cn/prod-api/promotion/home/raffleActivity/getUserRaffleCount?id=12",
            'userRaffle': "https://backward.bol.wo.cn/prod-api/promotion/home/raffleActivity/userRaffle?id=12&channel=",
            'validateCaptcha': "https://backward.bol.wo.cn/prod-api/promotion/home/raffleActivity/validateCaptcha?id=12",
            'grantPrize': "https://backward.bol.wo.cn/prod-api/promotion/home/raffleActivity/grantPrize",
            'getMyPrize': "https://backward.bol.wo.cn/prod-api/promotion/home/raffleActivity/getMyPrize",
        }
        self.headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 12; leijun Pro Build/SKQ1.22013.001);unicom{version:android@11.0702}",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            # 'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.common_value = None  

    async def get_ecstoken(self, session):
        payload = {
            'isFirstInstall': "1",
            'version': "android@11.0702",
            'token_online': self.ltToken
        }
        response_Value = await self.requestsPost('onLine', payload, session)
        try:
            valueJson=json.loads(response_Value)
            await asyncio.sleep(1)
            desmobile=valueJson.get("desmobile")
            if desmobile is None:
                print("未获取到手机号",valueJson.get("dsc"))
                return None
            self.currPhone=await mask_middle_four(desmobile);
            self.Phone=(desmobile);
            value=valueJson.get("ecs_token")
            self.ecs_token=value
            return value
        except  json.JSONDecodeError:
            print("get_ecstoken json error",response_Value)
            return None
    async def get_ticket(self, session):
        response_Value = await self.requestsGet('ticket',  session)
        try:
            parsed_url = urlparse(response_Value)
            query_params = parse_qs(parsed_url.query)
            ticket = query_params.get('ticket', [None])[0] 
            self.ticket=ticket
            return ticket
        except  json.JSONDecodeError:
            print("get_ticket json error")
            return None
        except Exception as e:
            print(f"error: {e}")
            return None
    async def get_qycsbdrequest(self, session):
        response_Value = await self.requestsGet('bdyearEndActivities',  session)
        try:
            
            return response_Value
        except Exception as e:
            print(f"error: {e}")
            return None
    async def get_qycslogin(self, session):
        payload = {
            
        }
        response_Value = await self.requestsPost('marketUnicomLogin',payload,  session)
        try:
            token=json.loads(response_Value).get("data").get("token")
            self.userToken=token
            return token
        except  json.JSONDecodeError:
            print("get_qycslogin json error",response_Value)
            return None
    async def get_qycsgetMyPrize(self, session):
        payload = {
            "id": 12,
            "type": 0,
            "page": 1,
            "limit": 100,
        }
        payload=json.dumps(payload)
        response_Value = await self.requestsPost('getMyPrize',payload,  session)
        try:
            jsonValue = json.loads(response_Value)
            lists = jsonValue.get("data", {}).get("list", [])
            if lists:
                print(f"{self.currPhone}:奖品未领取数: ", len(lists))
                print(f"{self.currPhone}:开始统计自己懒而未领取的奖品信息")
                table = PrettyTable()
                table.field_names = ["商品名称", "商品id", "领取时间", "失效时间"]
                for item in lists:
                    table.add_row([item.get("prizesName"), item.get("id"), item.get("createTime"), item.get("deadline")])
                
                print(table)
            else:
                print(f"{self.currPhone}:没有奖品可以领取")

            return lists
        except  json.JSONDecodeError:
            print("get_qycslogin json error",response_Value)
            return None
    async def get_qycsgrantPrize(self, session,lotteryRecordId):
        payload = {
            "recordId": lotteryRecordId,
        }
        payload=json.dumps(payload)
        response_Value = await self.requestsPost('grantPrize',payload,  session)
        try:
            msg=json.loads(response_Value).get("msg")
            print("领取->",msg)
        except  json.JSONDecodeError:
            print("get_qycslogin json error",response_Value)
            return None
    async def get_qycsuserRaffle(self, session,num=3):
        payload = {
            
        }
        response_Value = await self.requestsPost('userRaffle',payload,  session)
        try:
            response_Value=json.loads(response_Value)
            if response_Value.get("code")==200:
                num=0
                if response_Value.get("data"):
                    lotteryRecordId=response_Value.get("data").get("lotteryRecordId")
                    print(f"{self.currPhone}:抽奖成功:",response_Value.get("data").get("prizesName"))
                    if isRun==True:
                        print(f"{self.currPhone}:开始领取:",response_Value.get("data").get("prizesName"))
                        await self.get_qycsgrantPrize(session,lotteryRecordId)
                    else:
                        print(f"{self.currPhone}:不执行领取:",response_Value.get("data").get("prizesName"))


                return response_Value
            elif response_Value.get("code")==500:
                await self.get_qycsuserRaffle2(session)
                if num > 1: 
                    await self.get_qycsuserRaffle(session, num - 1)
                # print("抽奖失败")
            else:
                print("没有更多的尝试次数")

        except  json.JSONDecodeError as e:
            print(f"get_qycsuserRaffle error: {e}")
            return None
        
    async def get_qycsuserRaffle2(self, session):
        payload = {
            
        }
        response_Value = await self.requestsPost('validateCaptcha',payload,  session)
        try:
            response_Value=json.loads(response_Value)
            if response_Value.get("code")==200:
                print(f"{self.currPhone}:人机验证成功")
                # print(response_Value)
            elif response_Value.get("code")==500:
                print(f"{self.currPhone}:人机验证失败")
        except  json.JSONDecodeError:
            print("get_qycsuserRaffle2 json error")
            return None
        
    async def get_qycscheckShare(self, session):
        payload = {
            
        }
        self.wxarrKey=self.sharewxarr[0].get("param")
        response_Value = await self.requestsPost('checkShare',payload,  session)
        try:
            msg=json.loads(response_Value).get("msg")
            print(f"{self.currPhone}:分享->:"+msg)
        except  json.JSONDecodeError:
            print("get_qycscheckShare json error")
            return None
    async def get_qycscheckHelp(self, session,friendKey):
        payload = {
            
        }
        self.friendsKey=friendKey
        response_Value = await self.requestsPost('checkHelp',payload,  session)
        try:
            msg=json.loads(response_Value).get("msg")
            print("邀请好友->"+msg)
        except  json.JSONDecodeError:
            print("get_qycscheckHelp json error")
            return None
        
    async def get_qycsUserRaffleCount(self, session):
        payload = {
            
        }
        self.wxarrKey=self.sharewxarr[0].get("param")
        response_Value = await self.requestsPost('getUserRaffleCount',payload,  session)
        try:
            data=json.loads(response_Value).get("data")

            return data
        except  json.JSONDecodeError:
            print("get_qycsUserRaffleCount json error",response_Value)
            return None

    async def yearEndActivities(self, session):
        self.wxarrKey=self.sharewxarr[0].get("param")
        response_Value = await self.requestsGet('yearEndActivities', session)
        try:
            token=json.loads(response_Value).get("data").get("token")
            self.userToken=token
            return token
        except  json.JSONDecodeError:
            print("yearEndActivities json error")
            return None
    async def get_qycsAllActivityTasks(self, session):
        payload = {
            
        }
        response_Value = await self.requestsGet('getAllActivityTasks', session)
        try:
            active_id_listarr=json.loads(response_Value).get("data", [])
            for item in active_id_listarr.get("activityTaskUserDetailVOList"):
                if item.get("name") == "分享至朋友圈" or item.get("id") == "63" or item.get("id") == 63:
                    wx_info = {
                        "param": item.get("param1"),
                        "activityId": item.get("activityId"),
                        "name": item.get("name"),
                    }
                    self.sharewxarr.append(wx_info)
                elif item.get("name") == "邀请好友助力"or item.get("id") == "65"or item.get("id") == 65:
                    friend_info = {
                        "param": item.get("param1"),
                        "activityId": item.get("activityId"),
                        "name": item.get("name"),
                    }
                    self.sharefriends.append(friend_info)

                    logger.critical(f"{self.Phone} {friend_info}")
            # print(self.sharewxarr)
            # print(self.sharefriends)
        except  json.JSONDecodeError:
            print("get_qycsAllActivityTasks json error",response_Value)
            return None
        except Exception as e:
            print(f"error: {e}")
            return None

    async def requestsPost(self, url_name, payload, session):
        try:
            url = self.urls.get(url_name)
            if url_name=='marketUnicomLogin':
                url+='?ticket='+self.ticket
            if url_name=='checkShare' and self.wxarrKey:
                url+='?checkKey='+self.wxarrKey
            if url_name=='checkHelp' and self.friendsKey:
                url+='?checkKey='+self.friendsKey
            headers = getattr(self, 'headers', None)
            if url_name in ('getUserRaffleCount','userRaffle','checkHelp'):
                if self.userToken:
                    headers['Authorization'] = 'Bearer '+self.userToken 
            if url_name in ('grantPrize','getMyPrize'):
                headers['Accept'] = "application/json, text/plain, */*" 
                headers['Accept-Encoding'] = "gzip, deflate, br, zstd"
                headers['Content-Type'] =  "application/json"
                headers['sec-ch-ua-mobil'] =   "?1"
                headers['Origin'] = "https://backward.bol.wo.cn"
            # async with session.post(url,headers=headers, data=payload) as response:
            response=await session.post(url, headers=headers, data=payload)
            text = response.text
            return text
        except Exception as e:
            return f"Error: {e}"
    async def requestsGet(self, url_name,  session):
        try:

            url = self.urls.get(url_name)
            headers = self.headers.copy() 
            no_redirect_urls = {"ticket","yearEndActivities"} #瑞数相关去了，这里直接重定向获取算了....
            isredirect = False if url_name in no_redirect_urls else True
            if self.ecs_token:
                headers['Cookie'] = 'ecs_token='+self.ecs_token 
            if self.userToken:
                headers['Authorization'] = 'Bearer '+self.userToken 
            if  self.wxarrKey:
                url+='?key='+self.wxarrKey
            if url_name=='bdyearEndActivities':
                url+=f'&cb=suggestion'
            # async with session.get(url,headers=headers,allow_redirects=isredirect) as response:
            response=await session.get(url, headers=headers, follow_redirects=isredirect)
            stauts=response.status_code 
            if not isredirect and stauts in (301, 302, 303, 307, 308):
                return response.headers.get('Location')
            # text = await response.text()
            text = response.text
            return text
        except Exception as e:
            return f"Error: {e}"

    async def process_task(self, session,delay):
        ess_token= await self.get_ecstoken(session)
        ticket= await self.get_ticket(session)
        await asyncio.sleep(delay)
        token= await self.get_qycslogin(session)#登录
        if token:
            print(f"{self.currPhone}:登录成功")
        else:
            print(f"{self.currPhone}:登录失败")
            return None
        alltask= await self.get_qycsAllActivityTasks(session)#查询任务
        await asyncio.sleep(delay)
        # alltask= await self.yearEndActivities(session)#
        print(f"{self.currPhone}:开始分享任务(每天首次有效)")
        await self.get_qycscheckShare(session)#分享确认
        await asyncio.sleep(delay)
        await self.get_qycsbdrequest(session)#访问分享链接
        await asyncio.sleep(delay)
        friendKey=""#助力好友key
        # get_qycscheckHelp= await self.get_qycscheckHelp(session,friendKey)#助力确认
        await asyncio.sleep(delay)
        print(f"{self.currPhone}:开始查询可抽奖次数")
        datanum= await self.get_qycsUserRaffleCount(session)#查抽奖次数
        print(f"{self.currPhone}:抽奖次数"+str(datanum))
        # datanum=1
        for i in range(datanum):
            print(f"{self.currPhone}:开始抽奖第 {i + 1} 次")
            await self.get_qycsuserRaffle(session)

        await asyncio.sleep(1)
        await self.get_qycsgetMyPrize(session)

        return None

    async def main(self):
        delay = 0.6
        # async with aiohttp.ClientSession() as session:
        async with AsyncSessionManager() as session:
            task = asyncio.create_task(self.process_task(session,delay))
            await task

yf = datetime.datetime.now().strftime("%Y%m")
log_filename = f'./联通权益超市助力信息.log'
logging.basicConfig(level=logging.CRITICAL,
                    format='%(asctime)s -- %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=log_filename, 
                    filemode='a', encoding='utf-8')
logger = logging.getLogger(__name__)
logger.addFilter(NoDuplicatesFilter())

async def main(tokens):
    processors = [TaskProcessor(token) for token in tokens]
    tasks = [processor.main() for processor in processors]
    await asyncio.gather(*tasks)
splittt = r'[\n&^@%]+'





isRun = False#isRun为false抽奖后不直接领取
isRun = True#isRun为true抽奖后直接领取    不领取把这行注释掉
if __name__ == "__main__":
    PHONES =os.environ.get('chinaUnicomCookie') or '''token1&token2&token3''' 
    ltTokens_list = re.split(splittt, PHONES)
    total_tasks = len(ltTokens_list)
    print("共有任务数："+str(total_tasks))
    # print("下面几行日志少一字,你妈给你爹带一顶锃光的小绿帽");
    print("写权益本卖完钱还运行这个要脸?");
    print("买完本自用不共享还运行这个也要点脸?");
    print("收费代挂还运行这个要脸?");
    print("你们几种人不怕孩子那天没屁眼!");
    asyncio.run(main(ltTokens_list))

