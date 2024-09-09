var request = require('request');
var options = {
   'method': 'GET',
   'url': 'http://app.ccgh.org.cn/api/service/verify.jsp?token=14F11F9DAFB91E6F3298A65519E7B390&service_id=1489&service_id=1489%20HTTP/1.1%20Host:%20app.ccgh.org.cn%20Connection:%20keep-alive%20Accept:%20application/json,%20text/plain,%20%2A/%2A%20User-Agent:%20Mozilla/5.0%20%28Linux;%20Android%2012;%20SM-G9730%20Build/SP1A.210812.016;%20wv%29%20AppleWebKit/537.36%20%28KHTML,%20like%20Gecko%29%20Version/4.0%20Chrome/124.0.6367.123%20Mobile%20Safari/537.36%20Origin:%20http://localhost%20X-Requested-With:%20cn.com.sinosoft%20Referer:%20http://localhost/%20Accept-Encoding:%20gzip,%20deflate%20Accept-Language:%20zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
   'headers': {
      'Host': ' app.ccgh.org.cn',
      'Connection': ' keep-alive',
      'Accept': ' application/json, text/plain, */*',
      'User-Agent': ' Mozilla/5.0 (Linux; Android 12; SM-G9730 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36',
      'Origin': ' http://localhost',
      'X-Requested-With': ' cn.com.sinosoft',
      'Referer': ' http://localhost/',
      'Accept-Language': ' zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
      'Cookie': 'JSESSIONID=0001-irSjxvwFHJ_vd6TEIvw83i:J8EBTV1MU'
   }
};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});