from slack_sdk.models.blocks import (
    ContextBlock,
    DividerBlock,
    HeaderBlock,
    InputBlock,
    PlainTextInputElement,
    SectionBlock,
    PlainTextObject,
    MarkdownTextObject,
)
from slack_sdk.models.views import View
unique_identifier = "project_add_new_project_"


def project_added_succesfully_view(project_name):
    return View(
        type="modal",
        title={
            "type": "plain_text",
            "text": "Attendance Tracker",
            "emoji": True
        },
        close={
            "type": "plain_text",
            "text": "Close",
            "emoji": True
        },
        blocks=[
            HeaderBlock(
                text=PlainTextObject(
                    text=":file_cabinet:  Add New Project :file_cabinet:")
            ),
            SectionBlock(
                text=MarkdownTextObject(text=f"Projet *{project_name}* Added Successfully")
            ),
        ]
    )


def add_project_normal(project_name):
    return View(
        callback_id=f"{unique_identifier}submission_callback",
        type="modal",
        title={
            "type": "plain_text",
            "text": "Attendance Tracker",
            "emoji": True
        },
        submit={
            "type": "plain_text",
            "text": "Submit",
            "emoji": True
        },
        close={
            "type": "plain_text",
            "text": "Back",
            "emoji": True
        },
        blocks=[
            HeaderBlock(
                text=PlainTextObject(
                    text=":file_cabinet:  Add New Project :file_cabinet:")
            ),
            DividerBlock(),
            SectionBlock(
                text=MarkdownTextObject(text="Add New Project this is new")
            ),
            ContextBlock(
                elements=[
                    MarkdownTextObject(
                        text=":pushpin: project name has to be unique"
                    )
                ]
            ),
            InputBlock(
                dispatch_action=True,
                element=PlainTextInputElement(
                    dispatch_action_config={
                        "trigger_actions_on": ["on_character_entered"]},
                    initial_value=project_name,
                    action_id=f"{unique_identifier}charachter_change_action"
                ),
                label={"type": "plain_text",
                       "text": "Project Name", "emoji": True},
                block_id=f"{unique_identifier}block", 
            ),
        ]
    )


def add_project_error(project_name):
    return View(
        type="modal",
        callback_id=f"{unique_identifier}submission_callback",
        title={
            "type": "plain_text",
            "text": "Attendance Tracker",
            "emoji": True
        },
        submit={
            "type": "plain_text",
            "text": "Submit",
            "emoji": True
        },
        close={
            "type": "plain_text",
            "text": "Back",
            "emoji": True
        },
        blocks=[
            HeaderBlock(
                text={
                    "type": "plain_text",
                    "text": ":file_cabinet:  Add New Project :file_cabinet:",
                    "emoji": True
                }
            ),
            DividerBlock(),
            SectionBlock(
                text={"type": "mrkdwn", "text": "Add New Project"}
            ),
            ContextBlock(
                elements=[
                    {
                        "type": "mrkdwn",
                        "text": "*:pushpin: project name has to be unique*"
                    }
                ]
            ),
            InputBlock(
                dispatch_action=True,
                element=PlainTextInputElement(
                    dispatch_action_config={
                        "trigger_actions_on": ["on_character_entered"]},
                    initial_value=project_name,
                    action_id=f"{unique_identifier}charachter_change_action"
                ),
                label={"type": "plain_text",
                       "text": "Project Name", "emoji": True},
                block_id=f"{unique_identifier}block",
            ),
            SectionBlock(
                text=MarkdownTextObject(
                    text=":x: A project with the same name already exists.")
            )
        ]
    )
