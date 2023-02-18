Register_User = {
	"title": {
		"type": "plain_text",
		"text": "My App",
		"emoji": True 
	},
	"type": "modal",
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True 
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": True 
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
				"emoji": True 
			}
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True 
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Atrons",
							"emoji": True 
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "RateEat",
							"emoji": True 
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Lab-Connect",
							"emoji": True 
						},
						"value": "value-2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Portal",
							"emoji": True 
						},
						"value": "value-2"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Curently Working On",
				"emoji": True 
			}
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True 
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Full-Time",
							"emoji": True 
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Part-Time",
							"emoji": True 
						},
						"value": "value-1"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Job Type",
				"emoji": True 
			}
		}
	]
}