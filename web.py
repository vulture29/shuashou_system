from flask import Flask
from flask import request
import sqlite3
from job_util import *
from shuashou import Shuashou
from job import Job
from shop_store import ShopStore

app = Flask(__name__)

conn = sqlite3.connect('job_database.db')

@app.route('/')
def hello_world():
        return 'Hello, World!'


@app.route('/jobs', methods=['GET'])
def job_list():
    job_list = get_job_list(conn)
    # TODO: json support
    return str(job_list)


@app.route('/take', methods=['POST'])
def take_job():
    if request.method == 'POST':
        if valid_take_job(conn, request.form['wangwang_id'], request.form['job_id']):
            return "success"
    return "take job fail"


@app.route('/submit', methods=['POST'])
def submit_job():
    if request.method == 'POST':
        # TODO: add more vars
        if valid_submit_job(conn, request.form['wangwang_id'], request.form['job_id']):
            return "success"
    return "submit job fail"


@app.route('/publish', methods=['POST'])
def publish_job():
    if request.method == 'POST':
        # TODO: add more vars
        new_job = Job()
        new_job.store_id = request.form['store_id']
        new_job.job_id = "job_id"
        if valid_publish(conn, new_job):
            return "success"
    return "publish fail"


@app.route('/add_shuashou', methods=['POST'])
def add_shuashou():
    if request.method == 'POST':
        # TODO: add more vars
        new_shuashou = Shuashou()
        new_shuashou.wangwang_id = request.form['wangwang_id']
        if valid_add_shuashou(conn, new_shuashou):
            return "success"
    return "add shuashou fail"


@app.route('/add_shop_store', methods=['POST'])
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