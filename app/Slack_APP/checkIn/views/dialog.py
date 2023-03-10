from slack_sdk.models.views import View
from slack_sdk.models.blocks import HeaderBlock, DividerBlock, ContextBlock, SectionBlock, ImageElement, PlainTextObject, MarkdownTextObject
import datetime
import json
unique_identifier = "checkIn_Confirmation_"

header = HeaderBlock(text=' :tada: You Have Successfully Check-In')

current_datetime = datetime.datetime.now().strftime("%A, %b %d %Y, %I:%M%p")
current_date = datetime.datetime.now().strftime("%B %d, %Y")

subHeader = ContextBlock(
    block_id=f'{unique_identifier}SubHeader',
    elements=[
        MarkdownTextObject(
            text=f"*{current_date} * | *Full-Time * - UI-UX Member")
    ]
)


def body(thumbnail):
    return SectionBlock(
        block_id=f'{unique_identifier}body',
        text=f" *Eyouale Tensae* \n {current_datetime} \n",
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
    # print(json.dumps(user, indent=2))
    # response = client.users_info(user=body['user']['id'])
    thumbnail = user["profile"]["image_512"]
    # print(thumbnail)
    return View(
        type="modal",
        callback_id=f'{unique_identifier}view_callback',
        title=PlainTextObject(text="Attendance Monitoring", emoji=True),
        close=PlainTextObject(text="Close", emoji=True),
        blocks=[
            header,
            subHeader,
            body(thumbnail),
            footer
        ]
    )
