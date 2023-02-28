
def handle_view_submission_update_project(ack, body, logger, client):
    logger.debug(body)
    prev_project_name = body['view']['state']['values']['project_update_project_selected_project_block']['static_select-action']['selected_option']['value']
    new_project_name = body['view']['state']['values']['project_update_project_input_block']['project_update_project_new_project_name']['value']

    # if prev_project_name == new_project_name:
    ack({
        "response_action": "errors",
        "errors": {
            "project_update_project_input_block": "the previous project \
                    name and the new project name can't be the same"
        }
    })
        # return
    pass
