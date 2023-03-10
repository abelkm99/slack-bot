from slack_sdk.models.views import View
from slack_sdk.models.blocks import PlainTextObject, HeaderBlock, ContextBlock, DividerBlock, SectionBlock, StaticSelectElement, MarkdownTextObject, Option, InputBlock, ImageElement, RadioButtonsElement
from app.models.project import Project
import json
import datetime

unique_identifier = 'check-out_menu_'

current_datetime = datetime.datetime.now().strftime("%A, %b %d %Y, %I:%M%p")
current_date = datetime.datetime.now().strftime("%B %d, %Y")


def header(username):
    return HeaderBlock(
        block_id=f'{unique_identifier}header_block',
        text=PlainTextObject(
            text=f":tada: Welcome :back: {username} !!!", emoji=True),
    )


subHeader = ContextBlock(
    block_id=f'{unique_identifier}SubHeader',
    elements=[
        MarkdownTextObject(

            text=f"*{current_date} * | *Full-Time * - UI-UX Member")
    ]
)

information = SectionBlock(
    text=" *:clipboard: For 8:00 hr you have have work in atrons project :tada: *")


def body(thumbnail):
    return SectionBlock(
        block_id=f'{unique_identifier}body',
        text="*Check-In Time* ;-  Thursday, Oct 23 2019, 5:30am \n *Hour Work * ;-  3:00 HR",
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
            Option(text=" :star2::star2::star2::star2: ", value="1"),
            Option(text=" :star2::star2::star2: ", value="1"),
            Option(text=":sob:", value="1"),
        ]
    ),
)


def get_checkOut_form(user):
    thumbnail = user["profile"]["image_512"]
    # print(json.dumps(body, indent=2))
    return View(
        type="modal",
        callback_id=f'{unique_identifier}view_callback',
        title=PlainTextObject(text="Attendance Monitoring", emoji=True),
        close=PlainTextObject(text="Cancel", emoji=True),
        submit=PlainTextObject(text="Check-out :cry:", emoji=True),
        blocks=[
            header(user['name']),
            subHeader,
            DividerBlock(),
            information,
            body(thumbnail),
            warning,
            DividerBlock(),
            productivity_form
        ]
    )
