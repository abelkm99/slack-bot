from slack_sdk.models.views import View
from slack_sdk.models.blocks import HeaderBlock, DividerBlock, ContextBlock, SectionBlock, ImageElement, PlainTextObject, MarkdownTextObject

unique_identifier = "checkIn_Confirmation_"

header = HeaderBlock(text=' :tada: You Have Successfully Check-In')

subHeader = ContextBlock(
    block_id=f'{unique_identifier}SubHeader',
    elements=[
        MarkdownTextObject(
            text="*March 06, 2022 * | *Full-Time * - UI-UX Member")
    ]
)


body = SectionBlock(
    block_id=f'{unique_identifier}body',
    text=" *Eyouale Tensae* \n Thursday, Oct 23 2019, 5:30am \n",
    accessory=ImageElement(
        image_url="https://avatars.slack-edge.com/2023-03-08/4908624443878_7ed674cacef649d04679_512.jpg",
        alt_text="calendar thumbnail",
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


def get_confirmation_dialog():
    return View(
        type="modal",
        callback_id=f'{unique_identifier}view_callback',
        title=PlainTextObject(text="Attendance Monitoring", emoji=True),
        close=PlainTextObject(text="Close", emoji=True),
        blocks=[
            header,
            subHeader,
            body,
            footer
        ]
    )
