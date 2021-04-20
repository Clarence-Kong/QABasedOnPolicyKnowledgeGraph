# -*- coding: utf-8 -*-
# Author: Clarence Kong<clarencekong@qq.com,https://github.com/Clarence-Kong>
# @Time: 3/7/2021 11:03 PM
import time
import urllib.request
import urllib.parse
import urllib.parse
import json
import requests
from lxml import etree
import pymongo
import re

# mongoexport -h 127.0.0.1 -d policy -c test -o C:\Users\ckong\projects\QABasedOnPolicyKnowledgeGraph\data\policy.json
# mongoexport --db=policy --collection=test --out=policy.json

class MainData:
    def __init__(self):
        self.conn = pymongo.MongoClient()
        self.db = self.conn['policy']
        self.col = self.db['main']

        ''' 转义html '''

    def get_html(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.63 Safari/537.36'}
        req = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    ''' 根据task_id请求url '''

    def id_to_html(self, task_id):
        url = "http://www.gdzwfw.gov.cn/portal/guide/" + task_id
        html = self.get_html(url)
        selector = etree.HTML(html)
        return selector

    '''获取详细政务信息'''

    def get_matter_info(self, task_id):
        info = {}
        selector = self.id_to_html(task_id)
        info['matter_name'] = selector.xpath('//div[@class="matters-truncate title-name"]/text()')[0].strip()
        info['matter_short'] = selector.xpath('//th[contains(text(),"事项名称短语")]/following-sibling::td[1]/p/text()')[
            0].strip()
        info['matter_daily'] = selector.xpath('//th[contains(text(),"日常用语")]/following-sibling::td[1]/p/text()')[
            0].strip()
        info['matter_code'] = selector.xpath('//th[contains(text(),"业务办理项编码")]/following-sibling::td[1]/text()')[
            0].strip()
        info['matter_level'] = selector.xpath('//th[contains(text(),"行使层级")]/following-sibling::td[1]/p/text()')[
            0].strip()
        info['visit_number'] = selector.xpath('//th[contains(text(),"到办事现场次数")]/following-sibling::td[1]/p/text()')[
            0].strip()
        info['co_department'] = selector.xpath('//th[contains(text(),"联办机构")]/following-sibling::td[1]/p/text()')[
            0].strip()
        info['handle_location'] = selector.xpath('//h2[contains(text(),"窗口办理")]/following-sibling::div[1]/p[2]/text()')[
            0].strip()
        info['handle_time'] = selector.xpath('//h2[contains(text(),"窗口办理")]/following-sibling::div[1]/p[4]/text()')[
            0].strip()
        info['handle_time_limit'] = \
            selector.xpath('//h2[contains(text(),"窗口办理")]/following-sibling::div[1]/p[4]/text()')[0].strip()
        info['handle_type'] = selector.xpath('//th[contains(text(),"承诺办结时限")]/following-sibling::td[1]/p/text()')[
            0].strip().replace('\r', '').replace('\n', '').replace('\xa0', '').replace('   ',
                                                                                       '').replace(
            '\t', '')
        info['accept_standard'] = selector.xpath('//h3[contains(text(),"受理条件")]/following-sibling::p[1]/text()')[
            0].strip()
        info['consult_phone'] = selector.xpath('//p[contains(text(),"咨询电话")]/following-sibling::p[1]/text()')[0].strip()
        info['district'] = selector.xpath('//th[contains(text(),"行使层级")]/following-sibling::td[1]/p/text()')[
            0].strip()
        info['courier_service'] = selector.xpath('//th[contains(text(),"是否支持物流快递")]/following-sibling::td[1]/p/text()')[
            0].strip()
        info['bear_paltform'] = selector.xpath('//th[contains(text(),"业务系统")]/following-sibling::td[1]/p/text()')[
            0].strip()
        info['complain_phone'] = selector.xpath('//p[contains(text(),"投诉电话")]/following-sibling::p[1]/text()')[
            0].strip()
        # info['charge'] = selector.xpath('//h2[contains(text(),"收费项目信息")]/following-sibling::p[1]/text()')[0].strip()
        info['online_book'] = selector.xpath('//th[contains(text(),"是否网办")]/following-sibling::td[1]/text()')[0].strip()
        info['online_book_addr'] = selector.xpath("//th[contains(text(),'在线预约地址')]/following-sibling::td[1]//a/@href")[
            0]
        info['executer'] = selector.xpath('//th[contains(text(),"实施主体")]/following-sibling::td[1]/a/text()')[0].strip()
        info['theme_category'] = selector.xpath('//th[contains(text(),"面向自然人事项主题分类")]/following-sibling::td[1]/p/text()')[0].strip().split(',')
        info['service_object_name'] = selector.xpath('//th[contains(text(),"服务对象")]/following-sibling::td[1]/p/text()')[0].strip().split(',')

        # info['collect_resource_center'] = selector.xpath('')
        # info['service_content'] = selector.xpath('')
        # info['material_intro'] = selector.xpath('')
        # info['involved_mediation'] = selector.xpath('')
        # info['application_material'] = selector.xpath('')
        # info['online_payment'] = selector.xpath('')
        # info['certification_level_requirement'] = selector.xpath('')
        # info['setting_basis'] = selector.xpath('')
        # info['service_theme_name'] = selector.xpath('')
        # info['service_object_name'] = selector.xpath('')
        return info

    ''' 获取每条政务信息 '''

    def get_page_data(self):
        url = "http://www.gdzwfw.gov.cn/portal/item-solr/getCommonAuditItem"
        data_req = {
            "pageNum": 1,
            "pageSize": 10,
            "TASK_TYPE": '',
            "DEPT_CODE": '',
            "AREA_CODE": 442000,
            "ISLOCALLEVEL": 0,
            "KEY_WORD": '',
            "TYPE"'': '',
            "IS_ONLINE": '',
            "TASKTAG": 1,
            "LIMIT_SCENE_SUM": 0,
            "IS_ZERO_SECNE": '',
        }
        # 对要发送的数据进行打包
        postData = urllib.parse.urlencode(data_req).encode("utf-8")
        # 请求体
        req = urllib.request.Request(url, postData)
        # 发起请求
        req.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36")
        headers_req = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": "145",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "portal=9EEAD1F4784AC8BF7D24B6D06D65D465; _horizon_sid=fddcca10-975d-4109-90e2-89bc4579ce56; _horizon_uid=c7aebb2b-5c0f-4f88-a563-7fe987f24edf",
            "Host": "www.gdzwfw.gov.cn",
            "Origin": "http://www.gdzwfw.gov.cn",
            "Referer": "http://www.gdzwfw.gov.cn/portal/personal/theme?region=442000&catalogCode=",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        count = 0
        for page in range(49, 51):
            print('data page num is : ', page)
            data_req['pageNum'] = page
            res = requests.post(url, data=data_req, headers=headers_req)
            res_json = json.loads(res.text)
            data = res_json['data']
            # print(data)
            if data is None:
                print('jump out ')
                continue
            else:
                custom = data['CUSTOM']
                all_list = custom['AUDIT_ITEMLIST']
                # print(all_list)
                for index in range(0, len(all_list)):
                    print('名称: ', all_list[index]['TASK_NAME'])
                    count = count + 1
                    info = self.get_matter_info(all_list[index]['TASK_CODE'])
                    # print({...info})
                    all_list[index]['matter_name'] = info['matter_name']
                    all_list[index]['matter_short'] = info['matter_short']
                    all_list[index]['matter_daily'] = info['matter_daily']
                    all_list[index]['matter_code'] = info['matter_code']
                    all_list[index]['matter_level'] = info['matter_level']
                    all_list[index]['visit_number'] = info['visit_number']
                    all_list[index]['co_department'] = info['co_department']
                    all_list[index]['handle_location'] = info['handle_location']
                    all_list[index]['handle_time'] = info['handle_time']
                    all_list[index]['handle_time_limit'] = info['handle_time_limit']
                    all_list[index]['handle_type'] = info['handle_type']
                    all_list[index]['accept_standard'] = info['accept_standard']
                    all_list[index]['consult_phone'] = info['consult_phone']
                    all_list[index]['courier_service'] = info['courier_service']
                    all_list[index]['bear_paltform'] = info['bear_paltform']
                    all_list[index]['complain_phone'] = info['complain_phone']
                    # all_list[index]['charge'] = info['charge']
                    all_list[index]['matter_short'] = info['matter_short']
                    all_list[index]['online_book'] = info['online_book']
                    all_list[index]['online_book_addr'] = info['online_book_addr']
                    all_list[index]['consult_phone'] = info['consult_phone']
                    all_list[index]['district'] = info['district']
                    all_list[index]['theme_category'] = info['theme_category']
                    all_list[index]['service_object_name'] = info['service_object_name']
                    self.col.insert(all_list[index])

                print('页数: ', page, ' 总数：', count)
                time.sleep(1)


handler = MainData()
handler.get_page_data()
