# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 17:54
# @Author  : ziyou
# -------------------------------
# 参考了 一风一燕 的原脚本进行修改
# cron "32 10,13,15 * * *" script-path=xxx.py,tag=匹配cron用
# const $ = new Env('滴滴')
# 抓包获取 didi_jifen_token
# 手机抓包后，在手机点击，福利中心的明细，查看一次福利金明细后，搜索token=，token=xxxx&city，xxx便是 didi_jifen_token。
# 或者查看一次福利金明细后，查看URL，
# https://rewards.xiaojukeji.com/loyalty_credit/bonus/getWelfareUsage4Wallet?，后面的token=xxxx&city，xxx便是 didi_jifen_token。
# 主要功能：自动领取我的权益、福利金签到、瓜分福利金、领取完单返福利金...
# 滴滴
# export didi_jifen_token='9Op**__w==&9Op**__w==',多账号使用换行或&
# 青龙拉取命令 ql raw https://raw.githubusercontent.com/q7q7q7q7q7q7q7/ziyou/main/%E6%BB%B4%E6%BB%B4.py

import datetime
import os
import sys
import time
import requests

DIDI_JIFEN_TOKEN = []

didi_jifen_token = os.getenv("didi_jifen_token")
if didi_jifen_token:
    DIDI_JIFEN_TOKEN = didi_jifen_token.replace("&", "\n").split("\n")


