import numpy as np
import os
import json
from .common import save_json_file
from .motion_db_interface import get_collections_by_parent_id_from_remote_db
from .model_db_session import ModelDBSession, get_model_list_from_remote_db
from .mg_model_db_interface import download_motion_model_from_remote_db, \
                                         upload_cluster_tree_to_remote_db, \
                                        download_cluster_tree_from_remote_db


class MGModelDBSession(ModelDBSession):

    def download_motion_model(self, model_id):
        model_data = download_motion_model_from_remote_db(self.url, model_id, self.session)
        return model_data

    def download_cluster_tree(self, model_id):
        meta_data = download_cluster_tree_from_remote_db(self.url, model_id, self.session)
        return meta_data

    def upload_cluster_tree(self, model_id, meta_data):
        return upload_cluster_tree_to_remote_db(self.url, model_id, meta_data, self.session)

    def export_database_of_skeleton_to_directory(self, directory, skeleton_name):
        skeleton_dir = directory+os.sep+skeleton_name
        if not os.path.isdir(skeleton_dir):
            os.makedirs(skeleton_dir)
        skeleton_data = self.get_skeleton_data(skeleton_name)
        save_json_file(skeleton_data, skeleton_dir + os.sep + skeleton_name+"_skeleton.json")
        
        self.export_raw_motion_data(skeleton_name, skeleton_dir + os.sep + "raw")
        self.export_processed_motion_data(skeleton_name, skeleton_dir + os.sep + "processed")
        self.export_motion_models(skeleton_name, skeleton_dir + os.sep + "models")

    def export_motion_models(self, skeleton_name, out_dir, parent=0):
        for col in get_collections_by_parent_id_from_remote_db(self.url, parent, self.session):
            col_id, col_name, col_type, owner = col
            action_dir = out_dir+os.sep+col_name
            self.export_motion_primitive_models(col_id, skeleton_name, action_dir)
            self.export_motion_models(skeleton_name, action_dir, col_id)
  
    def export_motion_primitive_models(self, mp_name, skeleton_name, out_dir):
        model_list = get_model_list_from_remote_db(self.url, mp_name, skeleton_name, self.session)
        if len(model_list) > 0 and not os.path.isdir(out_dir):
            os.makedirs(out_dir)
        for model_id, name in model_list:
            model_data = download_motion_model_from_remote_db(self.url, model_id, self.session)
            with open(out_dir+ os.sep + name + "_quaternion_mm.json", "w+") as out_file:
                out_file.write(json.dumps(model_data))
            cluster_tree_data = download_cluster_tree_from_remote_db(self.url, model_id, self.session)
            if cluster_tree_data is not None:
                with open(out_dir+ os.sep + name + "_cluster_tree.json", "w+") as out_file:
                    out_file.write(json.dumps(cluster_tree_data))
