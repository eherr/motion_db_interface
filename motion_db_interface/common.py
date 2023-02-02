#!/usr/bin/env python
#
# Copyright 2019 DFKI GmbH.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the
# following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.
import requests
import os
import bson
import json


def save_json_file(data, file_path, indent=4):
    with open(file_path, "w") as out_file:
        return json.dump(data, out_file, indent=indent)


def load_json_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as in_file:
            return json.load(in_file)

def call_rest_interface(url, method, data):
    method_url = url+method
    r = requests.post(method_url, data=json.dumps(data), verify=False)
    return r.text

def call_bson_rest_interface(url, method, data):
    method_url = url+method
    r = requests.post(method_url, data=json.dumps(data), verify=False)
    return r.content



def authenticate(url, user, pw):
    data = {"username": user, "password": pw}
    result_str = call_rest_interface(url, "authenticate", data)
    try:
        result_data = json.loads(result_str)
    except:
        result_data = None
    return result_data


