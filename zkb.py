import os,requests, re, json, urllib3

def handle(cookie):
    urllib3.disable_warnings()
    imfo_list =[]
    for i in range(len(cookie)):
        print('开始第'+ str(i+1) +'个帐号签到'+'\n'+'***********************')
        f_url = 'https://v1.xianbao.net/' 
        url = 'https://v1.xianbao.net/app.php?p=sign&action=todaysign'
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1',
            'cookie': f'{cookie[i]}',
            'Host': 'v1.xianbao.net',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://v1.xianbao.net'
        }
        f_html = requests.post(url=f_url, headers=headers, verify=False,allow_redirects=False).text
        formhash = str(re.findall('name="formhash" value="(.*?)" />', f_html, re.S)).replace('[', '').replace('\'', '').replace(']', '')
        data = {
        'formhash': f'{formhash}'
        }
        html = requests.post(url=url, headers=headers, data=data, verify=False).text
        result = re.findall('<div id="messagetext" class="alert.*">\n<p>(.*?)<script type="text/javascript" reload="1">', html, re.S)
        message = "".join(result)
        url_2 = 'https://v1.xianbao.net/home.php?mod=spacecp&ac=credit&showcredit=1'
        html_2 = requests.get(url=url_2, headers=headers, verify=False).text
        info = '用户名：' + "".join(re.findall('title="访问我的空间">(.*?)</a>', html_2, re.S))
        guoguo = '果果:' + "".join(re.findall('src="/static/images/common/guoguo.gif" /> 果果: </em>(.*?)&nbsp; <a href="home.php?', html_2, re.S))
        sign_info = info + ' ' + guoguo + ' 签到结果:【' + message + '】'
        imfo_list.append(sign_info)
    imfo_message = str(imfo_list).replace("\', \'","\n").replace("[\'","").replace("\']","")
    return imfo_message

if __name__ ==  "__main__":
    cookie = os.environ.get('XZKB_COOKIE')
    cookie_list = cookie.split('#')
    print(handle(cookie_list))