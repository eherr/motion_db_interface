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
import bson
import bz2
from .common import call_bson_rest_interface, call_binary_rest_interface, call_json_rest_interface




def upload_motion_model_to_remote_db(url, name, collection, skeleton_name, model_data, config, session=None):
    data = {"name":name, "collection": collection, "skeleton_name": skeleton_name,
            "data": model_data, "config": config, "format":"mm"}
    return call_json_rest_interface(url, "upload_motion_model", data, session)


def download_motion_model_from_remote_db(url, model_id, session=None):
    data = {"model_id": model_id}
    result_str= call_binary_rest_interface(url, "download_motion_model", data, session)
    try:
        result_str = bz2.decompress(result_str)
        result_data = bson.loads(result_str)
    except:
        print("exception")
        result_data = None
    return result_data

def upload_cluster_tree_to_remote_db(url, model_id, cluster_tree_data, session=None):
    data = {"model_id": model_id, "cluster_tree_data": cluster_tree_data}
    return call_json_rest_interface(url, "upload_cluster_tree", data, session)

def download_cluster_tree_from_remote_db(url, model_id, session=None):
    data = {"model_id": model_id}
    result_str= call_binary_rest_interface(url, "download_cluster_tree", data, session)
    try:
        result_str = bz2.decompress(result_str)
        result_data = bson.loads(result_str)
    except:
        print("exception")
        result_data = None
    return result_data
