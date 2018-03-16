from api.job import Job


def construct_job(row):
    job = Job()
    job.job_id = row[0]
    job.item_id = row[1]
    job.store_id = row[2]
    job.main_img_src = row[3]
    job.tao_key = row[4]
    job.keyword = row[5]
    job.compare_img_src = row[6]
    job.sku = row[7]
    job.pay_amount = row[8]
    job.task_amount = row[9]
    job.chat_questions = row[10]
    job.comments = row[11]
    job.comment_img_src = row[12]
    job.salary = row[13]
    job.status = row[14]
    job.assign = row[15]
    return job


def retrieve_job(conn, job_id):
    cur = conn.cursor()
    cur.execute('SELECT * FROM job WHERE job_id=? AND status="published"', (job_id, ))
    rows = cur.fetchall()
    cur.close()
    return [construct_job(row) for row in rows]


def retrieve_job_list(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM job WHERE status="published"')
    rows = cur.fetchall()
    cur.close()
    return [construct_job(row) for row in rows]


def retrieve_submitted_job_list(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM job WHERE status="submitted"')
    rows = cur.fetchall()
    cur.close()
    return [construct_job(row) for row in rows]


def retrieve_user_job_list(conn, wangwang_id):
    cur = conn.cursor()
    cur.execute('SELECT * FROM job WHERE (status="assigned" OR status="submitted") AND assign = ?', (wangwang_id,))
    rows = cur.fetchall()
    cur.close()
    return [construct_job(row) for row in rows]


def valid_take_job(conn, wangwang_id, job_id):
    cur = conn.cursor()
    cur.execute('UPDATE job SET status = "assigned", assign = ? WHERE job_id = ?',
                (wangwang_id, job_id))
    conn.commit()
    cur.close()
    return True


def valid_submit_job(conn, job_id, confirm_img_srcs):
    cur = conn.cursor()
    cur.execute('UPDATE job SET status = "submitted", confirm_img_srcs = ? WHERE job_id = ?',
                (confirm_img_srcs, job_id,))
    conn.commit()
    cur.close()
    return True


def valid_approve_job(conn, job_id):
    cur = conn.cursor()
    cur.execute('UPDATE job SET status = "approved" WHERE job_id = ?',
                (job_id,))
    conn.commit()
    cur.close()
    return True


def valid_publish(conn, new_job):
    cur = conn.cursor()
    cur.execute("INSERT INTO job VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (new_job.job_id, new_job.item_id, new_job.store_id, new_job.main_img_src, new_job.tao_key,
                 new_job.keyword, new_job.compare_img_src, new_job.sku, new_job.pay_amount,
                 new_job.task_amount, new_job.chat_questions, new_job.comments,
                 new_job.comment_img_src, new_job.salary, new_job.status, new_job.assign, new_job.confirm_img_srcs))
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


