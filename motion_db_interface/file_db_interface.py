from .common import call_json_rest_interface, call_binary_rest_interface



def get_file_list(url, collection_id, skeleton, data_type=None, tags=None, session=None):
    data = {"collection": collection_id, "skeleton": skeleton}
    if data_type is not None:
        data["dataType"] = data_type
    if tags is not None:
        data["tags"] = tags
    if session is not None:
        data.update(session)
    result_data = call_json_rest_interface(url, "files", data)
    return result_data


def delete_file_by_id(url, file_id, session=None):
    data = {"file_id": file_id}
    if session is not None:
        data.update(session)
    result_data = call_json_rest_interface(url, "files/remove", data)
    return result_data


def upload_file(url, collection, skeleton_name, name, file_data, dataType, config=None, session=None):
    data = {"name": name, "collection": collection, "skeleton": skeleton_name,
            "data": file_data, "dataType":dataType}
    if config is not None:
        data["config"] = config
    if session is not None:
        data.update(session)
    result_data = call_json_rest_interface(url, "files/add", data)
    return result_data
    
def replace_file(url, file_id,  file_data, session=None):
    data = {"file_id": file_id,
            "data": file_data}
    if session is not None:
        data.update(session)
    result_data = call_json_rest_interface(url, "files/replace", data)
    return result_data


def download_file(url, file_id, session=None):
    data = {"file_id": file_id}
    if session is not None:
        data.update(session)
    result_data = call_binary_rest_interface(url, "files/download", data)
    return result_data

def get_data_types(url, tags, session=None):
    data = dict()
    data["tags"] = tags
    return call_json_rest_interface(url, "data_types", data,session)


def get_data_type_info(url, name, session=None):
    data = {"dataType": name}
    return call_json_rest_interface(url, "data_types/info", data, session)

def remove_data_type(url, name, session=None):
    data = {"data_type": name}
    return call_json_rest_interface(url, "data_types/remove", data, session)

def add_data_type(url, name, requirements=None, session=None):
    data = {"name": name}
    if requirements is not None:
        data["requirements"] = requirements
    return call_json_rest_interface(url, "data_types/add", data, session)

def edit_data_type(url, name, data, session=None):
    data["data_type"] = name
    return call_json_rest_interface(url, "data_types/edit", data, session)

def get_data_loaders(url, session=None):
    data = dict()
    return call_json_rest_interface(url, "data_loaders", data, session)

def add_data_loader(url, data_type, engine, script=None, requirements=None, session=None):
    data = {"data_type": data_type, "engine":engine}
    if script is not None:
        data["script"] = script
    if requirements is not None:
        data["requirements"] = requirements
    return call_json_rest_interface(url, "data_loaders/add", data, session)

def edit_data_loader(url, data_type, engine, data, session=None):
    data["data_type"] = data_type
    data["engine"] = engine
    return call_json_rest_interface(url, "data_loaders/edit", data, session)


def remove_data_loader(url, data_type, engine, session=None):
    data = {"data_type": data_type, "engine":engine}
    return call_json_rest_interface(url, "data_loaders/remove", data, session)

def get_data_loader_info(url, data_type, engine, session=None):
    data = {"data_type": data_type, "engine":engine}
    return call_json_rest_interface(url, "data_loaders/info", data, session)

def get_tag_list(url, session=None):
    data = {}
    return call_json_rest_interface(url, "tags", data, session)

def add_tag(url,  tag, session=None):
    data = {"tag":tag}
    return call_json_rest_interface(url, "tags/add", data, session)

def rename_tag(url, old_tag, new_tag, session=None):
    data = {"old_tag":old_tag, "new_tag": new_tag}
    return call_json_rest_interface(url, "tags/rename", data, session)

def remove_tag(url,  tag, session=None):
    data = {"tag":tag}
    return call_json_rest_interface(url, "tags/remove", data, session)

def get_data_type_tags(url, data_type, session=None):
    data = {"data_type": data_type}
    return call_json_rest_interface(url, "data_types/tags", data, session)

def add_data_type_tag(url, data_type, tag, session=None):
    data = {"data_type": data_type, "tag":tag}
    return call_json_rest_interface(url, "data_types/tags", data, session)

def remove_data_type_tag(url, data_type, tag, session=None):
    data = {"data_type": data_type, "tag":tag}
    return call_json_rest_interface(url, "data_loaders/remove", data, session)

def remove_all_data_type_tags(url, data_type, session=None):
    data = {"data_type": data_type}
    return call_json_rest_interface(url, "data_loaders/removeall", data, session)

