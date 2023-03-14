from slack_sdk.models.views import View
from slack_sdk.models.blocks import PlainTextObject, HeaderBlock, ContextBlock, DividerBlock, SectionBlock, StaticSelectElement, MarkdownTextObject, Option, InputBlock, ImageElement, RadioButtonsElement
from app.models.project import Project
import json
import datetime

unique_identifier = 'check-in_menu_'
current_date = datetime.datetime.now().strftime("%B %d, %Y")


def header(username):
    return HeaderBlock(
        block_id=f'{unique_identifier}header_block',
        text=PlainTextObject(
            text=f":tada: Welcome {username} !!!", emoji=True),
    )


def subHeader(role, employement):
    return ContextBlock(
        block_id=f'{unique_identifier}SubHeader',
        elements=[
            MarkdownTextObject(

                text=f"*{current_date} * | *{employement}* - {role}")
        ]
    )


title = SectionBlock(
    text=" :loud_sound: *Please fill your check-checkout* :loud_sound:")


def select_project():
    projects = Project.query.filter_by(archived=0).all()
    return InputBlock(
        block_id=f'{unique_identifier}select_project',
        label=":clipboard: *Select your project*\n that you are partipated today",
        hint="that you are partipated today",
        element=StaticSelectElement(
            placeholder=PlainTextObject(text="Select a project", emoji=True),
            options=[Option(text=project.name, value=project.name)
                     for project in projects],
            initial_option=Option(
                text=projects[0].name, value=projects[0].name),
            action_id="static_select-action",
        )
    )


lastCheckIn = ContextBlock(
    elements=[
        MarkdownTextObject(text=" *Last Check-In Time    *\nOct 22-23"),
        MarkdownTextObject(text=" *Minmium Hour Left*\n 3:00 HR")
        # MarkdownTextObject(text=" *Last Check-In Time*\nOct 22-23", "*Minmium Hour Left*\n 3:00 HR"),
    ])


def get_checkIn_form(name, role, employement, slack_id):
    # print(json.dumps(body, indent=2))
    return View(
        type="modal",
        callback_id=f'{unique_identifier}view_callback',
        title=PlainTextObject(text="Attendance Monitoring", emoji=True),
        close=PlainTextObject(text="Cancel", emoji=True),
        submit=PlainTextObject(
            text="Check in :smiley:", emoji=True),
        blocks=[
            header(name),
            subHeader(role, employement),
            DividerBlock(),
            title,
            select_project(),
            DividerBlock(),
            # lastCheckIn
        ]
    )
