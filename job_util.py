def get_job_list(conn):
    return []


def valid_take_job(conn, wangwang_id, job_id):
    return True


def valid_submit_job(conn, wangwang_id, job_id):
    return True


def valid_publish(conn, new_job):
    cur = conn.cursor()
    cur.execute("INSERT INTO job VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (new_job.job_id, new_job.item_id, new_job.store_id, new_job.main_img_src, new_job.tao_key,
                 new_job.keyword, new_job.compare_img_src, new_job.sku, new_job.pay_amount,
                 new_job.task_amount, new_job.chat_questions, new_job.comments,
                 new_job.comment_img_src, new_job.salary, new_job.status))
    conn.commit()
    cur.close()
    return True


def valid_add_shuashou(conn, new_shuashou):
    cur = conn.cursor()
    cur.execute("INSERT INTO shuashou VALUES(?, ?, ?, ?, ?, ?)",
                (new_shuashou.wangwang_id, new_shuashou.sex, new_shuashou.tao_score,
                new_shuashou.wechat_id, new_shuashou.position, new_shuashou.referer_id))
    conn.commit()
    cur.close()
    return True


def valid_add_shop_store(conn, new_store):
    cur = conn.cursor()
    cur.execute("INSERT INTO shopstore VALUES(?, ?, ?, ?, ?)",
                (new_store.store_id, new_store.balance, new_store.salary_balance,
                 new_store.public_jobs, new_store.finished_jobs))
    conn.commit()
    cur.close()
    return True


