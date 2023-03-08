from slack_sdk.models.views import View
from slack_sdk.models.blocks import PlainTextObject, HeaderBlock
unique_identifier = 'check-in_menu'


header = HeaderBlock(
    text=PlainTextObject(text="Profile", emoji=True),
)

def get_checkIn_menu():
    # send_time_counter(5)
    return View(
        type="modal",
        callback_id=f'{unique_identifier}view_callback',
        title=PlainTextObject(text="Attendance Monitoring", emoji=True),
        close=PlainTextObject(text="Cancel", emoji=True),
        blocks=[header]
    )
