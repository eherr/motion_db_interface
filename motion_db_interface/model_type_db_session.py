from .common import DBSession
from .model_type_db_interface import add_model_type, get_model_types, get_model_type_info, remove_model_type, edit_model_type
from .model_type_db_interface import get_model_evaluation_scripts, add_model_evaluation_script, edit_model_evaluation_script, remove_evaluation_script, get_evaluation_script_info


class ModelTypeDBSession(DBSession):

    def add_model_type(self, name, loader, requirements):
        return add_model_type(self.url, name, loader, requirements, session=self.session)

    def get_model_types(self):
        return get_model_types(self.url, session=self.session)
    
    def edit_model_type(self, model_type, data):
        return edit_model_type(self.url, model_type, data, session=self.session)

    def get_model_type_info(self, model_type):
        return get_model_type_info(self.url, model_type, session=self.session)

    def remove_model_type(self, model_type):
        return remove_model_type(self.url, model_type, session=self.session)

    def get_model_evaluation_scripts(self):
        return get_model_evaluation_scripts(self.url, session=self.session)

    def add_model_evaluation_script(self, model_type, engine, data):
        return add_model_evaluation_script(self.url, model_type, engine, data, session=self.session)

    def edit_model_evaluation_script(self, model_type, engine, data):
        return edit_model_evaluation_script(self.url, model_type, engine, data, session=self.session)

    def remove_evaluation_script(self, model_type, engine):
        return remove_evaluation_script(self.url, model_type, engine, session=self.session)

    def get_evaluation_script_info(self, model_type, engine):
        return get_evaluation_script_info(self.url, model_type, engine, session=self.session)


