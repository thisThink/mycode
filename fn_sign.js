const axios = require('axios');
const cheerio = require('cheerio');

// 填写对应的 Cookie 值
const cookies = {
    'pvRK_2132_saltkey': 'jWG6x396',
    'pvRK_2132_auth': '7085KUTUfbd6ecNiaU3uQS0fyi74g9mrMKCKuIwLT3XUEjo29fLZULjf3R%2FD4ib8Zm8EFCQH767F8MTgEefRJVtmBA',
};

const cookieHeader = Object.entries(cookies).map(([key, value]) => `${key}=${value}`).join('; ');

async function signIn() {
    try {
    // 签到请求链接右键打卡按钮直接复制替换
        const response = await axios.get('https://club.fnnas.com/plugin.php?id=zqlj_sign&sign=c13901e2', {
            headers: {
                'Cookie': cookieHeader
            }
        });

        if (response.data.includes('恭喜您，打卡成功！')) {
            console.log('打卡成功');
            await getSignInInfo();
        } else if (response.data.includes('您今天已经打过卡了，请勿重复操作！')) {
            console.log('已经打过卡了');
        } else {
            console.log('打卡失败, cookies可能已经过期或站点更新.');
        }
    } catch (error) {
        console.error('签到请求失败:', error);
    }
}

async function getSignInInfo() {
    try {
        const response = await axios.get('https://club.fnnas.com/plugin.php?id=zqlj_sign', {
            headers: {
               'Cookie': cookieHeader
            }
        });

        const $ = cheerio.load(response.data);
        const content = [];

        const patterns = [
           { name: '最近打卡', selector: 'li:contains("最近打卡")' },
           { name: '本月打卡', selector: 'li:contains("本月打卡")' },
           { name: '连续打卡', selector: 'li:contains("连续打卡")' },
           { name: '累计打卡', selector: 'li:contains("累计打卡")' },
           { name: '累计奖励', selector: 'li:contains("累计奖励")' },
           { name: '最近奖励', selector: 'li:contains("最近奖励")' },
           { name: '当前打卡等级', selector: 'li:contains("当前打卡等级")' }
        ];

        patterns.forEach(pattern => {
          const element = $(pattern.selector).text();
          if (element) {
              content.push(`${pattern.name}: ${element.replace(/.*：/, '').trim()}`);
            }
        });

       console.log(content.join('\n'));

    } catch (error) {
       console.error('获取打卡信息失败:', error);
    }
}

signIn();
