CREATE TABLE shuashou(wangwang_id text PRIMARY KEY, sex text, tao_score text, wechat_id text, position text, referer_id text)

CREATE TABLE job(job_id text PRIMARY KEY, item_id text, store_id text, main_img_src text, tao_key text, keyword text,
 compare_img_src text, sku text, pay_amount text, task_amount text, chat_questions text, comments text, comment_img_src text, salary text, status text, assign text)

CREATE TABLE shopstore(store_id text PRIMARY KEY, balance text, salary_balance text, public_jobs text, finished_jobs text)
