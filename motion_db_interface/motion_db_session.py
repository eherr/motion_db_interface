
import os
import json
import glob
import collections
from anim_utils.animation_data import MotionVector
from .skeleton_db_interface import get_skeleton_model_from_remote_db, delete_skeleton_from_remote_db, replace_skeleton_in_remote_db, get_skeletons_from_remote_db, create_new_skeleton_in_db, load_skeleton_from_db, get_skeleton_from_remote_db
from .motion_db_interface import delete_motion_by_id_from_remote_db, replace_motion_in_db,get_collections_tree_by_parent_id_from_remote_db, create_new_collection_in_remote_db, replace_collection_in_remote_db, delete_collection_from_remote_db, get_collections_by_parent_id_from_remote_db, upload_motion_to_db, get_bvh_string, get_motion_list_from_remote_db, get_motion_by_id_from_remote_db, get_annotation_by_id_from_remote_db, get_time_function_by_id_from_remote_db
from .project_db_session import ProjectDBSession


def create_sections_from_annotation(annotations):
    motion_sections = dict()
    for label in annotations:
        annotations[label].sort()
        section = dict()
        section["start_idx"] = annotations[label][0]
        section["end_idx"] = annotations[label][-1]
        motion_sections[section["start_idx"]] = section
    return list(collections.OrderedDict(sorted(motion_sections.items())).values())


def read_annotation_file(annotation_filepath):
    meta_info_str = ""
    with open(annotation_filepath, "rt") as annotation_file:
        print("read meta info from", annotation_filepath)
        annotation_str = annotation_file.read()
        annotation_data = json.loads(annotation_str)
        meta_info_data = dict()
        meta_info_data["sections"] = create_sections_from_annotation(annotation_data["semantic_annotation"])
        meta_info_str = json.dumps(meta_info_data)
    return meta_info_str


def load_bvh_with_annotations(directory, skeleton_model="custom"):
    data = collections.OrderedDict()
    for filename in glob.glob(directory+os.sep+"*.bvh"):
        name = filename.split(os.sep)[-1]
        bvh_str = None
        with open(filename, "rt") as in_file:
            print("read", filename)
            bvh_str = in_file.read()
        if bvh_str is not None:
            meta_info_str = ""
            #check for annoation
            annotation_file_option1 = filename[:-4]+"_section.json"
            annotation_file_option2 = filename[:-4]+"_sections.json"
            meta_info_file = filename+"_meta_info.json"
            if os.path.isfile(annotation_file_option1):
                meta_info_str = read_annotation_file(annotation_file_option1)
            elif os.path.isfile(annotation_file_option2):
                meta_info_str = read_annotation_file(annotation_file_option2)
            elif os.path.isfile(meta_info_file):
                with open(meta_info_file, "rt") as meta_info_file:
                    meta_info_str = meta_info_file.read()
            else:
                print("Did not find meta info for", filename)
                meta_info_str = ""
            data[name] = dict()
            data[name]["meta_info"] = meta_info_str
            data[name]["bvh_str"] = bvh_str
            data[name]["skeleton_model"] = skeleton_model
            
    return data


def load_bvh_with_keyframes(directory, skeleton_model="custom"):
    data = collections.OrderedDict()
    keyframe_file_name = directory+os.sep+"keyframes.json"
    with open(keyframe_file_name, "rt") as keyframe_file:
        keyframe_str = keyframe_file.read()
        keyframe_data = json.loads(keyframe_str)
    print("found keyframes", keyframe_data.keys())
    for filename in glob.glob(directory+os.sep+"*.bvh"):
        name = filename.split(os.sep)[-1]
        with open(filename, "rt") as in_file:
            print("read", filename)

            bvh_str = in_file.read()
            
            key = name[:-4]
            if key in keyframe_data:
                meta_info_data = dict()
                meta_info_data["sections"] = []
                section = dict()
                section["start_idx"] = 0
                section["end_idx"] = keyframe_data[key]
                meta_info_data["sections"].append(section)
                section = dict()
                section["start_idx"] = keyframe_data[key]
                section["end_idx"] = -1
                meta_info_data["sections"].append(section)
                meta_info_str = json.dumps(meta_info_data)
            else:
                meta_info_str = ""


            data[name] = dict()
            data[name]["meta_info"] = meta_info_str
            data[name]["bvh_str"] = bvh_str
            data[name]["skeleton_model"] = skeleton_model
    return data


