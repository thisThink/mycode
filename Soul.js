// !author = 怎么肥事   2025/5/4
let body = $response.body;

try {
    let obj = JSON.parse(body);
    let imageUrl = obj?.data?.url;

    if (imageUrl && typeof imageUrl === 'string') {
        console.log("图片地址: " + imageUrl);

        $notify("图片预览", "点击跳转浏览器", imageUrl, {
            "media-url": imageUrl,
            "open-url": imageUrl
        });
    }
} catch (e) {
    console.log("处理图片预览出错：" + e);
}

$done({ body });
