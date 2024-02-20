"""
心喜查询库存  1.0


"""
import os
import requests
from datetime import datetime, timezone, timedelta
import json
import time
import io
import sys
import requests
import base64

import random  # 导入random模块以生成随机暂停时间
enable_notification = 1   #0不发送通知   1发送通知


# 只有在需要发送通知时才尝试导入notify模块
if enable_notification == 1:
    try:
        from notify import send
    except ModuleNotFoundError:
        print("警告：未找到notify.py模块。它不是一个依赖项，请勿错误安装。程序将退出。")
        sys.exit(1)

#---------简化的框架 0.4 带通知--------

jbxmmz = "心喜视频会员库存查询"
jbxmbb = "1.0"


# 获取北京日期的函数
def get_beijing_date():  
    beijing_time = datetime.now(timezone(timedelta(hours=8)))
    return beijing_time.date()

def dq_time():
    # 获取当前时间戳
    dqsj = int(time.time())

    # 将时间戳转换为可读的时间格式
    dysj = datetime.fromtimestamp(dqsj).strftime('%Y-%m-%d %H:%M:%S')
    #print("当前时间戳:", dqsj)
    #print("转换后的时间:", dysj)

    return dqsj, dysj

def log(message):
    print(message)

def print_disclaimer():
    log("📢 请认真阅读以下声明")
    log("      【免责声明】         ")
    log("✨ 脚本及其中涉及的任何解密分析程序，仅用于测试和学习研究")
    log("✨ 禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断")
    log("✨ 禁止任何公众号、自媒体进行任何形式的转载、发布")
    log("✨ 本人对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害")
    log("✨ 脚本文件请在下载试用后24小时内自行删除")
    log("✨ 脚本文件如有不慎被破解或修改由破解或修改者承担")
    log("✨ 如不接受此条款请立即删除脚本文件")
    log("" * 10)
    log("如果喜欢请打赏支持维护和开发    更要钱动力 来 更新/维护脚本")
    log("" * 10)
    log(f'这个是怎么东西？？？')
    log(f'U2FsdGVkX1/F371b27nTzUeMknDFjABXyQBHINWvVPRkUVoUe6ZdZ508DVGF7dMc')
    log("" * 10)
    log("" * 10)
    log(f'-----------{jbxmmz} {jbxmbb}-----------')



# 获取环境变量
def get_env_variable(var_name):
    value = os.getenv(var_name)
    if value is None:
        print(f'环境变量{var_name}未设置，请检查。')
        return None
    accounts = value.strip().split('\n')
    num_accounts = len(accounts)
    print(f'-----------本次账号运行数量：{num_accounts}-----------')
   
    print_disclaimer()
    return accounts


#-------------------------------封装请求-------------


def create_headers(sso):
    headers = {
        'Host': 'api.xinc818.com',
        'Connection': 'keep-alive',
        'sso': sso,
        'xweb_xhr': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819) XWEB/8531',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    return headers


#-------------------------------封装请求---完成----------


def sign_in(sso):

    base_url = "https://api.xinc818.com/mini/integralGoods/"
    headers = create_headers(sso)
    product_ids = [2140, 2143, 2142, 2138, 2135, 2132, 2234]
    for product_id in product_ids:
        url = f"{base_url}{product_id}?type="
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # 确保请求成功
            data = response.json()  # 解析JSON响应体
            if data['code'] == 0:
                #print(f"签到成功：商品ID {product_id}")
                item_id = data['data']['id']
                name = data['data']['name']
                stock = data['data']['stock']
                miniDisplayPrice = data['data']['miniDisplayPrice']
                #print(f"商品ID：{item_id}, 名称：{name}, 库存：{stock} 需要：{miniDisplayPrice}")
                print(f"{name}, 库存：{stock}  需要：{miniDisplayPrice}")
            else:
                print(f"请求失败，商品ID {product_id}，完整响应体：", data)
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP错误：{http_err}")
        except Exception as err:
            print(f"请求异常：{err}")
        
        # 随机暂停1到3秒
        time_to_sleep = random.uniform(1, 3)
        time.sleep(time_to_sleep)

#本地测试用 
os.environ['XSSO111NFkc'] = '''

'''



class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for file in self.files:
            file.write(obj)
            file.flush()

    def flush(self):
        for file in self.files:
            file.flush()

def main():
    var_name = 'XSSONFkc'
    tokens = get_env_variable(var_name)
    if not tokens:
        print(f'环境变量{var_name}未设置，请检查。')
        return

    captured_output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = Tee(sys.stdout, captured_output)

    total_accounts = len(tokens)

    for i, token in enumerate(tokens):
        parts = token.split('#')
        if len(parts) < 1:
            print("令牌格式不正确。跳过处理。")
            continue

        sso = parts[0]  
        account_no = parts[1] if len(parts) > 1 else ""  # 备注信息
        print(f'------账号 {i+1}/{total_accounts} {account_no} -------')

        sign_in(sso)  # 为每个用户执行签到操作，确保sign_in函数接受cookie参数

    sys.stdout = original_stdout
    output_content = captured_output.getvalue()
    captured_output.close()


    if enable_notification == 1:
        try:
            send("通知", output_content)  # 尝试发送通知
            print("通知已发送。输出内容为：")
            #print(output_content)
        except NameError:
            print("通知发送失败，send函数未定义。")



if __name__ == "__main__":
    main()     
