from .common import DBSession
from .file_db_interface import add_data_type, get_data_types, get_data_type_info, remove_data_type, edit_data_type
from .file_db_interface import get_data_loaders, add_data_loader, edit_data_loader, remove_data_loader, get_data_loader_info
from .file_db_interface import get_file_list, delete_file_by_id, upload_file, upload_file, download_file
from .file_db_interface import get_tag_list, add_tag, rename_tag, remove_tag
from .file_db_interface import get_data_type_tags, add_data_type_tag, remove_data_type_tag, remove_all_data_type_tags


class FileDBSession(DBSession):

    def get_file_list(self, c_id, skeleton, model_format=None, tags=None):
        return get_file_list(self.url, c_id, skeleton, model_format, tags)

    def delete_model(self, file_id):
        return delete_file_by_id(self.url, file_id, self.session)
    
    def delete_file(self, file_id):
        return delete_file_by_id(self.url, file_id, self.session)

    def upload_file(self, name, c_id, skeleton, model_data, dataType, config=None):
        return upload_file(self.url, name, c_id, skeleton, model_data, dataType,config,  self.session)

    def download_file(self, file_id):
        model_data = download_file(self.url, file_id, self.session)
        return model_data
    
    def download_model(self, file_id):
        model_data = download_file(self.url, file_id, self.session)
        return model_data

    def add_data_type(self, name, loader, requirements):
        return add_data_type(self.url, name, loader, requirements, session=self.session)

    def get_data_types(self):
        return get_data_types(self.url, session=self.session)
    
    def edit_data_type(self, data_type, data):
        return edit_data_type(self.url, data_type, data, session=self.session)

    def get_data_type_info(self, data_type):
        return get_data_type_info(self.url, data_type, session=self.session)

    def remove_data_type(self, data_type):
        return remove_data_type(self.url, data_type, session=self.session)

    def get_data_loaders(self):
        return get_data_loaders(self.url, session=self.session)

    def add_data_loader(self, data_type, engine, data):
        return add_data_loader(self.url, data_type, engine, data, session=self.session)

    def edit_data_loader(self, data_type, engine, data):
        return edit_data_loader(self.url, data_type, engine, data, session=self.session)

    def remove_data_loader(self, data_type, engine):
        return remove_data_loader(self.url, data_type, engine, session=self.session)

    def get_data_loader_info(self, data_type, engine):
        return get_data_loader_info(self.url, data_type, engine, session=self.session)

    def get_tag_list(self):
        return get_tag_list(self.url, session=self.session)
    
    def add_tag(self, tag):
        return add_tag(self.url, tag, session=self.session)

    def rename_tag(self, old_tag, new_tag):
        return rename_tag(self.url, old_tag, new_tag, session=self.session)
    
    def remove_tag(self, tag):
        return remove_tag(self.url, tag, session=self.session)
    
    def get_data_type_tags(self, data_type):
        return get_data_type_tags(self.url, data_type, session=self.session)
    
    def add_data_type_tag(self, data_type, tag):
        return add_data_type_tag(self.url, data_type, tag, session=self.session)
   
    def remove_data_type_tag(self, data_type, tag):
        return remove_data_type_tag(self.url, data_type, tag, session=self.session)
    
    def remove_data_type_tags(self, data_type):
        return remove_all_data_type_tags(self.url, data_type, session=self.session)