class DiDi:
    LAT = '28.20055'  # 纬度
    LNG = '113.01907'  # 经度
    CITY_ID = 24  # 城市id

    def __init__(self, token, city_id=CITY_ID, lat=LAT, lng=LNG):
        self.token = token
        self.city_id = city_id
        self.lat = lat
        self.lng = lng
        self.today = datetime.datetime.now().strftime('%Y-%m-%d')  # 今天时间 例如：'2023-07-12'
        # 明天时间 例如：'2023-07-13'
        self.tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        self.activity_id_today = 0  # 今天的瓜分福利金的活动id 用于完成今天的瓜分福利金 需在14点之前
        self.task_id_today = 0  # 完成今天的瓜分福利金的任务id 用于完成今天的瓜分福利金 需在14点之前
        self.status_today = 0  # 显示今天的瓜分活动状态 1为待报名 2为已参加 3为已完成待发奖 4为已发奖 5为未参加
        self.activity_id_tomorrow = 0  # 明天瓜分福利金的活动id 用于报名明天的瓜分福利金
        self.status_tomorrow = 0  # 显示今天的瓜分活动状态 1为待报名 2为已参加 3为已完成待发奖 4为已发奖 5为未参加
        self.count_tomorrow = 0

    # 签到
    def check_in(self):
        url = f'https://ut.xiaojukeji.com/ut/welfare/api/action/dailySign'
        _json = {"token": self.token,
                 "lat": self.lat,
                 "lng": self.lng,
                 "platform": "na",
                 "env": '{}'}
        response = requests.post(url=url, json=_json)
        response_dict = response.json()
        # print(response_dict)
        if response_dict.get('errno') == 0:
            subsidy_amount = response_dict['data']['subsidy_state']['subsidy_amount']
            print(f"今日签到成功，获得{subsidy_amount}福利金")
            return
        if response_dict.get('errno') == 40009:
            print("今日福利金已签到，无需重复签到!")
            return
        print(f'福利金签到出错！ {response_dict}')

    # 获取瓜分活动ID
    def get_carve_up_action_id(self):
        url = f'https://ut.xiaojukeji.com/ut/welfare/api/home/init/v2'
        _json = {"token": self.token,
                 "lat": self.lat,
                 "lng": self.lng,
                 "platform": "na",
                 "env": '{}'}
        response = requests.post(url=url, json=_json)
        response_dict = response.json()
        # print(response_dict)
        divide_data = response_dict['data']['divide_data']['divide']

        today_data = divide_data[self.today]
        # print(today_data)
        self.activity_id_today, self.task_id_today, self.status_today = today_data['activity_id'], today_data[
            'task_id'], today_data['status']

        tomorrow_data = divide_data[self.tomorrow]
        # print(tomorrow_data)
        self.activity_id_tomorrow, self.status_tomorrow, self.count_tomorrow = tomorrow_data['activity_id'], \
            tomorrow_data['status'], tomorrow_data['button']['count']
        return True

    # 报名明天的瓜分福利金
    def apply_carve_up_action(self):
        url = f'https://ut.xiaojukeji.com/ut/welfare/api/action/joinDivide'
        _json = {"token": self.token,
                 "lat": self.lat,
                 "lng": self.lng,
                 "platform": "na",
                 "env": '{}',
                 "activity_id": self.activity_id_tomorrow,
                 "count": self.count_tomorrow,
                 "type": "ut_bonus"}
        response = requests.post(url=url, json=_json)
        response_dict = response.json()
        # print(response_dict)
        if response_dict.get("errno") == 0:
            if response_dict.get("data", {}).get("result") is True:
                print("报名今日打卡瓜分活动成功！")
                return
        print(f'报名今日打卡瓜分活动失败！ {response_dict}')

    # 完成今天的瓜分福利金 需在14点之前
    def complete_carve_up_action(self):
        url = f'https://ut.xiaojukeji.com/ut/welfare/api/action/divideReward'
        _json = {"token": self.token,
                 "lat": self.lat,
                 "lng": self.lng,
                 "platform": "na",
                 "env": '{}',
                 "activity_id": self.activity_id_today,
                 "task_id": self.task_id_today}
        response = requests.post(url=url, json=_json)
        response_dict = response.json()
        # print(response_dict)
        if response_dict.get("errno") == 0:
            if response_dict.get("data", {}).get("result") is True:
                print("完成今日打卡瓜分活动成功！")
                return
        print(f'完成今日打卡瓜分活动失败！ {response_dict}')

    # 查询当前福利金数量
    def get_info(self):
        url = "https://rewards.xiaojukeji.com/loyalty_credit/bonus/getWelfareUsage4Wallet"
        params = {"token": self.token, "city_id": self.city_id}
        response = requests.get(url=url, params=params)
        response_dict = response.json()
        # print(response_dict)
        balance = response_dict['data']['balance']
        return balance

    # 查询权益详情
    def inquire_benefits_details(self):
        url = "https://member.xiaojukeji.com/dmember/h5/privilegeLists"
        params = {"token": self.token, "city_id": self.city_id}
        time.sleep(0.5)
        response = requests.get(url=url, params=params)
        response_dict = response.json()
        # print(response_dict)
        privileges_list = response_dict.get('data', {}).get('privileges', [])  # 我的权益列表
        return privileges_list

    # 领取 周周领券 活动的优惠券
    def receive_level_gift(self):
        privileges_list = self.inquire_benefits_details()
        for privileges in privileges_list:
            if privileges.get('name') == '周周领券':
                coupons_list = privileges.get('level_gift', {}).get('coupons', [])
                for coupons in coupons_list:
                    status = coupons.get('status')  # 0为未领取，1为已使用，2为未使用
                    if status == 0:
                        batch_id = coupons.get('batch_id')
                        # print(batch_id)
                        print(f"开始领取 {coupons.get('remark')}{coupons.get('coupon_title')}")
                        url = f"https://member.xiaojukeji.com/dmember/h5/receiveLevelGift?xbiz=&prod_key=wyc-vip-level&xpsid=&dchn=&xoid=&xenv=passenger&xspm_from=&xpsid_root=&xpsid_from=&xpsid_share=&token={self.token}&batch_id={batch_id}&env={{}}&gift_type=1&city_id={self.city_id}"
                        time.sleep(0.5)
                        response = requests.get(url=url)
                        response_dict = response.json()
                        print(f'{response_dict}')
                        if response_dict.get('errno') == 0:
                            print('领取成功！')
                            continue
                        print(f'领取出错！ {response_dict}')
                return

    # 膨胀 周周领券 活动的优惠券
    def swell_coupon(self):
        privileges_list = self.inquire_benefits_details()  # 我的权益列表
        for privileges in privileges_list:
            if privileges.get('name') == '周周领券':
                coupons_list = privileges.get('level_gift', {}).get('coupons', [])
                for coupons in coupons_list:  # 膨胀
                    swell_status = coupons.get('swell_status')  # 0代表不能膨胀，1代表能膨胀,2代表已膨胀
                    # print(swell_status)
                    if swell_status == 1:
                        print(f"开始膨胀 {coupons.get('remark')}{coupons.get('coupon_title')}")
                        batch_id = coupons.get('batch_id')
                        coupon_id = coupons.get('coupon_id')
                        url = f'https://member.xiaojukeji.com/dmember/h5/swell_coupon?city_id={self.city_id}'
                        _json = {"token": self.token,
                                 "batch_id": batch_id,
                                 "coupon_id": coupon_id,
                                 "city_id": self.city_id}
                        time.sleep(0.5)
                        response = requests.post(url=url, json=_json)
                        response_dict = response.json()
                        print(response_dict)
                        if response_dict.get('error') == 0:
                            if response_dict.get('data', {}).get('is_swell') is True:
                                print('膨胀成功！')
                                continue
                            print('膨胀失败！')
                            continue
                        print(f'膨胀出错！ {response_dict}')
                return

    # 领取行程意外险
    def receive_travel_insurance(self):
        privileges_list = self.inquire_benefits_details()  # 我的权益列表
        for privileges in privileges_list:
            if privileges.get('name') == '行程意外险':
                # print(privileges)
                need_received = privileges.get('need_received')
                if need_received == 1:  # 0为未领取，1为已领取
                    print('已领取了！')
                    return
                if need_received == 0:  # 0为未领取，1为已领取
                    url = 'https://member.xiaojukeji.com/dmember/h5/bindPrivilege'
                    _json = {"token": self.token, "type": 3}
                    time.sleep(0.5)
                    response = requests.post(url=url, json=_json)
                    response_dict = response.json()
                    # print(response_dict)
                    if response_dict.get('errno') == 0:
                        print('领取成功！')
                        return
                    print(f'领取出错！ {response_dict}')
                    return
                print(f'出现未知情况！ {need_received =} {privileges}')
                return

    # 领取周三折上折权益
    def receive_memberday_discount_multi(self):
        privileges_list = self.inquire_benefits_details()  # 我的权益列表
        for privileges in privileges_list:
            if privileges.get('name') == '周三折上折':
                # print(privileges)
                need_received = privileges.get('need_received')
                if need_received == 1:  # 0为未领取，1为已领取
                    print('已领取了！')
                    return
                if need_received == 0:  # 0为未领取，1为已领取
                    url = 'https://member.xiaojukeji.com/dmember/h5/receiveMemberDayDiscount'
                    _json = {"token": self.token, "privilege_type": 1}
                    time.sleep(0.5)
                    response = requests.post(url=url, json=_json)
                    response_dict = response.json()
                    # print(response_dict)
                    if response_dict.get('errno') == 0:
                        print('领取成功！')
                        return
                    print(f'领取出错！ {response_dict}')
                    return
                print(f'出现未知情况！ {need_received =} {privileges}')
                return

    # 领取 气泡奖励 完单返福利金
    def receive_wyc_order_finish(self):
        url = 'https://ut.xiaojukeji.com/ut/welfare/api/home/getBubble'
        _json = {"token": self.token,
                 "lat": self.lat,
                 "lng": self.lng,
                 "platform": "na",
                 "env": "{}"}
        # time.sleep(0.5)
        response = requests.post(url=url, json=_json)
        response_dict = response.json()
        # print(response_dict)
        bubble_list = response_dict.get('data', {}).get('bubble_list', [])
        # print(bubble_list)
        for bubble in bubble_list:
            if bubble.get('pre_content') == '完单返':
                # print(bubble)
                cycle_id = bubble.get('cycle_id')
                reward_count = bubble.get('reward_count')
                url = 'https://ut.xiaojukeji.com/ut/welfare/api/action/clickBubble'
                _json = {"token": self.token,
                         "lat": self.lat,
                         "lng": self.lng,
                         "platform": "na",
                         "env": "{}",
                         "cycle_id": cycle_id, "bubble_type": "wyc_order_finish"}
                time.sleep(0.5)
                response = requests.post(url=url, json=_json)
                response_dict = response.json()
                # print(response_dict)
                if response_dict.get('errno') == 0:
                    print(f'领取成功，获得{reward_count}福利金！')
                    return
                print(f'领取出错！ {response_dict}')
                return

    def main(self):
        character = '★★'
        print(f'{character}当前福利金数量为：{self.get_info()}')
        print(f'{character}开始进行福利金签到！')
        self.check_in()
        if self.get_carve_up_action_id():
            print(f'{character}开始完成今日瓜分活动！')
            if self.status_today == 2:  # 1为待报名，2为待完成，3为已完成，4为已领取
                self.complete_carve_up_action()  # 完成瓜分福利金 需在14点之前
            elif self.status_today == 3:
                print('今天已完成瓜分活动！')
            elif self.status_today == 4:
                print('今天已领取瓜分活动奖励！')
            else:
                print('完成失败，可能昨日未报名！')
            print(f'{character}开始报名明日瓜分活动！')
            if self.status_tomorrow == 1:  # 1为待报名，2为待完成，3为已完成，4为已领取
                self.apply_carve_up_action()  # 报名瓜分福利金
            elif self.status_tomorrow == 2:
                print('今天已经报名参加瓜分明天的福利金了！')
            else:
                print('报名参加瓜分明天的福利金出现未知错误！')
        print(f'{character}开始领取 周周领券 活动的优惠券')
        self.receive_level_gift()
        print(f'{character}开始膨胀 周周领券 活动的优惠券')
        self.swell_coupon()
        print(f'{character}开始领取行程意外险')
        self.receive_travel_insurance()
        print(f'{character}开始领取周三折上折权益')
        self.receive_memberday_discount_multi()
        print(f'{character}开始领取气泡奖励')
        self.receive_wyc_order_finish()
        print(f'{character}当前福利金数量为：{self.get_info()}')


# 主程序
def main(ck_list):
    if not ck_list:
        print('没有获取到账号！')
        return
    print(f'获取到{len(ck_list)}个账号！')
    for index, ck in enumerate(ck_list):
        print(f'*****第{index + 1}个账号*****')
        DiDi(ck).main()
        print('')


if __name__ == '__main__':
    main(DIDI_JIFEN_TOKEN)
    sys.exit()
