# 软件:建行生活
# 活动信息: 奋斗季cc豆 功能：每日营收，签到 浏览任务，答题，抽奖，专区任务
# 先开抓包，先开抓包，进建行生活app，没抓到等两小时在抓。用的2.1.3版本
# https://yunbusiness.ccb.com/basic_service/txCtrl?txcode=A3341SB06下的deviceid值，和请求体中ENCRYPT_MSG值
# https://yunbusiness.ccb.com/clp_service/txCtrl?txcode=autoLogin里面的请求体全部
# 专区任务，专区抓fission-events.ccbft.com，全部cookie
# 格式 ccdck = deviceid值#ENCRYPT_MSG值#auto请求体值#cookie值
# 定时：0 0 0 * * *
# 注: 此脚本仅限个人使用,不得传播
# 作者: 木兮
import os
import random
import re
import time
from datetime import datetime

import requests

app_ua = ''  # 用app的ua，不填也能跑

user_cookie = os.getenv("ccdck")

'''
doll_flag  1开启抓娃娃，0关闭
doll_draw 抓娃娃次数，总数小于10
'''
doll_flag = 0  # 1开启抓娃娃，0关闭
doll_draw = 1

'''
basket_flag  1开启投篮球，0关闭
basket_draw  投篮球次数，总数小于5
'''
basket_flag = 1
basket_draw = 5

'''
box_flag   1开启开盲盒，0关闭
box_id  开盲盒类型，1为88豆，2为188豆，3为10000豆
box_draw   开盲盒次数，总数小于5
'''
box_flag = 0
box_id = 1
box_draw = 2

debug = 0  # 开启调式


