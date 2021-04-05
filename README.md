# QABasedOnPolicyKnowledgeGraph
基于知识图谱的政务问答系统

# 内容获取

> 从[中山市政企通平台业务知识库](http://12345.zs.gov.cn/businessFile/queryBusinessKM.do)中获取政策相关解读

依据知识类型分为以下类型

- 文化体育 typeId 202 [URL](http://12345.zs.gov.cn/searchBF/searchFile.do?searchName=&typeId=202&dateSpan=&randomnumber=57247)
- 医疗卫生 typeId 203 [URL](http://12345.zs.gov.cn/searchBF/searchFile.do?searchName=&typeId=203&dateSpan=&randomnumber=86509)  
- 公用事业 typeId 223 [URL](http://12345.zs.gov.cn/searchBF/searchFile.do?searchName=&typeId=223&dateSpan=&randomnumber=80918)
- 住房保障 typeId 205 [URL](http://12345.zs.gov.cn/searchBF/searchFile.do?searchName=&typeId=205&dateSpan=&randomnumber=78526)
- 财税金融 typeId 206 [URL](http://12345.zs.gov.cn/searchBF/searchFile.do?searchName=&typeId=206&dateSpan=&randomnumber=21762)
- 教育科研 typeId 281 [URL](http://12345.zs.gov.cn/searchBF/searchFile.do?searchName=&typeId=281&dateSpan=&randomnumber=57752)
- 其他 typeId 208 [URL](http://12345.zs.gov.cn/searchBF/searchFile.do?searchName=&typeId=208&dateSpan=&randomnumber=1021)
- 社会保障 typeId 221 [URL](http://12345.zs.gov.cn/searchBF/searchFile.do?searchName=&typeId=221&dateSpan=&randomnumber=68239)
- 交通出行 typeId 222 [URL](http://12345.zs.gov.cn/searchBF/searchFile.do?searchName=&typeId=221&dateSpan=&randomnumber=68239)

知识类形

## 实体类型

| 实体类型  | 中文含义 | 实体数量 | 举例                              |
| :-------- | :------: | :------: | :-------------------------------- |
| Matter    |   事项   |    34    | 中山税务局;公安局                 |
| Theme     | 服务主题 |    54    | 整形美容科;烧伤科                 |
| Power     | 权力类型 |  8,807   | 血栓闭塞性脉管炎;胸降主动脉动脉瘤 |
| District  | 行政区划 |  3,828   | 京万红痔疮膏;布林佐胺滴眼液       |
| Deparment |   部门   |  4,870   | 番茄冲菜牛肉丸汤;竹笋炖羊肉       |


## 实体关系类型

| 实体关系类型      |   中文含义   | 关系数量 | 举例                                                 |
| :---------------- | :----------: | :------: | :--------------------------------------------------- |
| Consists_of       |     下设     |  8,844   | <妇科,属于,妇产科>                                   |
| Theme_object      |   主题对象   |  14,649  | <阳强,常用,甲磺酸酚妥拉明分散片>                     |
| matter_subject    |   事项主题   |  22,238  | <胸椎骨折,宜吃,黑鱼>                                 |
| matter_object     |   事项对象   |  17,315  | <青霉素V钾片,在售,通药制药青霉素V钾片>               |
| belong_to         |     丛属     |  39,422  | <单侧肺气肿,所需检查,支气管造影>                     |
| management_level  |   办事层级   |  22,247  | <唇病,忌吃,杏仁>                                     |
| own_resonsibility |   拥有权责   |  59,467  | <混合痔,推荐用药,京万红痔疮膏>                       |
| accrual_item      |   权责事项   |  40,221  | <鞘膜积液,推荐食谱,番茄冲菜牛肉丸汤>                 |
| govern_thing      |     管辖     |  5,998   | <早期乳腺癌,疾病症状,乳腺组织肥厚>                   |


## 属性类型

| 属性类型      |   中文含义   |            举例             |
| :------------ | :----------: | :-------------------------: |
|  matter_name   |   事项名称||
| matter_code |   事项编码||
| mattrer_level | 事项层级   |       喘息样支气管炎        |
| visit_number | 到现场次数||
| co_department | 共同办理部门||
| gohome_materials | 上门收取材料||
| handle_location | 办理地点||
| handle_time | 办理时间||
| handle_time_limit | 办理时限||
| handle_type | 办理类型||
| accept_standard | 受理标准||
| consult_phone | 咨询电话||
| courier_service | 快递服务||
| bear_paltform | 承载平台||
| complain_phone | 投诉电话||
| charge | 收费||
| online_book | 网上预约||
| collect_resource_center | 纳入资源服务中心||
| service_content | 服务内容||
| material_intro | 材料说明||
| involved_mediation | 涉及中介||
| application_material | 申请材料||
| online_payment | 网上支付||
| certification_level_requirement | 认证等级需求||
|   setting_basis  |设定依据||
| service_theme_name |服务主题名称||
| service_object_name |服务对象名称||
| power_name |权力名称||
