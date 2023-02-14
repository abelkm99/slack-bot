import os
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "What is the currency of Japan?",
        "answer": "Yen"
    },
    {
        "question": "What is the tallest mammal?",
        "answer": "Giraffe"
    },
    {
        "question": "What is the largest planet in the solar system?",
        "answer": "Jupiter"
    }
]

CURRENT_QUESTION_INDEX = 0


@app.message("quiz")
def start_quiz(ack, command, say):
    ack("Starting quiz...")
    global CURRENT_QUESTION_INDEX
    CURRENT_QUESTION_INDEX = 0
    ask_question(say)


def ask_question(say):
    global CURRENT_QUESTION_INDEX
    if CURRENT_QUESTION_INDEX >= len(QUESTIONS):
        say("Quiz completed!")
        return
    question = QUESTIONS[CURRENT_QUESTION_INDEX]["question"]
    say(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": question
                }
            },
            {
                "type": "input",
                "block_id": "answer_input",
                "element": {
                    "type": "plain_text_input",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Enter your answer here..."
                    }
                },
                "label": {
                    "type": "plain_text",
                    "text": "Answer"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Submit"
                        },
                        "value": "submit",
                        "action_id": "submit_answer"
                    }
                ]
            }
        ]
    )


@app.action("submit_answer")
def handle_answer(ack, say, action):
    global CURRENT_QUESTION_INDEX
    ack()
    answer = action["value"]
    print("answer is",answer)
    correct_answer = QUESTIONS[CURRENT_QUESTION_INDEX]["answer"]
    if answer == correct_answer:
        say("Correct answer!")
    else:
        say("Wrong answer. The correct answer was: " + correct_answer)
    CURRENT_QUESTION_INDEX += 1
    ask_question(say)


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
