import json
from .common import call_json_rest_interface

def add_experiment(url, name, project, collection, skeleton_name, config, session=None):
    #part_data = bytearray(part, "utf-8")
    data = {"name": name, 
            "skeleton": skeleton_name,
            "project": project,
            "collection": collection,
            "config": config}
    return call_json_rest_interface(url, "experiments/add", data, session)

def get_experiment_list(url, collection_id, skeleton=None, session=None):
    data = {"collection": collection_id}
    if skeleton is not None:
        data["skeleton"] = skeleton
    return call_json_rest_interface(url, "experiments", data, session)

def edit_experiment(url, experiment_id, data, session=None):
    data["experiment_id"] = experiment_id
    if session is not None:
        data.update(session)
    return call_json_rest_interface(url, "experiments/edit", data)

def remove_experiment(url, experiment_id, session=None):
    data = {"experiment_id": experiment_id}
    return call_json_rest_interface(url, "experiments/remove", data, session)

def get_experiment_info(url, experiment_id, session=None):
    data = {"experiment_id": experiment_id}
    return call_json_rest_interface(url, "experiments/info", data, session)

def append_experiment_log(url, experiment_id, log_entry, session=None):
    data = {"experiment_id": experiment_id, "log_entry":log_entry}
    return call_json_rest_interface(url, "experiments/append_log", data, session)

def get_experiment_log(url, experiment_id, session=None):
    data = {"experiment_id": experiment_id}
    return call_json_rest_interface(url, "experiments/log", data, session)

