# -*- coding: utf-8 -*-

from py2neo import Graph


class AnswerSearcher:
    def __init__(self):
        self.g = Graph(
            # host="127.0.0.1",
            # http_port=7474,
            user="neo4j",
            password="ckong")
        self.num_limit = 20

    '''执行cypher查询，并返回相应结果'''

    def search_main(self, sqls):
        final_answers = []
        for sql_ in sqls:
            question_type = sql_['question_type']
            queries = sql_['sql']
            answers = []
            for query in queries:
                ress = self.g.run(query).data()
                answers += ress
            final_answer = self.answer_prettify(question_type, answers)
            if final_answer:
                final_answers.append(final_answer)
        return final_answers

    '''根据对应的qustion_type，调用相应的回复模板'''

    def answer_prettify(self, question_type, answers):
        final_answer = []
        if not answers:
            return ''
        if question_type == 'matter_short':
            name = answers[0]['m.mater_short']
            subject = answers[0]['m.name']
            if name:
                final_answer = '{0}的别称是：{1}'.format(subject, '；'.join(list(set(name))[:self.num_limit]))
            else:
                final_answer = '{0}没有别称'.format(subject)

        elif question_type == 'matter_code':
            code = answers[0]['m.matter_code']
            subject = answers[0]['m.name']
            if code:
                final_answer = '事项 {0} 的事项编码是：{1}'.format(subject, '；'.join(list(set(code))[:self.num_limit]))
            else:
                final_answer = '{0} 没有事项编码'.format(subject)

        elif question_type == 'URL':
            URL = answers[0]['m.URL']
            subject = answers[0]['m.name']
            if URL:
                final_answer = '事项 {0} 的在线办理地址是：{1}'.format(subject, URL)
            else:
                final_answer = '{0} 没有在线办理地址'.format(subject)

        elif question_type == 'visit_number':
            num = answers[0]['m.visit_number']
            subject = answers[0]['m.name']
            if num:
                if num:
                    final_answer = '{0} 不需要线下办理'.format(subject)
                else:
                    final_answer = '{0}你只需要去：{1}'.format(subject, '；'.join(list(set(num))[:self.num_limit]))
            else:
                final_answer = '{0} 不知道要去几次'.format(subject)

        elif question_type == 'consult_phone':
            phone = answers[0]['m.consult_phone']
            subject = answers[0]['m.name']
            if phone:
                final_answer = '{0}事项的咨询电话是：{1}'.format(subject, phone)
            else:
                final_answer = '{0} 不知道电话是多少'.format(subject)

        elif question_type == 'bear_paltform':
            bear = answers[0]['m.bear_paltform']
            subject = answers[0]['m.name']
            if bear:
                final_answer = '{0}的承办系统是：{1}'.format(subject, bear)
            else:
                final_answer = '{0} 不知道是哪个系统'.format(subject)

        elif question_type == 'co_department':
            de = answers[0]['m.bear_paltform']
            subject = answers[0]['m.name']
            if de:
                co_department = [','.join(i['m.co_department']) for i in answers]
                final_answer = '{0}是由：{1}联合办理的'.format(subject, '；'.join(list(set(co_department))[:self.num_limit]))
            else:
                final_answer = '{0}没有联办部门'.format(subject)

        elif question_type == 'matter_daily':
            daily = answers[0]['m.matter_daily']
            subject = answers[0]['m.name']
            if daily:
                final_answer = '{0}的日常用用语：{1}'.format(subject, daily)
            else:
                final_answer = '{0} 没有日常用语'.format(subject)

        elif question_type == 'matter_level':
            level = answers[0]['m.matter_level']
            subject = answers[0]['m.name']
            if level:
                final_answer = '{0}的办事层级是：{1}'.format(subject, level)
            else:
                final_answer = '{0} 不知道是哪个层级'.format(subject)

        elif question_type == 'handle_time_limit':
            daily = answers[0]['m.handle_time_limit']
            subject = answers[0]['m.name']
            if daily == "无":
                final_answer = '{0} 不知道要多久'.format(subject)
            elif daily:
                final_answer = '{0}最多：{1} 能办理好'.format(subject, daily)
            else:
                final_answer = '{0} 不知道要多久'.format(subject)

        elif question_type == 'handle_location':
            daily = answers[0]['m.handle_location']
            subject = answers[0]['m.name']
            if daily:
                final_answer = '{0}{1}'.format(subject, daily)
            else:
                final_answer = '{0} 没有具体地点'.format(subject)

        elif question_type == 'courier_service':
            courier_service = answers[0]['m.courier_service']
            subject = answers[0]['m.name']
            if courier_service:
                final_answer = '{0}支持快递材料服务：{1}'.format(subject, courier_service)
            else:
                final_answer = '{0} 不能快递材料'.format(subject)

        elif question_type == 'handle_time':
            time = answers[0]['m.handle_time']
            subject = answers[0]['m.name']
            if time:
                final_answer = '{0}的法定时限是：{1}'.format(subject, time)
            else:
                final_answer = '{0} 没有具体时间限制'.format(subject)

        elif question_type == 'handle_time_limit':
            time = answers[0]['m.handle_time_limit']
            subject = answers[0]['m.name']
            if time:
                final_answer = '{0}的系统时限是：{1}'.format(subject, time)
            else:
                final_answer = '{0} 没有具体时间限制'.format(subject)

        elif question_type == 'material_intro':
            intro = answers[0]['m.material_intro']
            subject = answers[0]['m.name']
            if intro:
                all = ','.join(intro)
                final_answer = '{0}需要准备：{1}'.format(subject, all)
            else:
                final_answer = '{0}的办理不需要提供材料'.format(subject)

        elif question_type == 'accept_standard':
            intro = answers[0]['m.accept_standard']
            subject = answers[0]['m.name']
            if intro:
                final_answer = '{0}的办理条件是：{1}'.format(subject, intro)
            else:
                final_answer = '{0}不知道要什么条件'.format(subject)

        elif question_type == 'disease_do_food':
            do_desc = [i['n.name'] for i in answers if i['r.name'] == '宜吃']
            recommand_desc = [i['n.name'] for i in answers if i['r.name'] == '推荐食谱']
            subject = answers[0]['m.name']
            final_answer = '{0}宜食的食物包括有：{1}\n推荐食谱包括有：{2}'.format(subject, ';'.join(list(set(do_desc))[:self.num_limit]),
                                                                 ';'.join(list(set(recommand_desc))[:self.num_limit]))

        elif question_type == 'food_not_disease':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            final_answer = '患有{0}的人最好不要吃{1}'.format('；'.join(list(set(desc))[:self.num_limit]), subject)

        elif question_type == 'food_do_disease':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            final_answer = '患有{0}的人建议多试试{1}'.format('；'.join(list(set(desc))[:self.num_limit]), subject)

        elif question_type == 'disease_drug':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            final_answer = '{0}通常的使用的药品包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'drug_disease':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            final_answer = '{0}主治的疾病有{1},可以试试'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_check':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            final_answer = '{0}通常可以通过以下方式检查出来：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'matter_desc':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            final_answer = '通常可以通过{0}检查出来的疾病有{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        return final_answer


if __name__ == '__main__':
    searcher = AnswerSearcher()
