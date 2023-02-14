from .common import DBSession

from .model_graph_db_interface import get_graph_list_from_db, create_new_graph_in_db, download_graph_from_remote_db, replace_graph_in_remote_db, delete_graph_from_remote_db


class ModelGraphSession(DBSession):

    def get_graph_list(self, name, loader, requirements):
        return get_graph_list_from_db(self.url, name, loader, requirements, session=self.session)

    def create_new_graph(self):
        return create_new_graph_in_db(self.url, session=self.session)
    
    def replace_graph(self, model_type, data):
        return replace_graph_in_remote_db(self.url, model_type, data, session=self.session)

    def delete_graph(self, model_type):
        return delete_graph_from_remote_db(self.url, model_type, session=self.session)

    def download_graph(self, model_type):
        return download_graph_from_remote_db(self.url, model_type, session=self.session)


