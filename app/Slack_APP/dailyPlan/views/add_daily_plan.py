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
from app.models.daily_plan import get_previous_plan
from app.utils import parse_date_time
from datetime import datetime

unique_identifier = "daily_plan_"


header = HeaderBlock(
    text=PlainTextObject(text="Daily Plan 📋", emoji=True)
)
divider = DividerBlock()


def get_previous_header(prev_datetime):
    return ContextBlock(
        elements=[
            MarkdownTextObject(
                text=f"*📅* Previous Day Report / *{prev_datetime}*"
            )
        ]
    )


def get_today_header(current_date):
    return ContextBlock(
        elements=[
            MarkdownTextObject(
                text=f"*📅* Toda's Report / *{current_date}*"
            )
        ]
    )


problem_solving = SectionBlock(
    text=MarkdownTextObject(text="*Problem Solving*")
)


development = SectionBlock(text=MarkdownTextObject(text="*Development*"))


def generate_task_drop_down_option(tasks, task_type):
    projects = [":white_check_mark: Done", ":x: Not Done"]
    return [SectionBlock(
        text=MarkdownTextObject(text=f"*{task.task}*"),
        accessory=StaticSelectElement(
            placeholder=PlainTextObject(text="Select a project", emoji=True),
            options=[Option(text=project, value=project)
                     for project in projects],
            action_id=f"{unique_identifier}ignore_action",
            initial_option=(
                Option(text=projects[1], value=projects[1]) if task.state == 0 else Option(
                    text=projects[0], value=projects[0])
            ),
        ),
        block_id=f"{task_type}-{task.id}"
    ) for task in tasks]


development_input_block = InputBlock(
    label=PlainTextObject(text="Development", emoji=True),
    element=PlainTextInputElement(
        multiline=True,
        initial_value='''Sync with TLs
Helped frontends with integration
Reviewed the website we did so far and listed issues that should be added and need modifications''',
        action_id="IGNORE"
    ),
    block_id=f"{unique_identifier}development_task",
    optional=True
)

problem_solving_input_block = InputBlock(
    label=PlainTextObject(text="Development", emoji=True),
    element=PlainTextInputElement(
        multiline=True,
        initial_value='''1 squid game problem and daily
Solved 3 squid game problems
One on one
        ''',
        action_id="IGNORE"
    ),
    block_id=f"{unique_identifier}problem_solving_tasks",
    optional=True
)


def get_daily_plan_view(slack_id):
    # get previous day tasks
    formater = "%B %d %Y"
    daily_plan = get_previous_plan(slack_id=slack_id)

    development_tasks, problem_solving_tasks = [], []

    for task in daily_plan.tasks:
        if task.type == "DEVELOPMENT":
            development_tasks.append(task)
        else:
            problem_solving_tasks.append(task)
    # pass the day for get_previous_header
    blocks = [
        header,
        divider,
        get_previous_header(parse_date_time(
            daily_plan.time_published, formater)),
        divider,
        development
    ]
    if len(development_tasks):
        blocks.extend(generate_task_drop_down_option(development_tasks,"development"))
    blocks.extend([divider, problem_solving])
    if len(problem_solving_tasks):
        blocks.extend(generate_task_drop_down_option(problem_solving_tasks,"problem_solving"))
    blocks.extend([
        divider,
        get_today_header(
            parse_date_time(datetime.now(), formater)
        ),
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
