from .add_project import handle_add_new_project, handle_view_submission_events
def register_actions(app):
    app.action("project_add_new_project_charachter_change_action")(handle_add_new_project)
    app.view("project_add_new_project_submission_callback")(handle_view_submission_events)