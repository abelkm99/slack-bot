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
    ConversationSelectElement,
    ConfirmObject
)
from slack_sdk.models.views import View

unique_identifier = "daily_plan_"


header = HeaderBlock(
    text=PlainTextObject(text="Daily Plan 📋", emoji=True)
)
divider = DividerBlock()


def get_previous_header():
    return ContextBlock(
        elements=[
            MarkdownTextObject(text="*📅 Previous Day Report / March 03*")
        ]
    )


def get_today_header():
    return ContextBlock(
        elements=[
            MarkdownTextObject(text="*📅 Toda's Report / March 11*")
        ]
    )


problem_solving = SectionBlock(
    text=MarkdownTextObject(text="*Problem Solving*")
)


def get_prev_problem_solving():
    projects = [":white_check_mark: Done", ":x: Not Done"]
    return [SectionBlock(
        text=MarkdownTextObject(text="*Sync With Product Team*"),
        accessory=StaticSelectElement(
            placeholder=PlainTextObject(text="Select a project", emoji=True),
            options=[Option(text=project, value=project)
                     for project in projects],
            action_id=f"{unique_identifier}ignore_action",
            initial_option=Option(text=projects[1], value=projects[1]),
        ),
    ) for i in range(2)]


development = SectionBlock(text=MarkdownTextObject(text="*Development*"))


def get_prev_development():
    projects = [":white_check_mark: Done", ":x: Not Done"]
    return [SectionBlock(
        text=MarkdownTextObject(text="*Sync With Product Team*"),
        accessory=StaticSelectElement(
            placeholder=PlainTextObject(text="Select a project", emoji=True),
            options=[Option(text=project, value=project)
                     for project in projects],
            action_id=f"{unique_identifier}ignore_action",
            initial_option=Option(text=projects[1], value=projects[1]),
        ),
    ) for i in range(3)]


development_input_block = InputBlock(
    label=PlainTextObject(text="Development", emoji=True),
    element=PlainTextInputElement(
        multiline=True,
    ),
    optional=True
)

problem_solving_input_block = InputBlock(
    label=PlainTextObject(text="Development", emoji=True),
    element=PlainTextInputElement(
        multiline=True,
    ),
    optional=True
)


def get_daily_plan_view():
    blocks = [header, divider, get_previous_header(), divider, development]
    blocks.extend(get_prev_development())
    blocks.extend([divider, problem_solving])
    blocks.extend(get_prev_problem_solving())
    blocks.extend([
        divider,
        get_today_header(),
        development_input_block,
        problem_solving_input_block
    ])
    return View(
        type="modal",
        callback_id=f'{unique_identifier}view_callback',
        title=PlainTextObject(text="Attendance Tracker", emoji=True),
        close=PlainTextObject(text="Close", emoji=True),
        submit=PlainTextObject(text="Publish", emoji=True),
        blocks=blocks
    )
