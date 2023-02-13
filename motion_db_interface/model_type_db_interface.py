from .common import call_json_rest_interface


def get_model_types(url, session=None):
    data = dict()
    return call_json_rest_interface(url, "model_types", data,session)


def get_model_type_info(url, name, session=None):
    data = {"model_type": name}
    return call_json_rest_interface(url, "model_types/info", data, session)

def remove_model_type(url, name, session=None):
    data = {"model_type": name}
    return call_json_rest_interface(url, "model_types/remove", data, session)

def add_model_type(url, name, requirements=None, session=None):
    data = {"name": name}
    if requirements is not None:
        data["requirements"] = requirements
    return call_json_rest_interface(url, "model_types/add", data, session)

def edit_model_type(url, name, data, session=None):
    data["model_type"] = name
    return call_json_rest_interface(url, "model_types/edit", data, session)

def get_model_evaluation_scripts(url, session=None):
    data = dict()
    return call_json_rest_interface(url, "eval_scripts", data, session)

def add_model_evaluation_script(url, model_type, engine, script=None, requirements=None, session=None):
    data = {"model_type": model_type, "engine":engine}
    if script is not None:
        data["script"] = script
    if requirements is not None:
        data["requirements"] = requirements
    return call_json_rest_interface(url, "eval_scripts/add", data, session)

def edit_model_evaluation_script(url, model_type, engine, data, session=None):
    data["model_type"] = model_type
    data["engine"] = engine
    return call_json_rest_interface(url, "eval_scripts/edit", data, session)


def remove_evaluation_script(url, model_type, engine, session=None):
    data = {"model_type": model_type, "engine":engine}
    return call_json_rest_interface(url, "eval_scripts/remove", data, session)

def get_evaluation_script_info(url, model_type, engine, session=None):
    data = {"model_type": model_type, "engine":engine}
    return call_json_rest_interface(url, "eval_scripts/info", data, session)
