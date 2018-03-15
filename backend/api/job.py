from json import *

default_str = "default"


class Job:
    def __init__(self):
        self.job_id = default_str
        self.item_id = default_str
        self.store_id = default_str
        self.main_img_src = default_str
        self.tao_key = default_str
        self.keyword = default_str
        self.compare_img_src = default_str
        self.sku = default_str
        self.pay_amount = default_str
        self.task_amount = default_str
        self.chat_questions = default_str
        self.comments = default_str
        self.comment_img_src = default_str
        self.salary = default_str
        self.status = "published"
        self.assign = default_str

    def get_map(self):
        job_map = {}
        job_map["job_id"] = self.job_id
        job_map["item_id"] = self.item_id
        job_map["store_id"] = self.store_id
        job_map["main_img_src"] = self.main_img_src
        job_map["tao_key"] = self.tao_key
        job_map["keyword"] = self.keyword
        job_map["compare_img_src"] = self.compare_img_src
        job_map["sku"] = self.sku
        job_map["pay_amount"] = self.pay_amount
        job_map["task_amount"] = self.task_amount
        job_map["chat_questions"] = self.chat_questions
        job_map["comments"] = self.comments
        job_map["comment_img_src"] = self.comment_img_src
        job_map["salary"] = self.salary
        job_map["status"] = self.status
        job_map["assign"] = self.assign
        return job_map
