# -*- coding: utf-8 -*-

import os
import ahocorasick


class QuestionClassifier:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        # 　特征词路径
        self.matter_path = os.path.join(cur_dir, 'dict/matter.txt')
        self.department_path = os.path.join(cur_dir, 'dict/department.txt')
        self.district_path = os.path.join(cur_dir, 'dict/district.txt')
        self.man_path = os.path.join(cur_dir, 'dict/man.txt')
        self.power_path = os.path.join(cur_dir, 'dict/power.txt')
        self.theme_path = os.path.join(cur_dir, 'dict/theme.txt')
        self.deny_path = os.path.join(cur_dir, 'dict/theme.txt')
        # 加载特征词
        self.matter_wds = [i.strip() for i in open(self.matter_path, encoding='utf-8') if i.strip()]
        self.department_wds = [i.strip() for i in open(self.department_path, encoding='utf-8') if i.strip()]
        self.district_wds = [i.strip() for i in open(self.district_path, encoding='utf-8') if i.strip()]
        self.man_wds = [i.strip() for i in open(self.man_path, encoding='utf-8') if i.strip()]
        self.power_wds = [i.strip() for i in open(self.power_path, encoding='utf-8') if i.strip()]
        self.theme_wds = [i.strip() for i in open(self.theme_path, encoding='utf-8') if i.strip()]
        self.region_words = set(
            self.department_wds + self.matter_wds + self.district_wds + self.man_wds + self.power_wds + self.theme_wds)
        self.deny_words = [i.strip() for i in open(self.deny_path, encoding='utf-8') if i.strip()]
        # 构造领域actree
        self.region_tree = self.build_actree(list(self.region_words))
        # 构建词典
        self.wdtype_dict = self.build_wdtype_dict()
        # 问句疑问词
        self.matter_short = ['简称', '简写', '别称', '别名']
        self.matter_daily = ['日常用语', '常用语']
        self.matter_code = ['编码', '事项编码']
        self.matter_level = ['事项层级', '层级']
        self.visit_number = ['次数', '几次', '去几次', '线下办理']
        self.co_department = ['部门', '几个部门', '联办', '几个部门', "一起"]
        self.handle_location = ['地点','地址', '怎么办理', '如何办理', '怎么办理', '哪里办理', '办理地点']
        self.handle_time_limit = ['多久能办好', '要多久', '多长时间', '几天', '几个工作日', '耗时多久']
        self.handle_time = ['法定时间', '最多多久', '规定多久办好', '规定多久']
        self.handle_type = ['承诺办结', '最多多久']
        self.accept_standard = ['受理条件', '什么条件', '办理条件', '办理资格']
        self.consult_phone = ['咨询电话', '客服', '客服电话', '怎么咨询']
        self.bear_paltform = ['业务系统', '办理系统', '承办系统', '哪个系统']
        self.matter_intro = ['材料', '哪些材料', '准备什么', '哪些文件']
        self.courier_service = ['快递', '可以快递', '快递材料', '支持快递']
        self.URL = ['哪里办理', '网站', '网址','地址']
        print('model init finished ......')

        return

    '''分类主函数'''

    def classify(self, question):
        data = {}
        policy_dict = self.check_policy(question)
        if not policy_dict:
            return {}
        data['args'] = policy_dict
        # 收集问句当中所涉及到的实体类型
        types = []
        for type_ in policy_dict.values():
            types += type_
        question_type = 'others'

        question_types = []

        # 简称
        if self.check_words(self.matter_short, question) and ('matter' in types):
            question_type = 'matter_short'
            question_types.append(question_type)
        #
        if self.check_words(self.matter_daily, question) and ('matter' in types):
            question_type = 'matter_daily'
            question_types.append(question_type)

        # 编码
        if self.check_words(self.matter_code, question) and ('matter' in types):
            question_type = 'matter_code'
            question_types.append(question_type)
        # # 并发症
        # if self.check_words(self.matter_code, question) and ('matter' in types):
        #     question_type = 'matter_code'
        #     question_types.append(question_type)

        # 办事层级
        if self.check_words(self.matter_level, question) and 'matter' in types:
            question_type = 'matter_level'
            question_types.append(question_type)
        # 办事层级
        if self.check_words(self.accept_standard, question) and 'matter' in types:
            question_type = 'accept_standard'
            question_types.append(question_type)
        # 网站
        if self.check_words(self.URL, question) and 'matter' in types:
            question_type = 'URL'
            question_types.append(question_type)

        # 到访次数
        if self.check_words(self.visit_number, question) and 'matter' in types:
            question_type = 'visit_number'
            question_types.append(question_type)
        # 快递
        if self.check_words(self.courier_service, question) and 'matter' in types:
            question_type = 'courier_service'
            question_types.append(question_type)

        # 咨询电话
        if self.check_words(self.consult_phone, question) and 'matter' in types:
            question_type = 'consult_phone'
            question_types.append(question_type)

        # 承办平台
        if self.check_words(self.bear_paltform, question) and 'matter' in types:
            question_type = 'bear_paltform'
            question_types.append(question_type)

        # # 已知检查项目查相应疾病
        # if self.check_words(self.bear_paltform + self.consult_phone, question) and 'check' in types:
        #     question_type = 'check_matter'
        #     question_types.append(question_type)

        # 　症状防御
        # if self.check_words(self.disease_do_food, question) and 'matter' in types:
        #     question_type = 'matter_prevent'
        #     question_types.append(question_type)

        # 联办部门
        if self.check_words(self.co_department, question) and 'matter' in types:
            question_type = 'co_department'
            question_types.append(question_type)

        # 办理地点
        if self.check_words(self.handle_location, question) and 'matter' in types:
            question_type = 'handle_location'
            question_types.append(question_type)

        # 办理时间
        if self.check_words(self.handle_time, question) and 'matter' in types:
            question_type = 'handle_time'
            question_types.append(question_type)

        # 承诺办理时限
        if self.check_words(self.handle_time_limit, question) and 'matter' in types:
            question_type = 'handle_time_limit'
            question_types.append(question_type)

        # 材料
        if self.check_words(self.matter_intro, question) and 'matter' in types:
            question_type = 'material_intro'
            question_types.append(question_type)

        # 若没有查到相关的外部查询信息，那么则将该疾病的描述信息返回
        # if question_types == [] and 'matter' in types:
        #     question_types = ['matter_desc']

        # # 若没有查到相关的外部查询信息，那么则将该疾病的描述信息返回
        # if question_types == [] and 'symptom' in types:
        #     question_types = ['symptom_matter']

        # 将多个分类结果进行合并处理，组装成一个字典
        data['question_types'] = question_types

        return data

    '''构造词对应的类型'''

    def build_wdtype_dict(self):
        wd_dict = dict()
        for wd in self.region_words:
            wd_dict[wd] = []
            if wd in self.matter_wds:
                wd_dict[wd].append('matter')
            if wd in self.department_wds:
                wd_dict[wd].append('department')
            if wd in self.man_wds:
                wd_dict[wd].append('man')
            if wd in self.power_wds:
                wd_dict[wd].append('power')
            if wd in self.theme_wds:
                wd_dict[wd].append('theme')
        return wd_dict

    '''构造actree，加速过滤'''

    def build_actree(self, wordlist):
        actree = ahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    '''问句过滤'''

    def check_policy(self, question):
        region_wds = []
        for i in self.region_tree.iter(question):
            wd = i[1][1]
            region_wds.append(wd)
        stop_wds = []
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        final_dict = {i: self.wdtype_dict.get(i) for i in final_wds}

        return final_dict

    '''基于特征词进行分类'''

    def check_words(self, wds, sent):
        for wd in wds:
            if wd in sent:
                return True
        return False


if __name__ == '__main__':
    handler = QuestionClassifier()
    while 1:
        question = input('input an question:')
        data = handler.classify(question)
