
from .project_db_interface import get_project_list, get_project_info, add_new_project, edit_project, remove_project

class ProjectDBSession:
    def __init__(self, db_url, session):
        self.url = db_url
        self.session = session

    def get_project_list(self):
        return get_project_list(self.url, session=self.session)

    def get_project_info(self, project_id):
        return get_project_info(self.url, project_id, session=self.session)

    def add_new_project(self, name, is_public):
        return add_new_project(self.url, name, is_public, self.session)
        
    def edit_project(self, project_id, name, is_public):
        return edit_project(self.url, project_id, name, is_public, self.session)

    def remove_project(self, project_id):
        return remove_project(self.url, project_id, self.session)
