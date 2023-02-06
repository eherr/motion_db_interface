import json
from .common import call_rest_interface

def add_experiment(url, name, project, collection, skeleton_name, config, session=None):
    #part_data = bytearray(part, "utf-8")
    data = {"name": name, 
            "skeleton": skeleton_name,
            "project": project,
            "collection": collection,
            "config": config}
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "experiments/add", data)
    try:
        result_data = json.loads(result_str)
    except:
        result_data = None
    return result_data

def get_experiment_list(url, collection_id, skeleton=None, session=None):
    data = {"collection": collection_id}
    if skeleton is not None:
        data["skeleton"] = skeleton
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "experiments", data)
    try:
        result_data = json.loads(result_str)
    except:
        result_data = None
    return result_data

def edit_experiment(url, experiment_id, data, session=None):
    data["experiment_id"] = experiment_id
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "experiments/edit", data)
    return result_str

def remove_experiment(url, experiment_id, session=None):
    data = {"experiment_id": experiment_id}
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "experiments/remove", data)
    return result_str

def get_experiment_info(url, experiment_id, session=None):
    data = {"experiment_id": experiment_id}
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "experiments/info", data)
    return result_str

def append_experiment_log(url, experiment_id, log_entry, session=None):
    data = {"experiment_id": experiment_id, "log_entry":log_entry}
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "experiments/append_log", data)
    return result_str

def get_experiment_log(url, experiment_id, session=None):
    data = {"experiment_id": experiment_id}
    if session is not None:
        data.update(session)
    result_str = call_rest_interface(url, "experiments/log", data)
    result_data = json.loads(result_str)
    return result_data

