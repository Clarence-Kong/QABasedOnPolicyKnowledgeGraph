# -*- coding: utf-8 -*-
# Author: Clarence Kong<clarencekong@qq.com,https://github.com/Clarence-Kong>
# @Time: 4/20/2021 10:42 PM


class QuestionPaser:
    '''构建实体节点'''

    def build_entitydict(self, args):
        entity_dict = {}
        for arg, types in args.items():
            for type in types:
                if type not in entity_dict:
                    entity_dict[type] = [arg]
                else:
                    entity_dict[type].append(arg)

        return entity_dict

    '''解析主函数'''

    def parser_main(self, res_classify):
        args = res_classify['args']
        entity_dict = self.build_entitydict(args)
        question_types = res_classify['question_types']
        sqls = []
        for question_type in question_types:
            sql_ = {}
            sql_['question_type'] = question_type
            sql = []
            if question_type == 'matter_short':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'matter_daily':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'matter_code':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'matter_level':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'visit_number':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'consult_phone':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'bear_paltform':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'co_department':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'handle_location':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'handle_time':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'handle_time_limit':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'material_intro':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))
            elif question_type == 'courier_service':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))
            elif question_type == 'matter_desc':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))
            elif question_type == 'handle_type':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))
            elif question_type == 'accept_standard':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))
            elif question_type == 'URL':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'disease_prevent':
                sql = self.sql_transfer(question_type, entity_dict.get('matter'))

            elif question_type == 'disease_lasttime':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_cureway':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_cureprob':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_easyget':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_desc':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            if sql:
                sql_['sql'] = sql

                sqls.append(sql_)

        return sqls

    '''针对不同的问题，分开进行处理'''

    def sql_transfer(self, question_type, entities):
        if not entities:
            return []

        # 查询语句
        sql = []
        # 简称
        if question_type == 'matter_short':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.mater_short".format(i) for i in entities]

        # 编码
        elif question_type == 'matter_code':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.matter_code".format(i) for i in entities]
   # 编码
        elif question_type == 'accept_standard':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.accept_standard".format(i) for i in entities]

        # 到现场次数
        elif question_type == 'visit_number':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.visit_number".format(i) for i in entities]

        # 到现场次数
        elif question_type == 'matter_level':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.matter_level".format(i) for i in entities]

        # 咨询电话
        elif question_type == 'consult_phone':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.consult_phone".format(i) for i in entities]

        # 承办平台
        elif question_type == 'bear_paltform':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.bear_paltform".format(i) for i in entities]

        # 联办部门
        elif question_type == 'co_department':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.easy_get".format(i) for i in entities]

        # 日常用语
        elif question_type == 'matter_daily':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.matter_daily".format(i) for i in entities]

        # 办理地点
        elif question_type == 'handle_location':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.handle_location".format(i) for i in entities]

        # 快递
        elif question_type == 'courier_service':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.courier_service".format(i) for i in entities]
        # 快递
        elif question_type == 'URL':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.URL".format(i) for i in entities]

        # 办公时间
        elif question_type == 'handle_time':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.handle_time".format(i) for i in entities]

        # 系统时限
        elif question_type == 'handle_time_limit':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.handle_time_limit".format(i) for i in
                   entities]

        # 事项材料
        elif question_type == 'material_intro':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m.name, m.material_intro".format(i) for i in entities]

        # 已知忌口查疾病
        elif question_type == 'food_not_disease':
            sql = ["MATCH (m:Matter)-[r:no_eat]->(n:Food) where n.name = '{0}' return m.name, r.name, n.name".format(i)
                   for i in entities]

        # 已知推荐查疾病
        elif question_type == 'food_do_disease':
            sql1 = ["MATCH (m:Matter)-[r:do_eat]->(n:Food) where n.name = '{0}' return m.name, r.name, n.name".format(i)
                    for i in entities]
            sql2 = [
                "MATCH (m:Matter)-[r:recommand_eat]->(n:Food) where n.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]
            sql = sql1 + sql2

        # 查询疾病常用药品－药品别名记得扩充
        elif question_type == 'disease_drug':
            sql1 = [
                "MATCH (m:Matter)-[r:common_drug]->(n:Drug) where m.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]
            sql2 = [
                "MATCH (m:Matter)-[r:recommand_drug]->(n:Drug) where m.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]
            sql = sql1 + sql2

        # 已知药品查询能够治疗的疾病
        elif question_type == 'drug_disease':
            sql1 = [
                "MATCH (m:Matter)-[r:common_drug]->(n:Drug) where n.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]
            sql2 = [
                "MATCH (m:Matter)-[r:recommand_drug]->(n:Drug) where n.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]
            sql = sql1 + sql2
        # 查询疾病应该进行的检查
        elif question_type == 'disease_check':
            sql = [
                "MATCH (m:Matter)-[r:need_check]->(n:Check) where m.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]

        # 已知检查查询疾病
        elif question_type == 'matter_desc':
            sql = ["MATCH (m:Matter) where m.name = '{0}' return m".format(i) for i in entities]

        return sql


if __name__ == '__main__':
    handler = QuestionPaser()
