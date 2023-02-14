
from .common import call_json_rest_interface


def get_graph_list_from_db(url, skeleton, session=None):
    data = {"skeleton":skeleton}
    return call_json_rest_interface(url, "get_graph_list", data, session)

def create_new_graph_in_db(url, name, skeleton, graph_data, session=None):
    data = {"name": name, "skeleton": skeleton, "data": graph_data}
    return call_json_rest_interface(url, "upload_graph", data, session)

def replace_graph_in_remote_db(url, graph_id, name, skeleton, graph_data, session=None):
    data = {"id":graph_id,"name": name, "skeleton": skeleton, "data": graph_data}
    return call_json_rest_interface(url, "replace_graph", data, session)


def delete_graph_from_remote_db(url, graph_id, session=None):
    data = {"id": graph_id}
    return call_json_rest_interface(url, "remove_graph", data, session)


def download_graph_from_remote_db(url, graph_id, session=None):
    data = {"id": graph_id}
    return call_json_rest_interface(url, "download_graph", data, session)


    