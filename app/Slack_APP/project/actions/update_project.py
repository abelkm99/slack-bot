
from app.models.project import Project
from app.Slack_APP.project.views import project_updated_succesfully_view


def handle_view_submission_update_project(ack, body, logger, context):
    context['flask_app'].app_context().push()
    logger.debug(body)
    prev_project_name = body['view']['state']['values']['project_update_project_selected_project_block']['static_select-action']['selected_option']['value']
    new_project_name = body['view']['state']['values']['project_update_project_input_block']['project_update_project_new_project_name']['value']
    new_project_name = new_project_name.strip().capitalize()

    if prev_project_name == new_project_name:
        ack({
            "response_action": "errors",
            "errors": {
                "project_update_project_input_block": "the previous project \
                        name and the new project name can't be the same"
            }
        })
    project = Project.query.filter_by(name=new_project_name).first()
    if project:
        ack({
            "response_action": "errors",
            "errors": {
                "project_update_project_input_block": f"project with the name {new_project_name}\
                    already exists in the database"
            }
        })
    

    project = Project.query.filter_by(name=prev_project_name).first()
    project.name = new_project_name
    project.save()
    ack(response_action="update", view=project_updated_succesfully_view(
        prev_project_name, new_project_name))
