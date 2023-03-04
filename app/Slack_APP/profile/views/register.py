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
            action_id=f"{unique_identifier}full_name_input_action"
        )
    )


def get_role_input():
    return InputBlock(
        label=PlainTextObject(text="Role :briefcase:", emoji=True),
        block_id=f"{unique_identifier}role_input_block",
        element=PlainTextInputElement(
            placeholder="Please Select Your Role at A2SV",
            action_id=f"{unique_identifier}role_input_action"
        ),
    )


def get_date_input():
    return InputBlock(
        element=DatePickerElement(
            action_id=f"{unique_identifier}date_picker_action"
        ),
        label="Starting Date"
    )


def get_employment_status():
    return SectionBlock(
        text="*What is your Current Employment Status>*",
        accessory=StaticSelectElement(
            placeholder="Select Role",
            options=[
                Option(text="Full-Time", value="Full-time"),
                Option(text="Part-Time", value="Part-Time"),
                Option(text="Intern", value="Intern")
            ],
            action_id="f{unique_identifier}employment_status_action"

        )
    )


def get_daily_plan_channel():
    return InputBlock(
        element=ConversationSelectElement(
            placeholder="Select a Channel",
            filter={"include": ["public", "mpim"]},
        ),
        label="Choose the channel to publish your daily plan to:"
    )


def get_heads_up_channel():
    return InputBlock(
        element=ConversationSelectElement(
            placeholder="Select a Channel",
            filter={"include": ["public", "mpim"]},
        ),
        label="Choose the channel to publish your Heads-Up :pleading_face: to:"
    )


def get_register_menu():
    return View(
        type="modal",
        callback_id=f'{unique_identifier}view_callback',
        title=PlainTextObject(text="Attendance Monitoring", emoji=True),
        submit=PlainTextObject(text="Continue", emoji=True),
        close=PlainTextObject(text="Cancel", emoji=True),
        blocks=[header, get_full_name_input("Teyouale"),
                get_role_input(),
                get_employment_status(),
                get_daily_plan_channel(),
                get_heads_up_channel()
                ]
    )