def load_motion_data_from_dir(directory, skeleton_model="custom"):
    if os.path.isfile(directory+os.sep+"keyframes.json"):
        data = load_bvh_with_keyframes(directory, skeleton_model)
    else:
        data = load_bvh_with_annotations(directory, skeleton_model)
    return data

class MotionDBSession(ProjectDBSession):

    def get_collection_id_from_path(self, collection_path):
        """Return the ID corresponding to the collection at the path

        Args:
            collection_path (str): a string separated by "/", e.g. INTERACT/walk/left_step

        Returns:
            int: ID of collection
        """
        name_list = collection_path.split("/")
        tree = get_collections_tree_by_parent_id_from_remote_db(self.url,0, self.session)
        collection_id = self.traverse_tree_by_names(tree, 0, name_list)
        print("found", collection_id, "using", name_list)
        return collection_id

    def traverse_tree_by_names(self, tree, parent_id, name_list, query_idx=0):
        match_id = None
        if query_idx < len(name_list):
            for c in tree:
                if tree[c]["name"] == name_list[query_idx]:
                    match_id = c
                    break
        if match_id is not None:
            return self.traverse_tree_by_names(tree[match_id]["sub_tree"], match_id,  name_list, query_idx+1)
        else:
            return parent_id
    

    def create_new_collection(self,name, col_type, c_id, owner):
        return create_new_collection_in_remote_db(self.url, name, col_type, c_id, owner, self.session)

    def replace_collection(self,c_id, name, col_type, p_id, owner):
        return replace_collection_in_remote_db(self.url, c_id, name, col_type, p_id, owner, self.session)

    def delete_collection(self, c_id):
        return delete_collection_from_remote_db(self.url, c_id, self.session)

    def create_new_skeleton(self,name, data, meta_data):
        return create_new_skeleton_in_db(self.url, name, data, meta_data, self.session)

    def get_collections_tree(self, parent_id):
        return get_collections_tree_by_parent_id_from_remote_db(self.url, parent_id)

    def get_skeleton_list(self):
        return get_skeletons_from_remote_db(self.url)

    def load_skeleton(self, skeleton_name):
        return load_skeleton_from_db(self.url, skeleton_name, self.session)

    def get_skeleton_data(self, skeleton_name):
        return get_skeleton_from_remote_db(self.url, skeleton_name)

    def get_skeleton_meta_data(self, skeleton_name):
        return get_skeleton_model_from_remote_db(self.url, skeleton_name)

    def replace_skeleton(self, name, data, meta_data):
        return replace_skeleton_in_remote_db(self.url, name, data, meta_data, self.session)

    def delete_skeleton(self, skeleton_name):
        return delete_skeleton_from_remote_db(self.url, skeleton_name, self.session)

    def get_motion_list(self, collection_id, skeleton_name, is_processed=False):
        return get_motion_list_from_remote_db(self.url, collection_id, skeleton_name, is_processed=is_processed, session=self.session)

    def get_motion_data(self, motion_id, is_processed=False):
        return get_motion_by_id_from_remote_db(self.url, motion_id, is_processed, session=self.session)

    def get_motion_meta_data(self, motion_id, is_processed):
        return get_annotation_by_id_from_remote_db(self.url, motion_id, is_processed, session=self.session)

    def replace_motion(self, motion_id, motion_name, data, collection, skeleton_name, meta_data, is_processed):
        return replace_motion_in_db(self.url, motion_id, motion_name, data, collection, 
                            skeleton_name, meta_data, is_processed=is_processed, session=self.session)

    def delete_motion(self, motion_id, is_processed=False):
        return delete_motion_by_id_from_remote_db(self.url, motion_id, is_processed, self.session)

    def upload_motion(self, motion_name, motion_data, collection, skeleton_model_name, meta_info_str):
        return upload_motion_to_db(self.url, motion_name, motion_data, collection, skeleton_model_name, meta_info_str, session=self.session)

    def copy_motion_in_db(self, motion_id, motion_name, collection, skeleton_model_name, is_processed=False):
        motion_data = self.get_motion_data(motion_id, is_processed)
        if motion_data is None:
            print("Error: motion data is empty")
            return
        meta_info_str = self.get_motion_meta_data(motion_id, is_processed)
        return self.upload_motion(motion_name, motion_data, collection, skeleton_model_name, meta_info_str)
        
    def export_raw_motion_data(self, skeleton_name, out_dir, parent=0, model_filter=None):
        for col in get_collections_by_parent_id_from_remote_db(self.url, parent):
            print(col)
            col_id, col_name, col_type, owner = col
            action_dir = out_dir+os.sep+col_name
            if model_filter is None or col_name in model_filter:
                self.export_collection_clips_to_folder(col_id, skeleton_name, action_dir, is_aligned=0)
            self.export_raw_motion_data(skeleton_name, action_dir, col_id)
    

    def export_processed_motion_data(self, skeleton_name, out_dir, parent=0, model_filter=None):
        for col in get_collections_by_parent_id_from_remote_db(self.url, parent):
            print(col)
            col_id, col_name, col_type, owner = col
            action_dir = out_dir+os.sep+col_name
            if model_filter is None or col_name in model_filter:
                self.export_collection_clips_to_folder(col_id, skeleton_name, action_dir, is_aligned=1)
            self.export_processed_motion_data(skeleton_name, action_dir, col_id)


    def export_collection_clips_to_folder(self, c_id, skeleton_name, directory, is_processed):
        print("export", is_processed)
        #is_aligned = 1
        skeleton = self.load_skeleton(skeleton_name)
        joint_count = 0
        for joint_name in skeleton.nodes.keys():
            if len(skeleton.nodes[joint_name].children) > 0 and "EndSite" not in joint_name:
                joint_count+=1
        skeleton.reference_frame_length = joint_count * 4 + 3

        motion_list = get_motion_list_from_remote_db(self.url, c_id, skeleton_name, is_processed, self.session)
        if motion_list is None:
            print("could not find motions")
            return
        n_motions = len(motion_list)
        if n_motions < 1:
            print("no motions", c_id)
            return
        if not os.path.isdir(directory):
            os.makedirs(directory)
        count = 1
        #print(skeleton_name, len(motion_list), is_aligned, directory)
        for motion_id, name in motion_list:
            print("download motion", str(count)+"/"+str(n_motions), name, is_processed)
            self.export_motion_clip(skeleton, motion_id, name, directory, is_processed, export_bvh=True)
            count+=1

    
    def export_motion_clip(self, skeleton, motion_id, name, directory, is_processed, export_bvh=True):
        print("export clip")
        motion_data = self.get_motion_data(motion_id, is_processed=is_processed)
        if motion_data is None:
            return
        print("write to file")
        filename = directory+os.sep+name
        
        print("ref frame length",skeleton.reference_frame_length)
        if export_bvh:
            motion_vector = MotionVector()
            motion_vector.from_custom_db_format(motion_data)
            print("loaded",name, motion_vector.frames.shape)
            frames = motion_vector.frames
            if motion_vector.frames.shape[1] < skeleton.reference_frame_length:
                frames = skeleton.add_fixed_joint_parameters_to_motion(frames)
            motion_str = get_bvh_string(skeleton, frames)
            if not name.endswith(".bvh"):
                filename += ".bvh"
        else:
            motion_str = json.dumps(motion_data)
        with open(filename, "wt") as out_file:
             out_file.write(motion_str)
            
        filename = directory+os.sep+name
        annotation_str = get_annotation_by_id_from_remote_db(self.url, motion_id, is_processed=False, session=self.session)
        if annotation_str != "":
            annotation_filename = filename + "_meta_info.json"
            with open(annotation_filename, "wt") as out_file:
                out_file.write(annotation_str)
        else:
            print("no meta info")
        time_function_str = get_time_function_by_id_from_remote_db(self.url, motion_id, self.session)
        if time_function_str != "":
            time_function_filename = filename + "_time_function.json"
            with open(time_function_filename, "wt") as out_file:
                out_file.write(time_function_str)
        else:
            print("no time function")


    def import_collection_from_directory(self, collection_id, directory):
        motion_data_list = load_motion_data_from_dir(directory)
        count = 1
        n_motions = len(motion_data_list)
        for name, data in motion_data_list.items():
            print("upload motion", str(count)+"/"+str(n_motions), name)
            is_processed = False
            motion_data = data["bvh_str"]
            upload_motion_to_db(self.url, name, motion_data, collection_id, data["skeleton_model"], data["meta_info"], is_processed, self.session)
            count+=1
