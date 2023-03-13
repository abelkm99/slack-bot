
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
    ConfirmObject,
    ImageElement
)
from slack_sdk.models.views import View


def daily_plan_published_succesfully():
    return View(
        type="modal",
        title=PlainTextObject(text="Attendance Tracker", emoji=True),
        close=PlainTextObject(text="Close", emoji=True),
        blocks=[
            HeaderBlock(
                text=PlainTextObject(
                    text=":white_check_mark:Daily Plan Published Succesfully"
                )
            ),
        ]
    )

def daily_plan_updated_succesfully():
    return View(
        type="modal",
        title=PlainTextObject(text="Attendance Tracker", emoji=True),
        close=PlainTextObject(text="Close", emoji=True),
        blocks=[
            HeaderBlock(
                text=PlainTextObject(
                    text=":white_check_mark:Daily Plan Updated Succesfully"
                )
            ),
        ]
    )
