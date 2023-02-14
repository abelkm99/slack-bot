Register_User = {
	"title": {
		"type": "plain_text",
		"text": "My App",
		"emoji": true
	},
	"type": "modal",
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": true
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": true
	},
	"blocks": [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action",
				"initial_value": "Abel Kidanemariam"
			},
			"label": {
				"type": "plain_text",
				"text": "Full Name",
				"emoji": true
			}
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": true
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Atrons",
							"emoji": true
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "RateEat",
							"emoji": true
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Lab-Connect",
							"emoji": true
						},
						"value": "value-2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Portal",
							"emoji": true
						},
						"value": "value-2"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Curently Working On",
				"emoji": true
			}
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": true
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Full-Time",
							"emoji": true
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Part-Time",
							"emoji": true
						},
						"value": "value-1"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Job Type",
				"emoji": true
			}
		}
	]
}