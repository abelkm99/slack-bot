from slack_sdk.models.blocks import (
    ContextBlock,
    DividerBlock,
    HeaderBlock,
    InputBlock,
    PlainTextInputElement,
    SectionBlock,
    PlainTextObject,
    MarkdownTextObject,
    StaticSelectElement,
    ButtonElement,
    ButtonStyles,
    Option,

)

from slack_sdk.models.views import View

from app.models.project import Project
unique_identifier = "project_update_project_"

header = HeaderBlock(
    text=PlainTextObject(text="Edit Project", emoji=True)
)
section = SectionBlock(
    text=MarkdownTextObject(
        text="*Edit Project Name*"
    )
)


def get_projets():
    projects = Project.query.filter_by(archived=0).all()
    return InputBlock(
        block_id=f'{unique_identifier}selected_project_block',
        label=PlainTextObject(
            text="select a project you want to edit", emoji=True),
        element=StaticSelectElement(
            placeholder=PlainTextObject(text="Select a project", emoji=True),
            options=[Option(text=project.name, value=project.name)
                     for project in projects],
            action_id="static_select-action",
        ),
    )


def get_input_block():
    return InputBlock(
        element=PlainTextInputElement(
            placeholder="new project name",
            action_id=f"{unique_identifier}new_project_name"
        ),
        label=PlainTextObject(text="new project name", emoji=True),
        block_id=f"{unique_identifier}input_block",
    )


divider = DividerBlock()


def edit_project_view():
    return View(
        type="modal",
        callback_id=f"{unique_identifier}edit_project_view",
        title=PlainTextObject(text="Attendance Tracker", emoji=True),
        submit=PlainTextObject(text="Update", emoji=True),
        blocks=[header, divider, get_projets(), divider, get_input_block()]
    )


def project_updated_succesfully_view(prev_project_name, new_project_name):
    return View(
        type="modal",
        title=PlainTextObject(text="Attendance Tracker", emoji=True),
        close=PlainTextObject(text="Close", emoji=True),
        blocks=[
            HeaderBlock(
                text=PlainTextObject(text="✅Success")
            ),
            divider,
            SectionBlock(
                text=MarkdownTextObject(
                    text=f"Projet *{prev_project_name}* has been updated to {new_project_name} successfully.")
            ),
        ]
    )
