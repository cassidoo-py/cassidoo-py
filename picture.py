# encoding:utf-8
import requests
import re
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
for i in range(1, 20):
    url = 'https://www.xxxx.com/guoneimeinv/list_5_{}.html'.format(i)
    response = requests.get(url, headers=headers)
    # print(response.content.decode('gbk'))
    # 提取想要的数据信息
    data_list = re.findall('</a> </li><li><a href="(.*?)" class="pic" target="_Blank" alt="(.*?)">', response.content.decode('gbk'))
    # print(data_list)
    num = 0
    for info_url, title in data_list:
        # print(info_url)
         # print(title)
        res = requests.get(info_url, headers=headers).content.decode('gbk')
        # print(res)
        page_num = re.findall('<li><a>共(.*?)页: </a></li><li>', res)
        # print(page_num)
        for i in range(1, int(page_num[0]) + 1):
            if i == 1:
                new_url = info_url
            else:
                new_url = info_url.replace('.html', f'_{i}.html')
            # print(new_url)
            jpg_data = requests.get(new_url, headers=headers).content.decode('gbk')
            # print(jpg_data)
            jpg_url_list = re.findall('<p align="center"><img src="(.*?)" /></p><br/>', jpg_data)
            # print(jpg_url_list)
            for jgp_url in jpg_url_list:
                result = requests.get(jgp_url, headers=headers).content
                f = open('图库/' + title + "-" + str(num) + ".jpg", 'wb')
                f.write(result)
                num += 1
                print(f"正在下载{title}第{num}张")