import requests
import json

url = "https://api.atlassian.com/jsm/insight/workspace/{workspaceId}/v1/object/{id}"

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
