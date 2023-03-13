import datetime
from typing import List
from slack_sdk.models.attachments import BlockAttachment, Attachment
from app.utils import parse_date_time
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

from app.models.user import User
unique_identifier = "daily_plan_"

header = HeaderBlock(text=PlainTextObject(
    text=f"-----:pencil2:  Daily Plan Report -----", emoji=True))
footer = HeaderBlock(text=PlainTextObject(
    text="---------------------------------------------------------------------", emoji=True))


def get_header_attachment():
    return BlockAttachment(blocks=[header])


def get_footer_attahcment():
    return BlockAttachment(blocks=[footer])


def date_indicator_block(content: str, date: str):
    return BlockAttachment(
        blocks=[
            DividerBlock(),
            ContextBlock(
                elements=[
                    ImageElement(
                        image_url="https://www.worklifepsych.com/wp-content/uploads/2018/11/WLP_web_image-18-1000x801.png",
                        alt_text="random_image"
                    ),
                    MarkdownTextObject(
                        text=content + " " + f"*{date}*", verbatim=False)
                ]
            ),
            DividerBlock(),
        ]
    )


def build_daily_plan_attachement(
    dev_completed: List[str],
    dev_not_completed: List[str],
    problem_solving_completed: List[str],
    problem_solving_not_completed: List[str],
    todays_development: List[str],
    todays_problem_solving: List[str],
    user: User,
    prev_date: datetime.datetime,
    current_date: datetime.datetime,
):
    attachments = []
    attachments.append(get_header_attachment())
    attachments.append(Attachment(
        title=user.role,
        text=f"<@{user.slack_id}>",
        author_name=user.full_name,
        author_icon="https://avatars.slack-edge.com/2023-03-13/4951001898961_871a4c0952e6b697c3f8_512.png",
        color="#439FE0"
    ))
    attachments.append(date_indicator_block(
        content="Previous Day Report",
        date=parse_date_time(current_date, date_format="%B %d %Y")
    ))
    if len(dev_completed):
        attachments.append(Attachment(
            color="good",
            title="Development Completed",
            text="\n".join([f"> _{task}_" for task in dev_completed]),
            markdown_in=["text"]
        ))
    if len(dev_not_completed):
        attachments.append(Attachment(
            color="#fd000e",
            title="Development Not Completed",
            text="\n".join([f"> _{task}_" for task in dev_not_completed]),
            markdown_in=["text"]
        ))
    if len(problem_solving_completed):
        attachments.append(Attachment(
            color="good",
            title="Problem Solving Completed",
            text="\n".join(
                [f"> _{task}_" for task in problem_solving_completed]),
            markdown_in=["text"]
        ))
    if len(problem_solving_not_completed):
        attachments.append(Attachment(
            color="#fd000e",
            title="Problem Solving Not Completed",
            text="\n".join(
                [f"> _{task}_" for task in problem_solving_not_completed]),
            markdown_in=["text"]
        ))
    attachments.append(date_indicator_block(
        content="Todays Plan ",
        date=parse_date_time(current_date, date_format="%B %d %Y")
    ))
    attachments.append(Attachment(
        color="#1414ff",
        title="Development",
        text="\n".join(
            [f"> _{task}_" for task in todays_development]),
    ))
    attachments.append(Attachment(
        color="#ff6b00",
        title="Development",
        text="\n".join(
            [f"> _{task}_" for task in todays_problem_solving]),
    ))

    return attachments
