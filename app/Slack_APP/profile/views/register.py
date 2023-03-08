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
    DatePickerElement,
    ConversationSelectElement
)
from slack_sdk.models.views import View

from app.models.project import get_active_projects
unique_identifier = "profile_register_"
header = HeaderBlock(
    text=PlainTextObject(text="Register", emoji=True)
)


def get_full_name_input(fullname):
    return InputBlock(
        label=PlainTextObject(text="Full Name", emoji=True),
        block_id=f"{unique_identifier}full_name_input_block",
        element=PlainTextInputElement(
            placeholder="Write Your Full Name",
            initial_value=fullname,
            action_id=f"{unique_identifier}full_name_input_action"
        )
    )


def get_role_input(initial_value=None):
    return InputBlock(
        label=PlainTextObject(text="Role :briefcase:", emoji=True),
        block_id=f"{unique_identifier}role_input_block",
        element=(PlainTextInputElement(
            placeholder="Please Select Your Role at A2SV",
            action_id=f"{unique_identifier}role_input_action"
        ) if initial_value == None else PlainTextInputElement(
            placeholder="Please Select Your Role at A2SV",
            action_id=f"{unique_identifier}role_input_action",
            initial_value=initial_value
        ))
    )


def get_date_input():
    return InputBlock(
        element=DatePickerElement(
            action_id=f"{unique_identifier}date_picker_action"
        ),
        label="Starting Date"
    )


def get_projets():
    projects = get_active_projects()
    return InputBlock(
        block_id=f'{unique_identifier}selected_project_block',
        label=PlainTextObject(
            text="select the project you are actively working on", emoji=True),
        element=StaticSelectElement(
            placeholder=PlainTextObject(text="Select a project", emoji=True),
            options=[Option(text=project.name, value=project.name)
                     for project in projects],
            action_id="static_select-action",
        ),
    )


def get_employment_status(employement_status=None):
    return InputBlock(
        block_id=f'{unique_identifier}selected_employement_status_block',
        label=PlainTextObject(
            text="What is your Current Employment Status", emoji=True),
        element=(
            StaticSelectElement(
                placeholder=PlainTextObject(text="Job Type", emoji=True),
                options=[
                    Option(text="Full-Time", value="Full-time"),
                    Option(text="Part-Time", value="Part-Time"),
                    Option(text="Intern", value="Intern")
                ],
                action_id=f"{unique_identifier}emoloyement_status_action",
            )
        ),
    )


def get_daily_plan_channel(daily_plan_channel=None):
    return InputBlock(
        element=(ConversationSelectElement(
            placeholder="Select a Channel",
            filter={"include": ["public", "mpim"]},
            action_id=f"{unique_identifier}daily_plan_channel_action",
        ) if daily_plan_channel == None else ConversationSelectElement(
            placeholder="Select a Channel",
            filter={"include": ["public", "mpim"]},
            action_id=f"{unique_identifier}daily_plan_channel_action",
            initial_conversation=daily_plan_channel
        )),
        label="Choose the channel to publish your daily plan to:",
        block_id=f"{unique_identifier}daily_plan_channel_block",
    )


def get_heads_up_channel(heads_up_channel=None):
    return InputBlock(
        element=(ConversationSelectElement(
            placeholder="Select a Channel",
            filter={"include": ["public", "mpim"]},
            action_id=f"{unique_identifier}heads_up_channel_action",
        ) if heads_up_channel == None else ConversationSelectElement(
            placeholder="Select a Channel",
            filter={"include": ["public", "mpim"]},
            action_id=f"{unique_identifier}heads_up_channel_action",
            initial_conversation=heads_up_channel
        )),
        label="Choose the channel to publish your Heads-Up :pleading_face: to:",
        block_id=f"{unique_identifier}heads_up_channel_block",
    )


def user_registration_form(
    fullname=None,
    role=None,
    employement_status=None,
    daily_plan_channel=None,
    heads_up_chanel=None
):
    return View(
        type="modal",
        callback_id=f'{unique_identifier}view_callback',
        title=PlainTextObject(text="Attendance Monitoring", emoji=True),
        submit=PlainTextObject(text="Continue", emoji=True),
        close=PlainTextObject(text="Cancel", emoji=True),
        blocks=[
            header,
            get_full_name_input(fullname),
            get_role_input(role),
            get_employment_status(employement_status),
            get_daily_plan_channel(daily_plan_channel),
            get_heads_up_channel(heads_up_chanel)
        ]
    )


def user_registration_form_edit():
    pass


def user_registered_succesfully_view(fullname):
    return View(
        type="modal",
        title=PlainTextObject(text="Attendance Tracker", emoji=True),
        close=PlainTextObject(text="Close", emoji=True),
        blocks=[
            HeaderBlock(
                text=PlainTextObject(
                    text=":white_check_mark:Member Registration Succesfull")
            ),
            SectionBlock(
                text=MarkdownTextObject(
                    text=f"New Member *{fullname}* Added Successfully")
            ),
        ]
    )
