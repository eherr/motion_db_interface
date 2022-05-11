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
import json
from anim_utils.animation_data import SkeletonBuilder
from .common import call_bson_rest_interface, call_rest_interface


def get_skeleton_from_remote_db(url, skeleton_type, session=None):
    data = {"skeleton_type": skeleton_type}
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "get_skeleton", data)
    try:
        result_data = json.loads(result_str)
    except:
        result_data = None
    return result_data


def get_skeleton_model_from_remote_db(url, skeleton_type, session=None):
    data = {"skeleton_type": skeleton_type}
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "get_skeleton_model", data)
    try:
        result_data = json.loads(result_str)
    except:
        result_data = None
    return result_data


def get_skeletons_from_remote_db(url, session=None):
    data = {}
    result_str = call_rest_interface(url, "get_skeleton_list", data)
    try:
        result_data = json.loads(result_str)
    except:
        result_data = None
    return result_data


def create_new_skeleton_in_db(url, name, skeleton_data, meta_data, session=None):
    data = {"name": name, "data": skeleton_data}
    if meta_data is not None:
        data["meta_data"] = meta_data
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "create_new_skeleton", data)


def replace_skeleton_in_remote_db(url, name, skeleton_data, meta_data, session=None):
    data = dict()
    data["name"] = name
    if skeleton_data is not None:
        data["data"] = skeleton_data
    if meta_data is not None:
        data["meta_data"] = meta_data
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "replace_skeleton", data)


def delete_skeleton_from_remote_db(url, name, session=None):
    data = {"name": name}
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "remove_skeleton", data)


def load_skeleton_from_db(db_url, skeleton_name, session=None):
    skeleton_data = get_skeleton_from_remote_db(db_url, skeleton_name, session)
    if skeleton_data is not None:
        skeleton = SkeletonBuilder().load_from_custom_unity_format(skeleton_data)
        skeleton_model = get_skeleton_model_from_remote_db(db_url, skeleton_name, session)
        skeleton.skeleton_model = skeleton_model
        return skeleton
