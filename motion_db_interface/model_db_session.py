from .motion_db_session import MotionDBSession
from .file_db_session import FileDBSession
from .model_graph_db_session import ModelGraphSession
from .model_db_interface import get_model_list_from_remote_db,upload_model_to_remote_db, download_model_from_remote_db, \
                                        delete_model_by_id_from_remote_db

from .experiment_db_interface import get_experiment_list, get_experiment_log, remove_experiment

class ModelDBSession(MotionDBSession, FileDBSession, ModelGraphSession):

    def get_model_list(self, c_id, skeleton, model_format=None):
        return get_model_list_from_remote_db(self.url, c_id, skeleton, model_format)

    def delete_model(self, model_id):
        return delete_model_by_id_from_remote_db(self.url, model_id, self.session)

    def upload_model(self, name, c_id, skeleton, model_data, model_format, config=None):
        return upload_model_to_remote_db(self.url, name, c_id, skeleton, model_data, config, model_format, self.session)

    def download_model(self, model_id):
        model_data = download_model_from_remote_db(self.url, model_id, self.session)
        return model_data

    def get_experiment_list(self, collection_id, skeleton):
        return get_experiment_list(self.url, collection_id, skeleton)

    def get_experiment_log(self, experiment_id):
        return get_experiment_log(self.url, experiment_id, self.session)

    def remove_experiment(self, experiment_id):
        return remove_experiment(self.url, experiment_id, self.session)