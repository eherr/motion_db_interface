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
"""
Created on Mon Jun 20 2017

@author: Erik Herrmann
"""
import json
from .common import call_bson_rest_interface, call_rest_interface, call_binary_rest_interface



def get_model_list_from_remote_db(url, collection_id, skeleton, model_format=None, session=None):
    data = {"collection": collection_id, "skeleton": skeleton}
    if model_format is not None:
        data["format"] = model_format
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "models", data)
    try:
        result_data = json.loads(result_str)
    except:
        result_data = None
    return result_data


def delete_model_by_id_from_remote_db(url, model_id, session=None):
    data = {"model_id": model_id}
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "delete_model", data)
    try:
        result_data = json.loads(result_str)
    except:
        result_data = None
    return result_data


def upload_model_to_remote_db(url, collection, skeleton_name, name, model_data, model_format, config=None, session=None):
    data = {"name": name, "collection": collection, "skeleton": skeleton_name,
            "data": model_data, "format":model_format}
    if config is not None:
        data["config"] = config
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "models/add", data)
    try:
        result_data = json.loads(result_str)
    except:
        result_data = None
    return result_data
    
def replace_model_in_remote_db(url, model_id,  model_data, session=None):
    data = {"model_id": model_id,
            "data": model_data}
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "models/replace", data)
    try:
        result_data = json.loads(result_str)
    except:
        result_data = None
    return result_data


def download_model_from_remote_db(url, model_id, session=None):
    data = {"model_id": model_id}
    if session is not None:
        data.update(session)
    result_data = call_binary_rest_interface(url, "models/download", data)
    return result_data