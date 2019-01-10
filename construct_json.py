import json
from peronal_info import *


upload_to = 'json_files/personal_info.json'
data = [{
        "first_name": FIRST_NAME,
        "last_name": LAST_NAME,
        "age": AGE,
        "address": ADDRESS,
        "phone": PHONE,
        "email": EMAIL,
        "profession": PROFESSION,
        "work_at": WORK_AT
    },
]

def upload_data(upload_to, data):
    with open(upload_to, 'w') as f_obj:
        json.dump(data, f_obj)

upload_data(upload_to, data)

