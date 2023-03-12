import json
def handle_publish_daily_plan(ack, body ,logger, client):
    # print(body)
    # logger.debug(json.dumps(body, indent=4, separators=(',', ': ')))
    data = body['view']['state']['values']
    print(body)
    keys = data.keys()
    tasks = []
    for key in keys:
        if "daily" not in key:
            print("key is", key)
            result = data[key]['daily_plan_ignore_action']['selected_option']['value']
            key_splited = key.split("-")
            tasks.append({
                "task_type": key_splited[0],
                "task_id": key_splited[1],
                "state": result
            })
    tasks.append({"development":data['daily_plan_development_task']['IGNORE']['value'].split("\n")})
    tasks.append({"problem_solving":data['daily_plan_problem_solving_tasks']['IGNORE']['value'].split("\n")})
    print(tasks)
    user = body['user']

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