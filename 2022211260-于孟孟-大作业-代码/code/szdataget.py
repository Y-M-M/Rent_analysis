import requests
import time
from lxml import etree
import csv
import re

def get_house_info(url):
    print(url)

    # 构造headers，添加自己的User-Agent和Cookie
    headers_chome = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Cookie' : 'lianjia_uuid=50628585-2297-4358-9549-6c4b78d9e44d; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1733958870; HMACCOUNT=1CE163A05FC161EA; _ga=GA1.2.2089045333.1733958870; ftkrc_=ed7d9328-a59e-44b3-a976-3f9943472c04; lfrc_=09b6fba4-07fd-4f29-9a20-05a01876a4a7; _ga_RCTBRFLNVS=GS1.2.1734531870.6.1.1734531879.0.0.0; _jzqc=1; _gid=GA1.2.1835376939.1735016686; login_ucid=2000000458627825; lianjia_token=2.0014d3cb4c4326bc51057ee27ddbae709c; lianjia_token_secure=2.0014d3cb4c4326bc51057ee27ddbae709c; security_ticket=WSLxiRzsm8L4tqFRapj1P5bTJKZ0kPAlsPF0ZQundkMvauiQlT1pB2tft/W+q+8zhqfGFXy6p8u+jufRzlvqQUxdbeTGpclfnRDd+QfoQgkgxi0SEOGRWMY8rGGlXaJFDCIC5yqFknOBWfBbYIStSi4GXvvnriTGfG1dOvqlFzA=; _jzqy=1.1735016842.1735016842.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6.-; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22193f70d744de30-05807c7e55cc8d-1e525636-1296000-193f70d744e2e88%22%2C%22%24device_id%22%3A%22193f70d744de30-05807c7e55cc8d-1e525636-1296000-193f70d744e2e88%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E9%93%BE%E5%AE%B6%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wybj%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; _ga_KJTRWRHDL1=GS1.2.1735016687.1.1.1735016934.0.0.0; _ga_QJN1VP0CMS=GS1.2.1735016687.1.1.1735016934.0.0.0; beikeBaseData=%7B%22parentSceneId%22:%222079002982467028737%22%7D; lianjia_ssid=d9bc98dd-54ee-47ae-85b5-a8daaef0638d; _jzqa=1.2391447098640810000.1735016674.1735016674.1735082029.2; _jzqx=1.1735082029.1735082029.1.jzqsr=sh%2Elianjia%2Ecom|jzqct=/.-; _ga_LRLL77SF11=GS1.2.1735082041.2.1.1735082168.0.0.0; _ga_GVYN2J1PCG=GS1.2.1735082041.2.1.1735082168.0.0.0; _ga_C4R21H79WC=GS1.2.1735082353.1.1.1735082357.0.0.0; _ga_WLZSQZX7DE=GS1.2.1735082256.2.1.1735082464.0.0.0; _ga_TJZVFLS7KV=GS1.2.1735082256.2.1.1735082464.0.0.0; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1735082468; _ga_654P0WDKYN=GS1.2.1735082274.1.1.1735082479.0.0.0; select_city=440300'
    }
    res = requests.get(url, headers=headers_chome)
    print(res.status_code)
    # print(url)
    # print(res.text)
    if res.status_code == 200:
        # print_res(res)
        with open('houses.html', 'w', encoding='utf-8') as file1:
            file1.write(res.text)
        html = etree.HTML(res.text)
        result = etree.tostring(html, encoding = 'utf-8')
        with open('string_house_html', 'w', encoding='utf-8') as file2:
            file2.write(result.decode('utf-8'))
        # 提取房屋名称
        # /html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div[1]/div/p[1]/a/text()
        housenames = html.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div/div/p[1]/a/text()')
        # print(housenames)
        n = len(housenames)
        # 提取与房屋名称等量的其他信息，构造house_list
        for i in range(1, n + 1):
            # //*[@id="content"]/div[1]/div[1]/div[11]/div/p[4]/span[1]
            all = html.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div[' + str(i) + ']/div/p[2]/text()')
            # print(all)
            area = html.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div[' + str(i) + ']/div/p[2]/text()[3]')
            category = html.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div[' + str(i) + ']/div/p[2]/text()[5]')

            price = html.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div[' + str(i) + ']/div/span/em/text()')
            a_house_info = []
            # print('housename: ', housenames[i - 1])
            # print('area:', area)
            # print('category', category)
            # print('price', price)
            
            nowname = str(housenames[i - 1].strip())
            a_house_info.append(nowname)

            begin = 0
            # 寻找area
            for j in range(0, len(all)):
                numbers = re.findall(r'\d+\.\d+|\d+', str(all[j]))
                numbers = list(map(float, numbers))
                if len(numbers) > 0 :
                    a_house_info.append(numbers[0])
                    begin = j
                    break
            if len(a_house_info) < 2:
                a_house_info.append(0)
            
            # print(all)
            # 寻找几居
            # 寻找几居
            for j in range(begin + 1, len(all)):
                # 使用正则表达式查找“室”前面的数字
                match = re.search(r'(\d+)\s*室', str(all[j]))
                if match:
                    a_house_info.append(int(match.group(1)))
                    break
            if len(a_house_info) < 3:
                a_house_info.append(0)

            start = nowname.find('·')
            if start != -1:
                # 从 '·' 的下一个字符开始提取
                start += 1
                # 找到第一个空格的位置
                end = nowname.find(' ', start)
                if end != -1:
                    # 返回 '·' 之后到第一个空格之前的子串
                    a_house_info.append(nowname[start:end])
                else:
                    a_house_info.append(nowname[begin:])
            else:
                a_house_info.append("")

            # 提取数字，如果是范围的话，就取上下限平均值
            if (len(price)):
                numbers = re.findall(r'\d+', str(price[0]))
                numbers = list(map(int, numbers))
                average = sum(numbers) // len(numbers)
                a_house_info.append(average)
            else:
                a_house_info.append(0)

            # 构造house_list
            house_list.append(a_house_info)

house_list = []

for i in range(1, 401):
    url = "https://sz.lianjia.com/zufang/pg" + str(i) + "/#contentList"
    get_house_info(url)
    if i % 50 == 0:
        time.sleep(100)
    time.sleep (5)

with open('../initaldata/szdata.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'area', 'category', 'section', 'price'])
    writer.writerows(house_list)