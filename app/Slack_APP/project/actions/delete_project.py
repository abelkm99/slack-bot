from app.models.project import *
from app.Slack_APP.project.views import *


def handle_delete_project_first_step(ack, body, logger, client):
    project_name = body['view']['state']['values']['project_delete_project_selected_project_block']\
                   ['static_select-action']['selected_option']['value']
    logger.info(project_name)
    ack(response_action="update", view=delete_project_confirmation_view(project_name=project_name))

def handle_delete_project_confirmation_step(ack, body, logger, client, context):
    # delete the project at this step and show project deleted succesfull page
    # with an ackowledgement of that the project has been deleted
    context['flask_app'].app_context().push()
    project_name = body['view']['private_metadata']
    logger.debug(project_name)
    project = Project.query.filter_by(name=project_name).first()
    logger.info(project)
    if project:
        project.archived = True
        project.save()
    ack(response_action="update", view=project_deleted_succesfully_view(project_name=project_name))