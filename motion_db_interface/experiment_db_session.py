
import base64
import json
import os
import numpy as np
from .experiment_db_interface import add_experiment, append_experiment_log, get_experiment_log, edit_experiment
from .model_db_interface import upload_model_to_remote_db, replace_model_in_remote_db

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, type):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

class ExperimentDBSession:
    instance = None
    def __init__(self, url="http://localhost:8888/", project_id =1, skeleton_name="mh_cmu", collection_id=1, session_file = "session.json"):
        self.url = url
        self.project_id = project_id
        self.session = None
        self.experiment_id = None
        self.collection_id = collection_id
        self.skeleton_name = skeleton_name
        self.experiment_name = ""
        self.model_id = None
        if os.path.isfile(session_file):
            with open(session_file, "r") as in_file:
                self.session = json.load(in_file)

    @classmethod
    def get_instance(cls, **kwargs):
        if cls.instance is None:
            cls.instance = ExperimentDBSession(**kwargs)
        return cls.instance


    def add_experiment_to_db(self, exp_name, params):
        if self.session is None:
            return
        params = json.dumps(params, cls=CustomEncoder)
        params = json.loads(params)
        result = add_experiment(self.url, exp_name, self.project_id, self.collection_id, self.skeleton_name, params, self.session)
        self.experiment_name = exp_name
        if "id" in result:
            self.experiment_id = result["id"]
        
    def append_log(self, log_entry):
        if self.session is None or self.experiment_id is None:
            print(self.experiment_id, self.session)
            return
        append_experiment_log(self.url, self.experiment_id, log_entry, session=self.session)

    def get_log(self):
        return get_experiment_log(self.url, self.experiment_id)

    def store_model(self, model_data, format="mm"):
        if self.session is None or self.experiment_id is None:
            return
        name = self.experiment_name
        model_data = base64.b64encode(model_data)
        model_data = model_data.decode()
        if self.model_id is None:
            result = upload_model_to_remote_db(self.url, self.collection_id, self.skeleton_name, name, model_data, format=format, session=self.session)
            if result is not None and "id" in result:
                self.model_id = result["id"]
                data = {"model": self.model_id}
                edit_experiment(self.url, self.experiment_id, data, session=self.session)
        else:
            result = replace_model_in_remote_db(self.url, self.model_id, model_data, session=self.session)
            
            
