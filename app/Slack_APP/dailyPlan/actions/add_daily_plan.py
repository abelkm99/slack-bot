import datetime
import json

from app.Slack_APP.dailyPlan.views.daily_plan_attachement import build_daily_plan_attachement
from app.models.daily_plan import create_daily_plan, get_daily_plan_for_today, get_previous_plan, update_daily_plan_tasks, update_prev_date_state
from app.models.user import get_user_by_slack_id


def handle_publish_daily_plan(ack, body, logger, client, context):
    context['flask_app'].app_context().push()
    # logger.debug(json.dumps(body, indent=4, separators=(',', ': ')))

    # get the tasks from the body
    data = body['view']['blocks']
    task_texts = [x['text']['text'].replace(
        "*", "") for x in data if "development-" in x['block_id'] or "problem_solving-" in x['block_id']]

    data = body['view']['state']['values']

    keys = data.keys()
    tasks = []
    for key in keys:
        if "daily" not in key:
            result = data[key]['daily_plan_ignore_action']['selected_option']['value']
            key_splited = key.split("-")
            tasks.append({
                "task_type": key_splited[0],
                "task_id": key_splited[1],
                "state": result
            })
    for idx, task in enumerate(tasks):
        task["task"] = task_texts[idx]

    today_development = [x.strip() for x in data['daily_plan_development_task']
                         ['IGNORE']['value'].split("\n") if len(x.strip())]
    today_problem_solving = [x.strip() for x in data['daily_plan_problem_solving_tasks']
                             ['IGNORE']['value'].split("\n") if len(x.strip())]
    user = body['user']
    dev_completed = []
    dev_not_completed = []
    prob_completed = []
    prob_not_completed = []

    completed_task_ids = set()

    for task in tasks:
        if task['task_type'] == 'development':
            if task['state'] == ':white_check_mark: Done':
                dev_completed.append(task['task'])
                completed_task_ids.add(int(task['task_id']))
            else:
                dev_not_completed.append(task['task'])
        elif task['task_type'] == 'problem_solving':
            if task['state'] == ':white_check_mark: Done':
                prob_completed.append(task['task'])
                completed_task_ids.add(int(task['task_id']))
            else:
                prob_not_completed.append(task['task'])
    # print(dev_completed, dev_not_completed, prob_completed,
    #       prob_not_completed, today_development, today_problem_solving)

    user = get_user_by_slack_id(body['user']['id'])
    prev_plan = get_previous_plan(user.slack_id)

    # check if i have published a daily PLAN on this day

    current_daily_plan = get_daily_plan_for_today(user=user)
    attachment_tobe_published = build_daily_plan_attachement(
        dev_completed=dev_completed,
        dev_not_completed=dev_not_completed,
        problem_solving_completed=prob_completed,
        problem_solving_not_completed=prob_not_completed,
        todays_development=today_development,
        todays_problem_solving=today_problem_solving,
        user=user,
        prev_date=datetime.datetime.now(),
        current_date=datetime.datetime.now(),
    )
    if current_daily_plan:
        # do update operations here
        response = client.chat_update(
            channel=current_daily_plan.channel_id,
            ts=current_daily_plan.message_id,
            attachments=attachment_tobe_published
        )
        if response['0k']:
            current_daily_plan = update_daily_plan_tasks(current_daily_plan=current_daily_plan)
            current_daily_plan.update()
        return

    response = client.chat_postMessage(
        channel=user.daily_plan_channel,
        attachments=attachment_tobe_published
    )

    if response['ok']:
        try:
            daily_plan = create_daily_plan(
                user=user,
                message_id=response['ts'],
                developments=today_development,
                problem_solvings=today_problem_solving
            )
            prev_plan = update_prev_date_state(
                prev_plan=prev_plan, completed_task_ids=completed_task_ids)
            prev_plan.update(commit=False)
            daily_plan.save()
        except Exception as e:
            client.chat_delete(channel=response["channel"], ts=response["ts"])

    return

    return

    import time
    attachment = {
        "fallback": "How is your day going so far?",
        "title": "How is your day going so far?",
        "text": f"Hi <@{user['id']}>, how's it going?",
        "color": "#3AA3E3",
        "footer": "My Bot",
        "ts": int(time.time())
    }
    response = client.chat_postMessage(
        channel="#general",
        text="Daily Tasks Report",
        attachments=[attachment]
    )
    # updated_attachment = {
    #     "fallback": "Saturday's Report / Mar 4",
    #     "title": "Saturday's Report / Mar 4",
    #     "fields": [
    #         {
    #             "title": "A2SV Development",
    #             "value": "Sync with product team\nWork on user flows related to uploading materials\nSync with Selman",
    #             "short": False
    #         },
    #         {
    #             "title": "A2SV Problem Solving",
    #             "value": "Solve leetcode daily question",
    #             "short": False
    #         }
    #     ],
    #     "color": "#36a64f",
    #     "footer": "My Bot",
    #     "ts": event['ts']
    # }
