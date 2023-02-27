from app.models.project import Project
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
unique_identifier = "project_menu_"

header = HeaderBlock(
    text=PlainTextObject(text="Projects", emoji=True),
)

add_project_section = SectionBlock(
    text=MarkdownTextObject(text="Add a new Project"),
    accessory=ButtonElement(
        text=PlainTextObject(text="Add Project", emoji=True),
        value="click_me_123",
        action_id=f"{unique_identifier}",
        style="primary"
    )
)
update_project_section = SectionBlock(
    text=MarkdownTextObject(text="Edit the name of the project"),
    accessory=ButtonElement(
        text=PlainTextObject(
            text="Update Existing Project", emoji=True),
        value="click_me_123",
        action_id="button-action",
        style="primary"
    )
)
delete_project_section = SectionBlock(
    text=MarkdownTextObject(
        text="Delete or Archive a Project from any future use"),
    accessory=ButtonElement(
        text=PlainTextObject(text="Delete Project", emoji=True),
        value="click_me_123",
        action_id="button-action",
        style="danger"
    )
)

divider = DividerBlock()

def get_project_menu():
    return View(
        type="modal",
        title=PlainTextObject(text="Attendance Monitoring", emoji=True),
        close=PlainTextObject(text="Cancel", emoji=True),
        blocks=[header, divider, add_project_section, divider, update_project_section,divider, delete_project_section]
    )
