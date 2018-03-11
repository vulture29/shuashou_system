from flask import Flask
from flask import request
from pymongo import MongoClient
from job_util import *

app = Flask(__name__)

db_client = MongoClient()


@app.route('/')
def hello_world():
        return 'Hello, World!'


@app.route('/publish', methods=['POST'])
def publish():
    if request.method == 'POST':
        # TODO: add more vars
        if valid_publish(db_client, request.form['store_id'], request.form['job_id']):
            return "success"
    return "publish fail"


@app.route('/jobs')
def get_job_list():
    job_list = []
    # TODO: json support
    return str(job_list)


@app.route('/take', methods=['POST'])
def take_job():
    if request.method == 'POST':
        if valid_take_job(db_client, request.form['wangwang_id'], request.form['job_id']):
            return "success"
    return "publish fail"


@app.route('/submit', methods=['POST'])
def take_job():
    if request.method == 'POST':
        # TODO: add more vars
        if valid_submit_job(db_client, request.form['wangwang_id'], request.form['job_id']):
            return "success"
    return "publish fail"


@app.route('/add_shuashou', methods=['POST'])
def add_shuashou():
    if request.method == 'POST':
        # TODO: add more vars
        if valid_add_shuashou(db_client, request.form['wangwang_id']):
            return "success"
    return "publish fail"


@app.route('/add_shop_store', methods=['POST'])
def add_shop_store():
    if request.method == 'POST':
        # TODO: add more vars
        if valid_add_shop_store(db_client, request.form['store_id']):
            return "success"
    return "publish fail"
