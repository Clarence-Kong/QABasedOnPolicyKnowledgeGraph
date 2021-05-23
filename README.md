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
| Man   | 服务对象 |    54    | 整形美容科;烧伤科                 |
| Power     | 权力类型 |  8,807   | 血栓闭塞性脉管炎;胸降主动脉动脉瘤 |
| District  | 行政区划 |  3,828   | 京万红痔疮膏;布林佐胺滴眼液       |
| Deparment |   部门   |  4,870   | 番茄冲菜牛肉丸汤;竹笋炖羊肉       |


## 实体关系类型

| 实体关系类型      | 中文含义 | 关系数量 | 举例                                   |
| :---------------- | :------: | :------: | :------------------------------------- |
| Consists_of       |   下设   |  8,844   | <妇科,属于,妇产科>                     |
| Theme_object      | 主题对象 |  14,649  | <阳强,常用,甲磺酸酚妥拉明分散片>       |
| matter_subject    | 事项主题 |  22,238  | <胸椎骨折,宜吃,黑鱼>                   |
| matter_object     | 事项对象 |  17,315  | <青霉素V钾片,在售,通药制药青霉素V钾片> |
| belong_to         |   丛属   |  39,422  | <单侧肺气肿,所需检查,支气管造影>       |
| management_level  | 办事层级 |  22,247  | <唇病,忌吃,杏仁>                       |
| own_resonsibility | 拥有权责 |  59,467  | <混合痔,推荐用药,京万红痔疮膏>         |
| accrual_item      | 权责事项 |  40,221  | <鞘膜积液,推荐食谱,番茄冲菜牛肉丸汤>   |
| govern_thing      |   管辖   |  5,998   | <早期乳腺癌,疾病症状,乳腺组织肥厚>     |


## 属性类型

| 属性类型      |   中文含义   |            举例             |
| :------------ | :----------: | :-------------------------: |
|  matter_name   |   事项名称|中外合作开办学前教育机构审批|
| matter_short|事项名称短语|无|
|matter_daily|日常用语|无|
| matter_code |   事项编码||
| mattrer_level | 事项层级   |       市级      |
| visit_number | 到现场次数|1|
| co_department | 共同办理部门|[ 中山市教育和体育局](http://www.gdzwfw.gov.cn/portal/branch-hall?orgCode=324776913)|
| handle_methods | 办理形式 |网上办理,窗口办理,快递申请|
| handle_location | 办理地点|中山市东区博爱六路22号市行政服务中心C区C10、C11、C12窗口|
| handle_time | 办理时间|周一至周五：上午9：00至12：00，下午13：30至17：00，法定节假日除外|
| handle_time_limit | 办理时限|1 ( 工作日 )|
| handle_legal_limit|法定实现|90 ( 工作日 )|
| handle_type | 办理类型|即办件|
| accept_standard | 受理标准|国家机构以外的社会组织或者个人（大陆境内）利用非国家财政性经费|
| consult_phone | 咨询电话|0760-89817133|
| courier_service | 快递服务|是|
| bear_paltform | 承载平台|中山市统一申办受理平台|
| complain_phone | 投诉电话|0760-89989215|
| charge | 收费|不收费|
| online_book | 网上预约|是|
| excuter                         |       实施主体       |[中山市教育和体育局](http://www.gdzwfw.gov.cn/portal/branch-hall?orgCode=324776913)|
| Self_terminal                   | 是否支持自助终端办理 |是|
| material_intro | 材料说明|其他都装里头|
| involved_mediation | 涉及中介||
| application_material | 申请材料|申请正式建校可行性论证报告|
| online_payment | 网上支付|否|
| theme_object |                      ||
|   setting_basis  |设定依据|[《教育部关于印发<中等职业学校管理规程>的通知》](http://www.gd.gov.cn/zwgk/wjk/zcfgk/content/post_2521446.html)|
| theme_category       |服务主题名称|教育科研,升学,儿童青少年|
| service_object_name |服务对象名称|自然人,企业法人,社会组织法人|
|application_content|       主题分类       |适用于中外合作开办学前教育机构审批的申请|
|                      |                      ||

![image-20210416221036232](C:\Users\ckong\AppData\Roaming\Typora\typora-user-images\image-20210416221036232.png)

# 2.3　支持问答类型

| 问句类型          |      中文含义      |                问句举例                |
| :---------------- | :----------------: | :------------------------------------: |
| matter_short      |      事项简称      |    中外合作办学审核审批简称是什么？    |
| matter_daily      | 已知症状找可能疾病 |          最近老流鼻涕怎么办？          |
| matter_code       |      事项编码      |   中外合作办学审核审批事项编码是什么   |
| matter_level      |    疾病的并发症    |           失眠有哪些并发症？           |
| visit_number      |      到访次数      |   中外合作办学审核审批需要到访几次？   |
| disease_do_food   | 疾病建议吃什么食物 |             耳鸣了吃点啥？             |
| co_department     |      联办部门      | 中外合作办学审核审批有哪几个联办部门？ |
| handle_location   |      办理地点      |            鹅肉有什么好处？            |
| handle_time       |      办理时间      |             肝病要吃啥药？             |
| handle_time_limit |      办理时限      |          板蓝根颗粒能治啥病？          |
| handle_type       |      办理类型      |           办件类型 （即办）            |
| accept_standard   |      受理标准      |        全血细胞计数能查出啥来？        |
| consult_phone     |      咨询电话      |           怎样才能预防肾虚？           |
| bear_paltform     |      办理平台      |           感冒要多久才能好？           |
| complain_phone    |      投诉电话      |            高血压要怎么治？            |
| online_book_addr  |      在线预约      |            白血病能治好吗？            |
| district          |     b案例层级      |          什么人容易得高血压？          |
| theme_category    |      事项类型      |                 糖尿病                 |