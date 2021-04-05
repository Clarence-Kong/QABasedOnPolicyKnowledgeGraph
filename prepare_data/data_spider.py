# -*- coding: utf-8 -*-
# Author: Clarence Kong<clarencekong@qq.com,https://github.com/Clarence-Kong>
# @Time: 3/7/2021 11:03 PM

import urllib.request
import urllib.parse
from lxml import etree
import pymongo
import re

'''基于中山12345政企通的业务知识库采集'''


def strip_content(content):
    return content.strip()


class CrimeSpider:
    def __init__(self):
        self.conn = pymongo.MongoClient()
        self.db = self.conn['policy']
        self.col = self.db['data']

    '''根据url，请求html'''

    def get_html(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.63 Safari/537.36'}
        req = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    ''' 获取类型对应问题 '''

    def get_type_ques(self, type_id):

        return

    '''获取信息'''

    def spider_main(self):
        for page in range(1, 11000):
            try:
                basic_url = 'http://jib.xywy.com/il_sii/gaishu/%s.htm' % page
                cause_url = 'http://jib.xywy.com/il_sii/cause/%s.htm' % page
                prevent_url = 'http://jib.xywy.com/il_sii/prevent/%s.htm' % page
                symptom_url = 'http://jib.xywy.com/il_sii/symptom/%s.htm' % page
                inspect_url = 'http://jib.xywy.com/il_sii/inspect/%s.htm' % page
                treat_url = 'http://jib.xywy.com/il_sii/treat/%s.htm' % page
                food_url = 'http://jib.xywy.com/il_sii/food/%s.htm' % page
                drug_url = 'http://jib.xywy.com/il_sii/drug/%s.htm' % page
                data = {}
                data['url'] = basic_url
                data['basic_info'] = self.basicinfo_spider(basic_url)
                # data['cause_info'] =  self.common_spider(cause_url)
                # data['prevent_info'] =  self.common_spider(prevent_url)
                # data['symptom_info'] = self.symptom_spider(symptom_url)
                # data['inspect_info'] = self.inspect_spider(inspect_url)
                # data['treat_info'] = self.treat_spider(treat_url)
                # data['food_info'] = self.food_spider(food_url)
                # data['drug_info'] = self.drug_spider(drug_url)
                print(page, basic_url)
                self.col.insert(data)

            except Exception as e:
                print(e, page)
        return

    '''基本信息解析'''

    def basicinfo_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        title = selector.xpath('//title/text()')[0]
        category = selector.xpath('//div[@class="wrap mt10 nav-bar"]/a/text()')
        desc = selector.xpath('//div[@class="jib-articl-con jib-lh-articl"]/p/text()')
        ps = selector.xpath('//div[@class="mt20 articl-know"]/p')
        infobox = []
        for p in ps:
            info = p.xpath('string(.)').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('   ',
                                                                                                        '').replace(
                '\t', '')
            infobox.append(info)
        basic_data = {}
        basic_data['category'] = category
        basic_data['name'] = title.split('的简介')[0]
        basic_data['desc'] = desc
        basic_data['attributes'] = infobox
        return basic_data

    '''treat_infobox治疗解析'''

    def treat_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        ps = selector.xpath('//div[starts-with(@class,"mt20 articl-know")]/p')
        infobox = []
        for p in ps:
            info = p.xpath('string(.)').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('   ',
                                                                                                        '').replace(
                '\t', '')
            infobox.append(info)
        return infobox

    '''treat_infobox治疗解析'''

    def drug_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        drugs = [i.replace('\n', '').replace('\t', '').replace(' ', '') for i in
                 selector.xpath('//div[@class="fl drug-pic-rec mr30"]/p/a/text()')]
        return drugs

    '''food治疗解析'''

    def food_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        divs = selector.xpath('//div[@class="diet-img clearfix mt20"]')
        try:
            food_data = {}
            food_data['good'] = divs[0].xpath('./div/p/text()')
            food_data['bad'] = divs[1].xpath('./div/p/text()')
            food_data['recommand'] = divs[2].xpath('./div/p/text()')
        except:
            return {}

        return food_data

    '''症状信息解析'''

    def symptom_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        symptoms = selector.xpath('//a[@class="gre" ]/text()')
        ps = selector.xpath('//p')
        detail = []
        for p in ps:
            info = p.xpath('string(.)').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('   ',
                                                                                                        '').replace(
                '\t', '')
            detail.append(info)
        symptoms_data = {}
        symptoms_data['symptoms'] = symptoms
        symptoms_data['symptoms_detail'] = detail
        return symptoms, detail

    '''检查信息解析'''

    def inspect_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        inspects = selector.xpath('//li[@class="check-item"]/a/@href')
        return inspects

    '''通用解析模块'''

    def common_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        ps = selector.xpath('//p')
        infobox = []
        for p in ps:
            info = p.xpath('string(.)').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('   ',
                                                                                                        '').replace(
                '\t', '')
            if info:
                infobox.append(info)
        return '\n'.join(infobox)

    '''获取'''

    def depart_detect(self, html):
        selector = etree.HTML(html)
        depart_list = {}
        depart_list['href'] = self.url_parser(html, '//div[@class="ddianos_smfuwon"]/div/a/@href')
        depart_list['name'] = selector.xpath('//div[@class="ddianos_smfuwon"]/div/a/text()')
        print(depart_list)
        return depart_list

    '''问题详情'''

    def quest_info(self, html):
        selector = etree.HTML(html)
        name_answer = {}
        name_answer['name'] = selector.xpath('//div[@class="zhwebf_mardjujthr"]/p[2]')
        name_answer['answer'] = selector.xpath('//div[@class="zhwebf_mardjujthr"]/p[6]')
        print(name_answer)
        return name_answer

    '''获取问题'''

    def get_depart_question(self, html):
        selector = etree.HTML(html)
        quest_list = {}
        name_answer = []
        quest_list['href'] = self.url_parser(html, '//a[@class="text-decoration:underline; color: blue"]/@onclick')
        for link in quest_list:
            print(quest_list)
        return quest_list

    '''遍历问题'''

    def depart_question(self, depart_list):
        quest_answer = {}
        for link in depart_list.href:
            html = self.get_html(link)

    ''' url解析 '''

    # 将获取到的id 转换为 url 链接
    def url_parser(self, content, path):
        selector = etree.HTML(content)
        url_list = selector.xpath(path)
        all_parse_url = []
        for i in url_list:
            id = re.findall(r"toInput\(\'(.+?)\'\)", i)
            url = 'http://12345.zs.gov.cn/searchBF/input.do?id={}&searchName='.format(id[0])
            all_parse_url.append(url)
        return all_parse_url

    ''' 获取对应类型问题 '''

    def type_of_question(self, html):
        selector = etree.HTML(html)
        quest_list = []
        quest_list_url = self.url_parser(html, '//a[@style="text-decoration:underline; color: blue;"]/@onclick')
        quest_list_name = selector.xpath('//a[@style="text-decoration:underline; color: blue;"]/text()')
        for i in range(0, len(quest_list_url)):
            quest_list.append({'url': quest_list_url[i], 'title': quest_list_name[i].strip()})
        return quest_list

    ''' 去除多余字符 '''

    ''' 问题页面内容获取 '''

    def content_parser(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        content = selector.xpath('//div[@class="item_c"]//span/text()')
        return list(map(strip_content, content))

    '''main'''

    def inspect_ques(self):
        try:
            # TODO 已知类型有如下，可以自动获取类型以应付网站更新
            data = {}
            type_list = [
                {'id': 202, 'name': "文化体育"},
                {'id': 203, 'name': "医疗卫生"},
                {'id': 223, 'name': "公用事业"},
                {'id': 205, 'name': "住房保障"},
                {'id': 206, 'name': "财税金融"},
                {'id': 281, 'name': "教育科研"},
                {'id': 208, 'name': "其他"},
                {'id': 221, 'name': "社会保障"},
                {'id': 222, 'name': "交通出行"}]
            question_list = []
            base_url = 'http://12345.zs.gov.cn/searchBF/searchFile.do?'
            for type in type_list:
                url = base_url + 'searchName=&typeId={}&dateSpan=&randomnumber=57247'.format(
                    type['id'])
                html = self.get_html(url)
                selector = etree.HTML(html)
                page_number = re.findall(r"共(.+?)页",
                                         selector.xpath('//td[@style="border: 0; height: 48px;"]/text()')[0])
                for i in range(0, int(page_number[0])):
                    url_page = base_url + 'pageNo={}&searchName=&orgId=&typeId={}&dateSpan=&randomnumber=49293'.format(
                        i, type['id'])
                    html_page = self.get_html(url_page)
                    selector_page = etree.HTML(html_page)
                    quest_list = self.type_of_question(html_page)
                    for ques in quest_list:
                        ques_info = {}
                        ques_info['url'] = ques['url']
                        ques_info['type'] = type['name']
                        ques_info['parent_id'] = type['id']
                        ques_info['title'] = ques['title']
                        ques_info['content'] = self.content_parser(ques['url'])
                        question_list.append(ques_info)
                        self.col.insert(ques_info)
                        print('insert ' + ques['title'])
            print(len(question_list))

        except Exception as e:
            print(e)


handler = CrimeSpider()
# handler.depart_detect('http://12345.zs.gov.cn/public/item/catalogList.do')
handler.inspect_ques()
# handler.content_parser('http://12345.zs.gov.cn/searchBF/input.do?id=110001315&searchName=')
