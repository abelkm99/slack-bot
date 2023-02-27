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
unique_identifier = "project_delete_project_"

# Define the header block
header = HeaderBlock(
    text=PlainTextObject(text="Delete Project", emoji=True)
)

confirm_delete_header = HeaderBlock(
    text=PlainTextObject(text="Confirm Delete Project", emoji=True)
)
# Define the section block
section = SectionBlock(
    text=MarkdownTextObject(
        text="*When a project is deleted, it will be marked as inactive and moved to an archive, where it cannot be accessed or used in the future*.\n *This Process is Irreversible*",
        verbatim=True
    )
)


def get_confirmation_sectionBlock(project_name):
    return SectionBlock(
        text=MarkdownTextObject(
            text=f"*Are you sure you want to delete the project {project_name}*\n *this process is IRREVERSIBLE*",
        )
    )
# Define the input block with a static select element


def get_projets():
    projects = Project.query.all()
    return InputBlock(
        label=PlainTextObject(text="Project Name", emoji=True),
        element=StaticSelectElement(
            placeholder=PlainTextObject(text="Select a project", emoji=True),
            options=[Option(text=project.name, value=project.name)
                     for project in projects],
            action_id="static_select-action",
        ),
    )


# Define the divider block
divider = DividerBlock()


def delete_project_view():
    return View(
        type="modal",
        callback_id=f"{unique_identifier}fist_step",
        title=PlainTextObject(text="Attendance Tracker", emoji=True),
        submit=PlainTextObject(text="Continue", emoji=True),
        blocks=[header, section, divider, get_projets()]
    )


def delete_project_confirmation_view(project_name):
    return View(
        type="modal",
        callback_id=f"{unique_identifier}confirm_delete_project",
        title=PlainTextObject(text="Attendance Tracker", emoji=True),
        submit=PlainTextObject(text="Continue", emoji=True),
        blocks=[header, get_confirmation_sectionBlock(
            project_name=project_name), divider, get_projets()]
    )
