from .add_project import handle_add_new_project
def register_actions(app):
    app.action("project_add_new_project_charachter_change_action")(handle_add_new_project)