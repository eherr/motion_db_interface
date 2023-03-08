from .common import call_json_rest_interface, call_binary_rest_interface



def get_data_transforms(url, session=None):
    data = dict()
    result_data = call_json_rest_interface(url, "data_transforms", data, session)
    return result_data

def get_data_transform_info(url, data_transform_id, session=None):
    data = {"data_transform_id": data_transform_id}
    result_data = call_json_rest_interface(url, "data_transforms/info", data, session)
    return result_data

def remove_data_transform(url, data_transform_id, session=None):
    data = {"data_transform_id": data_transform_id}
    result_data = call_json_rest_interface(url, "data_transforms/remove", data, session)
    return result_data


def add_data_transform(url, name, script, parameters, requirements,  outputType, session=None):
    data = {"name": name, "requirements": requirements, "outputType": outputType,
            "script": script, "parameters":parameters}
    result_data = call_json_rest_interface(url, "data_transforms/add", data, session)
    return result_data

def edit_data_transform(url, data_transform_id, name="", script="", parameters="", requirements="",  outputType="", session=None):
    data = {"data_transform_id":data_transform_id, "name": name, "requirements": requirements, "outputType": outputType,
            "script": script, "parameters":parameters}
    result_data = call_json_rest_interface(url, "data_transforms/edit", data, session)
    return result_data

def get_data_transform_inputs(url, data_transform_id, session=None):
    data = {"data_transform_id":data_transform_id}
    result_data = call_json_rest_interface(url, "data_transforms/inputs", data, session)
    return result_data

def run_data_transform(url, data_transform_id, exp_name, skeleton, output_id, input_data, parameters, store_log, session=None):
    data = dict()
    data["data_transform_id"] = data_transform_id
    data["skeleton_type"] = skeleton
    data["output_id"] = output_id
    data["input_data"] = input_data
    data["exp_name"] = exp_name
    data["store_log"] = store_log
    data["hparams"] = parameters
    result_data = call_json_rest_interface(url, "data_transforms/run", data, session)
    return result_data
    
