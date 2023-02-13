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
from .common import call_json_rest_interface


def get_project_list(url, session=None):
    data = dict()
    return call_json_rest_interface(url, "projects", data, session)

def get_project_info(url, project_id, session=None):
    data = dict()
    data["project_id"] = project_id
    return call_json_rest_interface(url, "projects/info", data, session)

def add_new_project(url, name, is_public, session=None):
    data = dict()
    data["name"] = name
    data["is_public"] = is_public
    return call_json_rest_interface(url, "projects/add", data, session)

def edit_project(url, project_id, name, is_public, session=None):
    data = dict()
    data["project_id"] = project_id
    data["name"] = name
    data["is_public"] = is_public
    return call_json_rest_interface(url, "projects/edit", data, session)

def remove_project(url, project_id, session=None):
    data = dict()
    data["project_id"] = project_id
    return call_json_rest_interface(url, "projects/remove", data, session)
