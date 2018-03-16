# 接口定义

- jobs: GET, 获得所有可接任务

- userjobs: GET. 获得刷手已接和已提交任务   [wangwang_id]

- take: POST，刷手接任务  [wangwang_id, job_id]

- submit: POST, 刷手提交任务  [confirm_img_src, wangwang_id, job_id]

- approve: POST, 商家批准任务 [wangwang_id, job_id]

- publish: POST, 商家发布任务 [store_id, item_id ..]

- add_shuashou: POST, 添加刷手  [wangwang_id..]

- add_shop_store: POST, 添加商家    [store_id]

# 数据库
- job: 任务信息
- shuashou: 刷手信息
- shopstore: 商家信息
