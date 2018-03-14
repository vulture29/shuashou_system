from flask import Flask
from flask import request
from flask import render_template
import sqlite3
from api.job_util import *
from api.shuashou import Shuashou
from api.job import Job
from api.shop_store import ShopStore
import uuid

app = Flask(__name__)

conn = sqlite3.connect('job_database.db')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/jobs')
def render_job_list():
    return render_template('job.html')


@app.route('/api/v1/jobs', methods=['GET'])
def get_job_list():
    job_list = retrieve_job_list(conn)
    job_list_str = [str(job) for job in job_list]
    return str(job_list_str)


@app.route('/api/v1/userjobs', methods=['GET'])
def get_user_job_list():
    wangwang_id = request.args.get('wangwang_id')
    job_list = retrieve_user_job_list(conn, wangwang_id)
    job_list_str = [str(job) for job in job_list]
    return str(job_list_str)


@app.route('/api/v1/take', methods=['POST'])
def take_job():
    if request.method == 'POST':
        if valid_take_job(conn, request.form['wangwang_id'], request.form['job_id']):
            return "success"
    return "take job fail"


@app.route('/api/v1/submit', methods=['POST'])
def submit_job():
    if request.method == 'POST':
        # TODO: add more vars
        confirm_img_srcs = [request.form['confirm_img_src']]
        if valid_submit_job(conn, request.form['wangwang_id'], request.form['job_id'], confirm_img_srcs):
            return "success"
    return "submit job fail"


@app.route('/api/v1/approve', methods=['POST'])
def approve_job():
    if request.method == 'POST':
        # TODO: add more vars
        if valid_approve_job(conn, request.form['wangwang_id'], request.form['job_id']):
            return "success"
    return "submit job fail"


@app.route('/api/v1/publish', methods=['POST'])
def publish_job():
    if request.method == 'POST':
        # TODO: add more vars
        new_job = Job()
        new_job.store_id = request.form['store_id']
        new_job.item_id = request.form['item_id']
        new_job.job_id = str(uuid.uuid4())
        if valid_publish(conn, new_job):
            return "success"
    return "publish fail"


@app.route('/api/v1/add_shuashou', methods=['POST'])
def add_shuashou():
    if request.method == 'POST':
        # TODO: add more vars
        new_shuashou = Shuashou()
        new_shuashou.wangwang_id = request.form['wangwang_id']
        if valid_add_shuashou(conn, new_shuashou):
            return "success"
    return "add shuashou fail"


@app.route('/api/v1/add_shop_store', methods=['POST'])
def add_shop_store():
    if request.method == 'POST':
        # TODO: add more vars
        new_shop_store = ShopStore()
        new_shop_store.store_id = request.form['store_id']
        if valid_add_shop_store(conn, new_shop_store):
            return "success"
    return "add shop fail"


if __name__ == '__main__':
    app.run()