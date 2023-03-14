from slack_sdk.models.views import View
from slack_sdk.models.blocks import HeaderBlock, DividerBlock, ContextBlock, SectionBlock, ImageElement, PlainTextObject, MarkdownTextObject
import datetime
import json
from app.models.time_sheet import get_status

from app.models.user import get_user_by_slack_id
unique_identifier = "checkIn_Confirmation_"

header = HeaderBlock(text=' :tada: You Have Successfully Check-In')

current_datetime = datetime.datetime.now().strftime("%A, %b %d %Y, %I:%M%p")
current_date = datetime.datetime.now().strftime("%B %d, %Y")


def subHeader(role, employement):
    return ContextBlock(
        block_id=f'{unique_identifier}SubHeader',
        elements=[
            MarkdownTextObject(

                text=f"*{current_date} * | *{employement}* - {role}")
        ]
    )


def body(name, thumbnail):
    return SectionBlock(
        block_id=f'{unique_identifier}body',
        text=f" *{name}* \n *Check-In Time* ;- {current_datetime} \n",
        accessory=ImageElement(
            image_url=thumbnail,
            alt_text="user thumbnail",
        ),
    )


footer = ContextBlock(
    block_id=f'{unique_identifier}footer',
    elements=[
        ImageElement(
            image_url="https://api.slack.com/img/blocks/bkb_template_images/notificationsWarningIcon.png",
            alt_text="notifications warning icon",
        ),
        MarkdownTextObject(
            text="*Recommended Check-Out: 4:30pm*",
        )
    ]
)


def get_confirmation_dialog(user):
    slack_id = user['id']
    thumbnail = user["profile"]["image_512"]
    # print(json.dumps(user, indent=2))
    user = get_user_by_slack_id(slack_id)
    name = user.full_name
    role = user.role
    employement = user.employement_status
    # slack_id = user.slack_id
    return View(
        type="modal",
        callback_id=f'{unique_identifier}view_callback',
        title=PlainTextObject(text="Attendance Monitoring", emoji=True),
        close=PlainTextObject(text="Close", emoji=True),
        blocks=[
            header,
            subHeader(role, employement),
            body(name, thumbnail),
            # footer
        ]
    )
