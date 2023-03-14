from slack_sdk.models.views import View
from slack_sdk.models.blocks import PlainTextObject, HeaderBlock, ContextBlock, DividerBlock, SectionBlock, StaticSelectElement, MarkdownTextObject, Option, InputBlock, ImageElement, RadioButtonsElement
from app.models.project import Project
import json
from datetime import datetime
from app.models.time_sheet import get_elapsed_time, get_status
from app.models.user import get_user_by_slack_id
from app.utils import convert_time_to_string

unique_identifier = 'check-out_menu_'

current_datetime = datetime.now().strftime("%A, %b %d %Y, %I:%M%p")
current_date = datetime.now().strftime("%B %d, %Y")


def header(username):
    return HeaderBlock(
        block_id=f'{unique_identifier}header_block',
        text=PlainTextObject(
            text=f":tada: Welcome :back: {username} !!!", emoji=True),
    )


def subHeader(role, employement):
    return ContextBlock(
        block_id=f'{unique_identifier}SubHeader',
        elements=[
            MarkdownTextObject(

                text=f"*{current_date} * | *{employement}* - {role}")
        ]
    )


def information(elasped_time):
    return SectionBlock(
        text=f" *:clipboard: For {elasped_time} hr you have have work in atrons project :tada: *")


def body(thumbnail, elasped_time, check_inTime):
    return SectionBlock(
        block_id=f'{unique_identifier}body',
        text=f"*Check-In Time* ;-  {check_inTime} \n *Hour Work * ;-  {elasped_time} HR",
        accessory=ImageElement(
            image_url=thumbnail,
            alt_text="user thumbnail",
        ),
    )


warning = ContextBlock(
    block_id=f'{unique_identifier}footer',
    elements=[
        ImageElement(
            image_url="https://api.slack.com/img/blocks/bkb_template_images/notificationsWarningIcon.png",
            alt_text="notifications warning icon",
        ),
        MarkdownTextObject(
            text="*A2SV expect you to work minimum 8hr per day*",
        )
    ]
)

productivity_form = InputBlock(
    label="Rate you Productiviy",
    element=RadioButtonsElement(
        action_id=f'{unique_identifier}productivity_form',
        options=[
            Option(text=" :star2::star2::star2::star2: ", value="3"),
            Option(text=" :star2::star2::star2: ", value="2"),
            Option(text=":sob:", value="1"),
        ]
    ),
)


def get_checkOut_form(user):
    slack_id = user['id']
    elasped_time = get_elapsed_time(slack_id)
    thumbnail = user["profile"]["image_512"]
    user = get_user_by_slack_id(slack_id)
    name = user.full_name
    role = user.role
    employement = user.employement_status
    slack_id = user.slack_id
    check_inTime = convert_time_to_string(get_status(slack_id).check_in_time)

    return View(
        type="modal",
        callback_id=f'{unique_identifier}view_callback',
        title=PlainTextObject(text="Attendance Monitoring", emoji=True),
        close=PlainTextObject(text="Cancel", emoji=True),
        submit=PlainTextObject(text="Check-out :cry:", emoji=True),
        blocks=[
            header(name),
            subHeader(role, employement),
            DividerBlock(),
            information(elasped_time),
            body(thumbnail, elasped_time, check_inTime),
            warning,
            DividerBlock(),
            productivity_form
        ]
    )