class CCD:
    base_header = {
        'Host': 'm3.dmsp.ccb.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': app_ua,
        'origin': 'https://m3.dmsp.ccb.com',
        'x-requested-with': 'com.tencent.mm',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json'
    }
    token_headers = {
        'Host': 'event.ccbft.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': app_ua,
        'origin': 'https://event.ccbft.com',
        'x-requested-with': 'com.ccb.longjiLife',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json'
    }

    def __init__(self, ccb_cookie):
        ccb_cookie_parts = ccb_cookie.split("#")
        self.deviceid, self.tx_payload, self.login_payload, self.zq_cookie = ccb_cookie_parts
        self.ccbParam = None
        self.ccb_uuid = None
        self.zhc_token = None
        self.zq_headers = {
            'Host': 'fission-events.ccbft.com',
            'accept': 'application/json, text/plain, */*',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': app_ua,
            'origin': 'https://fission-events.ccbft.com',
            'Cookie': self.zq_cookie,
            'content-type': 'application/json'
        }

    # 随机延迟默认1-1.5
    def sleep(self, min_delay=1, max_delay=1.5):
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)

    def send_request(self, url, headers, data=None, method='GET', cookies=None):
        with requests.Session() as session:
            session.headers.update(headers)
            if cookies is not None:
                session.cookies.update(cookies)

            try:
                if method == 'GET':
                    response = session.get(url)
                elif method == 'POST':
                    response = session.post(url, json = data)
                else:
                    raise ValueError('Invalid HTTP method.')

                response.raise_for_status()
                if debug:
                    print(response.json())
                return response.json()

            except requests.Timeout as e:
                print("请求超时:", str(e))

            except requests.RequestException as e:
                print("请求错误:", str(e))

            except Exception as e:
                print("其他错误:", str(e))

            # 请求发生错误，但不抛出异常，继续执行下一个请求
            return None

        # 获取app Session

    def get_session(self):
        url = "https://yunbusiness.ccb.com/clp_service/txCtrl?txcode=autoLogin"

        headers = {
            'Host': 'yunbusiness.ccb.com',
            'appversion': '2.1.3.001',
            'devicetype': 'Android',
            'zipversion': '1.0',
            'accept': 'application/json',
            'deviceid': self.deviceid,
            'mbc-user-agent': f'MBCLOUDCCB/Android/Android 13/2.13/2.00/{self.deviceid}/Decrypt-UTF8/1080*2316/',
            'content-type': 'application/json; charset=utf-8',
            'Connection': 'keep-alive',
        }

        try:
            response = requests.post(url, headers = headers, data = self.login_payload)

            setCookie = response.headers.get('Set-Cookie')
            session_cookie = re.search(r'SESSION=([^;]+)', setCookie)

            if session_cookie:
                session_value = session_cookie.group(1)
                headers['cookie'] = f'SESSION={session_value}'

                login_data = requests.post(url, headers = headers, data = self.login_payload).json()
                errCode = login_data.get('errCode', '')
                if errCode != "0":
                    print(login_data)
                else:
                    tx_url = 'https://yunbusiness.ccb.com/basic_service/txCtrl?txcode=A3341SB06'
                    payload = {
                        "regionCode": "360400",
                        "PLATFORM_ID": "YS44000010000078",
                        "chnlType": "1",
                        "APPEND_PARAM": f"{self.deviceid}|@|2409:895a:bf18:420b:1792:6fc4:2a81:a4da|@|Mobile|@|116.248996|@|29.356575|@|01|@|13|@|M2012K10C|@|02:00:00:00:00:00|@|360400|@|610100|@|936DD6661744EB6A1786D059A9EF5D633CAB61B9|@|2.1.3.001",
                        "ENCRYPT_MSG": self.tx_payload
                    }
                    param_data = requests.post(tx_url, headers = headers, json = payload).json()
                    errCode = param_data.get('errCode')
                    if errCode != '0':
                        print(param_data)
                    else:
                        self.ccbParam = param_data.get('data', {}).get('ENCRYPTED_MSG', '')
                        self.get_token()
            else:
                print("token刷新失败")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def get_token(self):
        try:
            url = f"https://event.ccbft.com/api/flow/nf/shortLink/redirect/ccb_gjb?CCB_Chnl=2030023&ccbParamSJ={self.ccbParam}&cityid=610100&CITYID=610100&userCityId=360400&USERCITYID=360400"

            payload = {
                "shortId": "polFsWD2jPnjhOx9ruVBcA",
                "archId": "ccb_gjb",
                "ccbParamSJ": self.ccbParam,
                "channelId": "ccbLife",
                "ifCcbLifeFirst": True
            }

            return_data = self.send_request(url, headers = self.token_headers, data = payload, method = 'POST')

            redirect_url = return_data['data'].get('redirectUrl')
            self.ccb_uuid = return_data['data'].get('ccbLifeUUID')
            token = self.extract_token(redirect_url)
            if token:
                self.zhc_token = token
                if self.auth_login(token):
                    self.user_info()
                    self.sign_in()
                    self.getlist()
                    self.answer_state()
                    print('\n======== 专区任务 ========')
                    time.sleep(random.randint(3, 5))
                    self.get_csrftoken()
                    self.get_user_ccd()
                else:
                    print(return_data)
        except Exception as e:
            print(e)

    def extract_token(self, redirect_url):
        start_token_index = redirect_url.find("__dmsp_token=") + len("__dmsp_token=")
        end_token_index = redirect_url.find("&", start_token_index)

        token = None
        if start_token_index != -1 and end_token_index != -1:
            token = redirect_url[start_token_index:end_token_index]
        return token

    # 登录
    def auth_login(self, token):
        url = 'https://m3.dmsp.ccb.com/api/businessCenter/auth/login'
        payload = {"token": token, "channelId": "ccbLife"}
        return_data = self.send_request(url, headers = self.base_header, data = payload, method = 'POST')
        self.sleep()
        if return_data['code'] != 200:
            print(return_data['message'])
            return False
        else:
            return True

    # 查询用户等级
    def user_info(self):
        url = f'https://m3.dmsp.ccb.com/api/businessCenter/mainVenue/getUserState?zhc_token={self.zhc_token}'
        return_data = self.send_request(url, headers = self.base_header, method = 'POST')

        if return_data['code'] != 200:
            print(return_data['message'])
        else:
            current_level = return_data['data'].get('currentLevel')
            need_exp = return_data['data'].get('nextMonthProtectLevelNeedGrowthExp') - return_data['data'].get(
                'growthExp')
            level = return_data['data'].get('currentProtectLevel')
            reward_id = return_data['data'].get('zhcRewardInfo').get('id')
            reward_type = return_data['data'].get('zhcRewardInfo').get('rewardType')
            reward_value = return_data['data'].get('zhcRewardInfo').get('rewardValue')
            print(f"当前用户等级{current_level}级")
            print(f"距下一级还需{need_exp}成长值")
            self.income(level, reward_id, reward_type, reward_value)

    # 每日营收
    def income(self, level, reward_id, reward_type, reward_value):
        url = f'https://m3.dmsp.ccb.com/api/businessCenter/mainVenue/receiveLevelReward?zhc_token={self.zhc_token}'
        payload = {"level": level, "rewardId": reward_id, "levelRewardType": reward_type}
        return_data = self.send_request(url, headers = self.base_header, data = payload, method = 'POST')
        self.sleep()
        if return_data['code'] != 200:
            print(return_data['message'])
        else:
            print(f"今日营收: {reward_value}cc豆")

    # 签到
    def sign_in(self):
        signin_url = f'https://m3.dmsp.ccb.com/api/businessCenter/taskCenter/signin?zhc_token={self.zhc_token}'
        signin_payload = {"taskId": 96}
        return_data = self.send_request(url = signin_url, headers = self.base_header, data = signin_payload,
                                        method = 'POST')
        self.sleep()
        if return_data['code'] != 200:
            print(return_data['message'])
        else:
            print(return_data['message'])

    # 获取浏览任务列表
    def getlist(self):
        try:
            list_url = f'https://m3.dmsp.ccb.com/api/businessCenter/taskCenter/getTaskList?zhc_token={self.zhc_token}'
            payload = {"publishChannels": "03", "regionId": "110100"}  # 440300

            return_data = self.send_request(url = list_url, headers = self.base_header, data = payload, method = 'POST')

            if return_data['code'] != 200:
                print(return_data['message'])
            else:
                task_list = return_data['data'].get('浏览任务')

                for value in task_list:
                    complete_status = value['taskDetail'].get('completeStatus')

                    if complete_status == '02':
                        print(f"--已完成: {value['taskName']}")
                    else:
                        task_id = value['id']
                        task_name = value['taskName']
                        print(f'---去完成: {task_name}')
                        self.execute_task(task_id)
        except Exception as e:
            print(e)

    def execute_task(self, task_id):
        try:
            browse_url = f'https://m3.dmsp.ccb.com/api/businessCenter/taskCenter/browseTask?zhc_token={self.zhc_token}'
            receive_url = f'https://m3.dmsp.ccb.com/api/businessCenter/taskCenter/receiveReward?zhc_token={self.zhc_token}'
            payload = {"taskId": task_id, "browseSec": 1}

            browse_data = self.send_request(browse_url, headers = self.base_header, data = payload, method = 'POST')

            if browse_data['code'] != 200:
                print(browse_data['message'])
            else:
                print(browse_data['message'])

                receive_data = self.send_request(receive_url, headers = self.base_header, data = payload,
                                                 method = 'POST')
                if receive_data['code'] != 200:
                    print(receive_data['message'])
                else:
                    print(receive_data['message'])
        except Exception as e:
            print(e)

    # 获取答题state
    def answer_state(self):
        url = f'https://m3.dmsp.ccb.com/api/businessCenter/zhcUserDayAnswer/getAnswerStatus?zhc_token={self.zhc_token}'
        return_data = self.send_request(url, headers = self.base_header)
        if return_data['code'] == 200:
            if return_data['data'].get('answerState') == 'Y':
                print(return_data['message'])
            else:
                # 获取今日题目
                print('获取今日题目')
                self.get_question()
        else:
            print(return_data['message'])

    # 获取题目
    def get_question(self):
        url = f'https://m3.dmsp.ccb.com/api/businessCenter/zhcUserDayAnswer/queryQuestionToday?zhc_token={self.zhc_token}'
        return_data = self.send_request(url, headers = self.base_header)
        self.sleep()
        if return_data['code'] != 200:
            print(return_data['message'])
        else:
            question_id = return_data['data'].get('questionId')
            remark = return_data['data'].get('remark')
            answer_list = return_data['data'].get('answerList')
            if remark:
                # 匹配答案
                print('开始匹配正确答案')
                pattern = r"[，。？！“”、]"
                remark_cleaned = re.sub(pattern, "", remark)

                max_match_count = 0
                right_answer_id = None
                for answer in answer_list:
                    answer_id = answer["id"]
                    answer_result = answer["answerResult"]
                    answer_cleaned = re.sub(pattern, "", answer_result)

                    match_count = 0
                    for word in answer_cleaned:
                        if word in remark_cleaned:
                            match_count += 1
                            remark_cleaned = remark_cleaned.replace(word, "", 1)

                    if match_count > max_match_count:
                        max_match_count = match_count
                        right_answer_id = answer_id
                if right_answer_id is not None:
                    print("匹配成功，开始答题")
                else:
                    print("匹配失败，随机答题")
                    right_answer_id = random.choice(answer_list)['id']
                self.answer(question_id, right_answer_id)
            else:
                print('暂无提示随机答题')
                right_answer_id = random.choice(answer_list)['id']
                self.answer(question_id, right_answer_id)

    # 答题
    def answer(self, question_id, answer_ids):
        url = f'https://m3.dmsp.ccb.com/api/businessCenter/zhcUserDayAnswer/userAnswerQuestion?zhc_token={self.zhc_token}'
        payload = {"questionId": question_id, "answerIds": answer_ids}
        return_data = self.send_request(url, headers = self.base_header, data = payload, method = 'POST')
        self.sleep()
        if return_data['code'] != 200:
            print(return_data['message'])
        else:
            print(return_data['message'])

    # ---------下面是精彩专区任务--------
    def get_csrftoken(self):
        refresh_url = 'https://event.ccbft.com/api/flow/nf/shortLink/redirect/ccb_gjb?CCB_Chnl=6000117'
        payload = '{{"shortId":"m13hviAVn3cy3PFWPRBB_w","archId":"ccb_gjb","ccbParamSJ":null,"channelId":"ccbLife","ifCcbLifeFirst":false,"ccbLifeUUID":"{}"}}'.format(
            self.ccb_uuid)

        headers = {
            'Host': 'fission-events.ccbft.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': app_ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'com.ccb.longjiLife',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'referer': 'https://event.ccbft.com/',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': self.zq_cookie
        }

        return_data = requests.post(refresh_url, headers = self.token_headers, data = payload).json()
        if return_data['code'] != 200:
            print(return_data['message'])

        else:
            redirect_url = return_data['data'].get('redirectUrl')
            requests.get(url = redirect_url, headers = headers)
            # 使用正则__dmsp_st的值
            match = re.search(r'__dmsp_st=([^&]+)', redirect_url)

            if match:
                dmsp_st_value = match.group(1)
                try:
                    url2 = f'https://fission-events.ccbft.com/a/224/1m0xM2mx?CCB_Chnl=6000117&__dmsp_st={dmsp_st_value}'
                    res = requests.get(url = url2, headers = headers)
                    data = res.text
                    csrf_token, authorization = self.extract_csrf_and_auth(data)

                    if csrf_token and authorization:
                        self.zq_headers['x-csrf-token'] = csrf_token
                        self.zq_headers['authorization'] = f'Bearer {authorization}'
                        self.sleep()

                        print('\n----代发专区----')
                        # self.game_id()
                        print('\n----养老专区----')
                        self.turn()
                        print('\n----跨境专区----')
                        self.border_draw()
                        print('\n----商户专区----')
                        self.shoplist()
                        print('\n----消保专区----\n---登山游戏----')
                        self.fire()
                        print('\n---抓娃娃游戏----')
                        self.get_doll()
                        print('\n---投篮球游戏----')
                        self.do_basket()
                        print('\n---开盲盒----')
                        self.open_box()
                    else:
                        print('CSRF token or Authorization not found.')
                except requests.RequestException as e:
                    print(f"请求异常: {e}")

    def extract_csrf_and_auth(self, data):
        csrf_token_pattern = r'<meta\s+name=csrf-token\s+content="([^"]+)">'
        authorization_pattern = r'<meta\s+name=Authorization\s+content="([^"]+)">'
        csrf_token_match = re.search(csrf_token_pattern, data)
        authorization_match = re.search(authorization_pattern, data)
        if csrf_token_match and authorization_match:
            return csrf_token_match.group(1), authorization_match.group(1)

        return None, None

    # 养老专区新
    def turn(self):
        tasklist_url = 'https://fission-events.ccbft.com/activity/dmspmileage/getindexdata/224/5P87Md3y'
        go_url = 'https://fission-events.ccbft.com/activity/dmspmileage/go/224/5P87Md3y'

        tasks_data = self.send_request(tasklist_url, headers = self.zq_headers)

        if not tasks_data or tasks_data['status'] != 'success':
            print(tasks_data['message'])
        else:
            task_list = tasks_data.get('data', {}).get('acttask', {}).get('limit_time')
            user_map_ident = tasks_data.get('data', {}).get('user_map_ident', '')

            print(f'当前是第 {user_map_ident} 张地图')

            rewards = tasks_data.get('data', {}).get('map', {}).get('config', {}).get('node')
            self.process_rewards(rewards)

            self.process_tasks(task_list)

            self.sleep()

            query_data = self.send_request(tasklist_url, headers = self.zq_headers)

            surplus = query_data.get('data', {}).get('mileage', {}).get('surplus')
            if surplus != '0':
                go_data = self.send_request(go_url, headers = self.zq_headers, method = 'POST')
                if go_data:
                    mileage_go = go_data.get('data', {}).get('mileage_go', '')
                    user_node = go_data.get('data', {}).get('user_node_value')
                    print(f'前进: {mileage_go}里程， 当前: {user_node}里程')
                    query_data2 = self.send_request(tasklist_url, headers = self.zq_headers)
                    rewards = query_data2.get('data', {}).get('map', {}).get('config', {}).get('node')
                    self.process_rewards(rewards)

    def process_rewards(self, rewards):
        for reward in rewards:
            value = reward.get('value')
            state = reward.get('state')
            if value == 0 or state != 3:
                continue
            elif value == 5000 and state == 4:
                replace_url = 'https://fission-events.ccbft.com/activity/dmspmileage/togglesmap/224/5P87Md3y'
                replace_data = self.send_request(replace_url, headers = self.zq_headers, method = 'POST')
                if replace_data and replace_data['status'] == 'success':
                    print('更换地图成功')
                    self.sleep()
            else:
                getreward_url = 'https://fission-events.ccbft.com/activity/dmspmileage/draw/224/5P87Md3y'
                reward_payload = {"value": value}
                rewrd_data = self.send_request(getreward_url, headers = self.zq_headers, data = reward_payload,
                                               method = 'POST')
                if rewrd_data['status'] != 'success':
                    return print(rewrd_data['message'])
                prizename = rewrd_data.get('data', {}).get('prizename')
                print(f'领取 {value}里程奖励: {prizename}')
                if value == 5000:
                    replace_url = 'https://fission-events.ccbft.com/activity/dmspmileage/togglesmap/224/5P87Md3y'
                    replace_data = self.send_request(replace_url, headers = self.zq_headers, method = 'POST')
                    if replace_data and replace_data['status'] == 'success':
                        print('更换地图成功')
                        self.sleep()
                time.sleep(3)

    def process_tasks(self, task_list):
        for task in task_list:
            ident = task.get('ident')
            title = task.get('title')
            state = task.get('state')
            reward = task.get('reward')
            if state == 1:
                print(f'--已完成: {title}')
            else:
                print(f'---去完成: {title}')
                dotask_url = 'https://fission-events.ccbft.com/activity/dmspmileage/taskgo/224/5P87Md3y'
                do_payload = {"type": "limit_time", "ident": ident}
                do_data = self.send_request(dotask_url, headers = self.zq_headers, data = do_payload, method = 'POST')
                if do_data and do_data['status'] == 'success':
                    print(f'--浏览成功获得: {reward} 里程')
                time.sleep(3)

    # 跨境专区新
    def border_draw(self):
        query_url = 'https://fission-events.ccbft.com/Component/draw/getUserExtInfo/224/1m0xM2mx'
        draw_url = 'https://fission-events.ccbft.com/Component/draw/commonDrawPrize/224/1m0xM2mx'

        query_data = self.send_request(query_url, headers = self.zq_headers)
        if query_data['status'] != 'success':
            print(query_data['message'])
        else:
            remain = query_data['data'].get('remain_num')
            if remain == '0':
                return print('--当前剩余抽奖次数为0')
            self.sleep()
            draw_data = self.send_request(draw_url, headers = self.zq_headers, method = 'POST')
            if draw_data['status'] != 'success':
                print(draw_data['message'])
            else:
                print(f"--{draw_data['message']}---{draw_data['data'].get('prizename')}")

    # 商户专区新
    def shoplist(self):
        task_url = 'https://fission-events.ccbft.com/Component/task/lists/224/8ZWXBM3w'
        tasks_data = self.send_request(task_url, headers = self.zq_headers)
        self.sleep()
        if tasks_data['status'] != 'success':
            print(tasks_data['message'])
        else:
            task_list = tasks_data['data'].get('userTask')
            for value in task_list:
                complete_status = value['finish']
                if complete_status == 1:
                    print('--已完成该任务，继续浏览下一个任务')
                    continue
                task_id = value['id']
                do_url = 'https://fission-events.ccbft.com/Component/task/do/224/8ZWXBM3w'
                payload = {"id": task_id}
                do_data = self.send_request(do_url, headers = self.zq_headers, data = payload, method = 'POST')
                if do_data['status'] != 'success':
                    print(do_data['message'])
                    continue
                print('--浏览完成')
                time.sleep(3)
            print('--已完成全部任务，去掷骰子')
            time.sleep(3)
            self.throw()

    def throw(self):
        query_url = 'https://fission-events.ccbft.com/activity/dmspshzq/getIndex/224/8ZWXBM3w'
        query_data = self.send_request(query_url, headers = self.zq_headers)
        if query_data['status'] != 'success':
            print(query_data['message'])
        else:
            remain_num = query_data['data'].get('remain_num')
            if remain_num == '0':
                return print('当前没有骰子了')
            self.sleep()
            num = int(remain_num)
            draw_url = 'https://fission-events.ccbft.com/activity/dmspshzq/drawPrize/224/8ZWXBM3w'
            payload = {}
            prizes = []
            for _ in range(num):
                draw_data = self.send_request(draw_url, headers = self.zq_headers, data = payload, method = 'POST')
                if draw_data['status'] != 'success':
                    print(draw_data['message'])
                    continue
                add_step = draw_data['data'].get('add_step')
                current_step = draw_data['data'].get('current_step')
                prize_name = draw_data['data'].get('prize_name')
                prizes.append(f"前进步数:{add_step},当前步数:{current_step}\n获得奖励:{prize_name}")
                time.sleep(3)

            if prizes:
                print('\n'.join(prizes))

    # 消保专区新
    def fire(self):
        num_url = 'https://fission-events.ccbft.com/activity/dmspxbmountain/getUserInfo/224/jmXN4Q3d'
        num_data = self.send_request(num_url, headers = self.zq_headers)
        self.sleep()
        if num_data.get('status') != 'success':
            print(num_data.get('message'))
        else:
            remain_num = num_data['data'].get('remain_num', 0)
            num = int(remain_num)
            if num == 0:
                print('当前剩余游戏次数为0')
                return
            id_url = 'https://fission-events.ccbft.com/activity/dmspxbmountain/startChallenge/224/jmXN4Q3d'
            draw_url = 'https://fission-events.ccbft.com/Component/draw/commonDrawPrize/224/jmXN4Q3d'
            payload = {}
            for _ in range(num):
                id_data = self.send_request(id_url, headers = self.zq_headers, data = payload, method = 'POST')
                if id_data.get('status') != 'success':
                    print(id_data.get('message'))
                    continue
                game_id = id_data.get('data')
                print('获取成功，开始登山游戏')
                time.sleep(20)
                game_url = 'https://fission-events.ccbft.com/activity/dmspxbmountain/doChallenge/224/jmXN4Q3d'
                payload_game = {"l_id": game_id, "stage": 13, "score": 200}
                msg_data = self.send_request(game_url, headers = self.zq_headers, data = payload_game,
                                             method = 'POST')
                if msg_data.get('status') != 'success':
                    print(msg_data.get('message'))
                else:
                    draw_payload = {}
                    draw_data = self.send_request(draw_url, headers = self.zq_headers, data = draw_payload,
                                                  method = 'POST')
                    if draw_data.get('status') != 'success':
                        print(draw_data.get('message'))
                    else:
                        mes = draw_data.get('message')
                        prizename = draw_data.get('data', {}).get('prizename', '')
                        print(f'{mes}  {prizename}')
                        time.sleep(5)

    # 抓娃娃
    def get_doll(self):
        if doll_flag == 0:
            print('已关闭抓娃娃游戏')
            return
        query_url = 'https://fission-events.ccbft.com/Component/draw/getUserCCB/224/xPOLkama'
        draw_url = 'https://fission-events.ccbft.com/Component/draw/dmspCommonCcbDrawPrize/224/xPOLkama'

        query_data = self.send_request(query_url, headers = self.zq_headers)
        draw_num = query_data.get('data', {}).get('user_day_draw_num', 0)
        num = 10 - int(draw_num)
        num2 = 10 - doll_draw
        print(f'--当前剩余游戏次数: {num}')

        while num > num2:
            draw_payload = {}
            draw_data = self.send_request(draw_url, headers = self.zq_headers, data = draw_payload, method = 'POST')
            if draw_data.get('status') != 'success':
                print(draw_data.get('message'))
                continue
            msg = draw_data.get('message')
            prizename = draw_data.get('data', {}).get('prizename', '')
            print(f'{msg}  {prizename}')
            time.sleep(5)
            num -= 1

    # 投篮球
    def do_basket(self):
        if basket_flag == 0:
            print('已关闭投篮球游戏')
            return
        index_url = 'https://fission-events.ccbft.com/a/224/eZgpye3y/index?CCB_Chnl=1000181'
        query_url = 'https://fission-events.ccbft.com/activity/dmspdunk/user/224/eZgpye3y'
        requests.get(url = index_url, headers = self.zq_headers)
        query_data = self.send_request(query_url, headers = self.zq_headers)
        remain_daily = query_data.get('data', {}).get('remain_daily_times')
        num = 5 - basket_draw
        print(f'--当前剩余游戏次数: {remain_daily}')
        self.sleep()

        while remain_daily > num:
            id_url = 'https://fission-events.ccbft.com/activity/dmspdunk/start/224/eZgpye3y'
            id_data = self.send_request(id_url, headers = self.zq_headers, method = 'POST')

            if id_data.get('status') != 'success':
                print(id_data.get('message'))
                continue
            game_id = id_data.get('data', {}).get('id')
            time.sleep(5)
            activity_url = f'https://fission-events.ccbft.com/activity/dmspdunk/scene/224/eZgpye3y?id={game_id}'
            activity_data = self.send_request(activity_url, headers = self.zq_headers)
            remain_times = activity_data.get('data', {}).get('remain_times')
            basket_num = int(remain_times)  # 篮球数量
            while basket_num > 0:
                dogame_url = 'https://fission-events.ccbft.com/activity/dmspdunk/shot/224/eZgpye3y'
                payload = {'id': game_id}
                dogeme_data = self.send_request(dogame_url, headers = self.zq_headers, data = payload, method = 'POST')
                if dogeme_data.get('status') != 'success':
                    print(dogeme_data.get('message'))
                    continue
                win_times = dogeme_data.get('data', {}).get('win_times')  # 投中数量
                got_ccb = dogeme_data.get('data', {}).get('got_ccb')  # 获得cc豆
                print(f'当前投中篮球数量: {win_times}')

                if basket_num == 1:
                    print(f'游戏结束,获得cc豆数量: {got_ccb}')
                time.sleep(2.5)
                basket_num -= 1
            remain_daily -= 1

    # 开盲盒
    def open_box(self):
        if box_flag == 0:
            print('已关闭开盲盒')
            return

        type_url = 'https://fission-events.ccbft.com/activity/dmspblindbox/index/224/xZ4JKaPl'
        type_data = self.send_request(type_url, headers = self.zq_headers)
        self.sleep()

        types = type_data.get('data', [])

        for value in types:
            pot_id = value['pot_id']
            pot_name = value['pot_name']
            draw_one_ccb = value['draw_one_ccb']

            if box_id == pot_id:
                print(f'当前盲盒种类: [{pot_name}], 需消耗: {draw_one_ccb}cc豆')
                self.process_opening(pot_id)
                break
        else:
            print("未找到对应盲盒种类")

    def process_opening(self, box_id):
        num_url = 'https://fission-events.ccbft.com/Component/draw/getUserCCB/224/xZ4JKaPl'
        num_data = self.send_request(num_url, headers = self.zq_headers)
        self.sleep()

        draw_num = num_data.get('data', {}).get('draw_day_max_num', '')
        user_num = num_data.get('data', {}).get('user_day_draw_num', '')

        surplus_num = draw_num - int(user_num)
        num = draw_num - box_draw

        print(f'--当前开盲盒次数: {surplus_num}')

        while surplus_num > num:
            open_url = 'https://fission-events.ccbft.com/activity/dmspblindbox/draw/224/xZ4JKaPl'
            open_data = self.send_request(open_url, headers = self.zq_headers, data = {"pot_id": box_id},
                                          method = 'POST')

            if open_data['status'] != 'success':
                print(open_data['message'])
                return

            prizename = open_data.get('data', {}).get('prizename', '')
            print(f'开盲盒获得: {prizename}')
            time.sleep(3)
            surplus_num -= 1

    # 查询cc豆及过期cc豆时间
    def get_user_ccd(self):
        url_get_ccd = f'https://m3.dmsp.ccb.com/api/businessCenter/user/getUserCCD?zhc_token={self.zhc_token}'
        url_get_expired_ccd = f'https://m3.dmsp.ccb.com/api/businessCenter/user/getUserCCDExpired?zhc_token={self.zhc_token}'

        try:
            return_data1 = self.send_request(url_get_ccd, headers = self.base_header, data = {},
                                             method = 'POST')
            self.sleep()
            return_data2 = self.send_request(url_get_expired_ccd, headers = self.base_header,
                                             data = {}, method = 'POST')
            if return_data1['code'] != 200:
                raise Exception(return_data1['message'])
            elif return_data2['code'] != 200:
                raise Exception(return_data2['message'])
            count1 = return_data1['data'].get('userCCBeanInfo').get('count')
            count2 = return_data2['data'].get('userCCBeanExpiredInfo').get('count')
            expire_date_str = return_data2['data'].get('userCCBeanExpiredInfo').get('expireDate')
            if expire_date_str:
                expire_date = datetime.fromisoformat(expire_date_str)
                formatted_date = expire_date.strftime('%Y-%m-%d %H:%M:%S')
                print(f'\n当前cc豆:{count1}，有{count2} cc豆将于{formatted_date}过期')
            else:
                print("expire_date_str is empty")

        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    cookies = user_cookie.split("@")
    msg = f"建行cc豆共获取到{len(cookies)}个账号"
    print(msg)

    for i, cookie in enumerate(cookies, start = 1):
        print(f"\n======== ▷ 第 {i} 个账号 ◁ ========")
        CCD(cookie).get_session()
        print("\n随机等待5-10s进行下一个账号")
        time.sleep(random.randint(5, 10))
