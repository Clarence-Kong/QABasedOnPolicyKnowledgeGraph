#!/usr/bin/env python3
# coding: utf-8

import os
import json
from py2neo import Graph, Node


class PolicyGraph:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        cur_dir = os.getcwd()
        self.data_path = os.path.join(cur_dir, 'data/policy.json')
        self.g = Graph(
            # host="127.0.0.1",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
            # http_port=7474,  # neo4j 服务器监听的端口号
            user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
            password="ckong")

    '''读取文件'''

    def read_nodes(self):
        # 共７类节点
        matter = []  # 事项
        theme = []  # 服务主题
        man = []  # 服务对象
        power = []  # 权力类型
        district = []  # 行政区划
        department = []  # 部门

        policy_infos = []
        # 构建节点实体关系
        consists_of = []  # 下设
        theme_object = []  # 主题对象
        theme_category = []  # 事项主题
        matter_object = []  # 事项对象
        belong_to = []  # 丛属
        management_level = []  # 办事层级
        own_resonsibility = []  # 拥有权责
        accrual_item = []  # 权责事项
        govern_thing = []  # 管辖

        count = 0
        for data in open(self.data_path, encoding='utf-8'):
            policy_dict = {}
            count += 1
            data_json = json.loads(data)
            policies = data_json["TASK_NAME"]
            policy_dict["name"] = policies
            matter.append(policies)
            for cate in data_json['theme_category']:
                theme.append(cate)
            for obj in data_json['service_object_name']:
                man.append(obj)
            department.append(data_json['DEPT_NAME'])
            district.append(data_json['district'])
            power.append(data_json['TASK_TYPE_TEXT'])
            policy_dict['matter_short'] = ''
            policy_dict['matter_daily'] = ''
            policy_dict['matter_code'] = ''
            policy_dict['matter_level'] = ''
            policy_dict['visit_number'] = ''
            policy_dict['co_department'] = ''
            policy_dict['handle_location'] = ''
            policy_dict['handle_time'] = ''
            policy_dict['handle_time_limit'] = ''
            policy_dict['handle_type'] = ''
            policy_dict['accept_standard'] = ''
            policy_dict['consult_phone'] = ''
            policy_dict['courier_service'] = ''
            policy_dict['bear_paltform'] = ''
            policy_dict['complain_phone'] = ''
            policy_dict['charge'] = ''
            policy_dict['online_book'] = ''
            policy_dict['online_book_addr'] = ''
            policy_dict['executer'] = ''
            policy_dict['service_object_name'] = ''
            policy_dict['material_intro'] = ''
            policy_dict['courier_service'] = ''
            policy_dict['URL'] = ''

            if 'theme_category' in data_json:
                for cate in data_json['theme_category']:
                    theme_category.append([policies, cate])

            if 'service_object_name' in data_json:
                for name in data_json['service_object_name']:
                    matter_object.append([policies, name])
                for cate in data_json['theme_category']:
                    for obj in data_json['service_object_name']:
                        theme_object.append([cate, obj])

            if 'AREA_CODE_TEXT' in data_json:
                dep = data_json['AREA_CODE_TEXT']
                depar = data_json['DEPT_NAME']
                belong_to.append([dep, depar])

            if 'DEPT_NAME' in data_json:
                dep = data_json['DEPT_NAME']
                consists_of.append([data_json['district'], dep])

            if 'TASK_TYPE_TEXT' in data_json:
                dep = data_json['DEPT_NAME']
                own_resonsibility.append([dep, data_json['TASK_TYPE_TEXT']])
                accrual_item.append([dep, policies])

            if 'DEPT_NAME' in data_json:
                dep = data_json['DEPT_NAME']
                management_level.append([policies, dep])

            if 'name' in data_json:
                policy_dict['name'] = data_json['name']

            if 'matter_short' in data_json:
                policy_dict['matter_short'] = data_json['matter_short']

            if 'matter_daily' in data_json:
                policy_dict['matter_daily'] = data_json['matter_daily']

            if 'matter_code' in data_json:
                policy_dict['matter_code'] = data_json['matter_code']

            if 'material_intro' in data_json:
                policy_dict['material_intro'] = data_json['material_intro']

            if 'courier_service' in data_json:
                policy_dict['courier_service'] = data_json['courier_service']

            if 'URL' in data_json:
                policy_dict['URL'] = data_json['URL']

            if 'visit_number' in data_json:
                policy_dict['visit_number'] = data_json['visit_number']
            if 'co_department' in data_json:
                policy_dict['co_department'] = data_json['co_department']
            if 'handle_location' in data_json:
                policy_dict['handle_location'] = data_json['handle_location']
            if 'handle_time' in data_json:
                policy_dict['handle_time'] = data_json['handle_time']
            if 'handle_time_limit' in data_json:
                policy_dict['matter_level'] = data_json['matter_level']
            if 'handle_time_limit' in data_json:
                policy_dict['handle_time_limit'] = data_json['handle_time_limit']
            if 'handle_type' in data_json:
                policy_dict['handle_type'] = data_json['handle_type']
            if 'accept_standard' in data_json:
                policy_dict['accept_standard'] = data_json['accept_standard']
            if 'consult_phone' in data_json:
                policy_dict['consult_phone'] = data_json['consult_phone']

            if 'courier_service' in data_json:
                policy_dict['courier_service'] = data_json['courier_service']

            if 'bear_paltform' in data_json:
                policy_dict['bear_paltform'] = data_json['bear_paltform']

            if 'complain_phone' in data_json:
                policy_dict['complain_phone'] = data_json['complain_phone']

            if 'charge' in data_json:
                policy_dict['charge'] = data_json['charge']

            if 'online_book' in data_json:
                policy_dict['online_book'] = data_json['online_book']

            if 'online_book_addr' in data_json:
                policy_dict['online_book_addr'] = data_json['online_book_addr']

            if 'executer' in data_json:
                policy_dict['executer'] = data_json['executer']

            if 'service_object_name' in data_json:
                policy_dict['service_object_name'] = data_json['service_object_name']

            if 'management_level' in data_json:
                policy_dict['service_object_name'] = data_json['service_object_name']

            policy_infos.append(policy_dict)
        return set(matter), set(theme), set(man), set(power), set(department), set(district), policy_infos, \
               consists_of, theme_object, theme_category, matter_object, belong_to, \
               management_level, own_resonsibility, accrual_item, govern_thing,

    '''建立节点'''

    def create_node(self, label, nodes):
        count = 0
        for node_name in nodes:
            node = Node(label, name=node_name)
            self.g.create(node)
            count += 1
        return

    '''创建知识图谱中心疾病的节点'''

    def create_policies_nodes(self, policy_infos):
        count = 0
        for policy_dict in policy_infos:
            node = Node("Matter", name=policy_dict['name'], matter_short=policy_dict['matter_short'],
                        matter_daily=policy_dict['matter_daily'], matter_code=policy_dict['matter_code'],
                        matter_level=policy_dict['matter_level'], visit_number=policy_dict['visit_number'],
                        co_department=policy_dict['co_department'], handle_location=policy_dict['handle_location'],
                        handle_time=policy_dict['handle_time'], handle_time_limit=policy_dict['handle_time_limit'],
                        handle_type=policy_dict['handle_type'], accept_standard=policy_dict['accept_standard'],
                        consult_phone=policy_dict['consult_phone'], courier_service=policy_dict['courier_service'],
                        bear_paltform=policy_dict['bear_paltform'], complain_phone=policy_dict['complain_phone'],
                        charge=policy_dict['charge'], online_book=policy_dict['online_book'],
                        online_book_addr=policy_dict['online_book_addr'], executer=policy_dict['executer'],
                        service_object_name=policy_dict['service_object_name'],
                        material_intro=policy_dict['material_intro'],
                        URL=policy_dict['URL'])
            self.g.create(node)
            count += 1
            print(count)
        return

    '''创建知识图谱实体节点类型schema'''

    def create_graphnodes(self):
        Matter, Theme, Man, Power, Department, District, policy_infos, consists_of, \
        theme_object, theme_category, matter_object, belong_to, management_level, own_resonsibility, \
        accrual_item, govern_thing = self.read_nodes()
        self.create_policies_nodes(policy_infos)
        self.create_node('Matter', Matter)
        print('Matter len', len(Matter))
        self.create_node('Theme', Theme)
        print('Theme len', len(Theme))
        self.create_node('Man', Man)
        print('Man len', len(Man))
        self.create_node('Power', Power)
        print('Power len', len(Power))
        self.create_node('Department', Department)
        print('Department len', len(Department))
        self.create_node('District', District)
        print('District len', len(District))
        return

    '''创建实体关系边'''

    def create_graphrels(self):
        Matter, Theme, Man, Power, Department, District, policy_infos, consists_of, \
        theme_object, theme_category, matter_object, belong_to, management_level, own_resonsibility, \
        accrual_item, govern_thing = self.read_nodes()
        print(matter_object, 'matter ob-----')
        self.create_relationship('Matter', 'Theme', theme_category, 'theme_category', '服务主题')
        self.create_relationship('Theme', 'Man', theme_object, 'theme_object', '对象')
        self.create_relationship('District', 'Department', consists_of, 'consists_of', '下设')
        self.create_relationship('Department', 'Department', belong_to, 'belong_to', '属于')
        self.create_relationship('Matter', 'District', management_level, 'management_level', '办事层级')
        self.create_relationship('Matter', 'Man', matter_object, 'matter_object', '事项对象')
        self.create_relationship('Department', 'Power', own_resonsibility, 'own_resonsibility', '拥有权责')
        self.create_relationship('Department', 'Matter', accrual_item, 'accrual_item', '权责事项')
        self.create_relationship('District', 'District', govern_thing, 'govern_thing', '管辖')

    '''创建实体关联边'''

    def create_relationship(self, start_node, end_node, edges, rel_type, rel_name):
        count = 0
        # 去重处理
        set_edges = []
        for edge in edges:
            set_edges.append('###'.join(edge))
        all = len(set(set_edges))
        for edge in set(set_edges):
            edge = edge.split('###')
            p = edge[0]
            q = edge[1]
            query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:%s{name:'%s'}]->(q)" % (
                start_node, end_node, p, q, rel_type, rel_name)
            try:
                self.g.run(query)
                count += 1
                print(rel_type, count, all)
            except Exception as e:
                print(e)
        return

    '''导出数据'''

    def export_data(self):
        Matter, Theme, Man, Power, Department, District, policy_infos, consists_of, \
        theme_object, theme_category, matter_object, belong_to, management_level, own_resonsibility, \
        accrual_item, govern_thing = self.read_nodes()
        f_matter = open('dict/matter.txt', 'w+', encoding="utf-8")
        f_theme = open('dict/theme.txt', 'w+', encoding="utf-8")
        f_man = open('dict/man.txt', 'w+', encoding="utf-8")
        f_district = open('dict/district.txt', 'w+', encoding="utf-8")
        f_department = open('dict/department.txt', 'w+', encoding="utf-8")
        f_power = open('dict/power.txt', 'w+', encoding="utf-8")
        f_matter.write('\n'.join(list(Matter)))
        f_theme.write('\n'.join(list(Theme)))
        f_man.write('\n'.join(list(Man)))
        f_district.write('\n'.join(list(District)))
        f_department.write('\n'.join(list(Department)))
        f_power.write('\n'.join(list(Power)))

        f_matter.close()
        f_theme.close()
        f_man.close()
        f_district.close()
        f_department.close()
        f_power.close()

        return


if __name__ == '__main__':
    handler = PolicyGraph()
    handler.create_graphnodes()
    handler.create_graphrels()
    handler.export_data()
