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
            print(answers, 'ans')
            subject = answers[0]['m.name']
            if code:
                final_answer = '事项 {0} 的事项编码是：{1}'.format(subject, '；'.join(list(set(code))[:self.num_limit]))
            else:
                final_answer = '{0} 没有事项编码'.format(subject)

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
            print(answers,'ans')
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

        elif question_type == 'disease_cureway':
            desc = [';'.join(i['m.cure_way']) for i in answers]
            subject = answers[0]['m.name']
            final_answer = '{0}可以尝试如下治疗：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_cureprob':
            desc = [i['m.cured_prob'] for i in answers]
            subject = answers[0]['m.name']
            final_answer = '{0}治愈的概率为（仅供参考）：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_easyget':
            desc = [i['m.easy_get'] for i in answers]
            subject = answers[0]['m.name']

            final_answer = '{0}的易感人群包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_desc':
            desc = [i['m.desc'] for i in answers]
            subject = answers[0]['m.name']
            final_answer = '{0},熟悉一下：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_acompany':
            desc1 = [i['n.name'] for i in answers]
            desc2 = [i['m.name'] for i in answers]
            subject = answers[0]['m.name']
            desc = [i for i in desc1 + desc2 if i != subject]
            final_answer = '{0}的症状包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_not_food':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            final_answer = '{0}忌食的食物包括有：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

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

        elif question_type == 'check_disease':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            final_answer = '通常可以通过{0}检查出来的疾病有{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        return final_answer


if __name__ == '__main__':
    searcher = AnswerSearcher()
