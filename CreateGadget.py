import requests
import json

# Set up the JIRA server URL and API token
jira_url = 'https://'
jira_api_token = ''
AUTH = ('thetube', jira_api_token)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Make the POST request to the Jira REST API to create the dashboard
payload = {
    "title": "Filter Results",
    "uri": "rest/gadgets/1.0/g/com.atlassian.jira.gadgets:filter-results-gadget/gadgets/filter-results-gadget.xml"
}

response = requests.post(
    f"{jira_url}/rest/api/2/dashboard/10002/gadget",
    auth=AUTH,
    json=payload
)

print(response.status_code)
filter_gadget = response.json()
gadgetId = filter_gadget['id']
# Check the response status code to make sure the request was successful
if response.status_code == 200:
    print("Successfully Gadget added to Dashboar.")
else:
    print(f"Failed to create dashboard. Response: {response.content}")

# Set the ID of the Jira filter you want to use
filter_id = '10010'
# Set the ID of the Jira dashboard you want to update
dashboard_id = '10002'

payload_updateGadget = {
    "color": "red",
    "title": "My new gadget title"

    # 'showActions': True,
    # "userPref": {
    #     "numColumns": num_columns,
    #     "columns": column_names
    # }
}
response_gadgetUpdate = requests.put(
    f"{jira_url}/rest/api/2/dashboard/10002/gadget/{gadgetId}",
    auth=AUTH,
    json=payload_updateGadget
)
print(response_gadgetUpdate.status_code)
print(response_gadgetUpdate.text)

# Updating Gadget Filter
payload_updateGadgetFilter={
     "filterId": filter_id,
     "columnNames": "issuetype|issuekey|summary",
     "num": "10",
     "refresh": "true",
     "isConfigured": "true"
}

response_gadgetUpdate = requests.put(
    f"{jira_url}/rest/api/2/dashboard/10002/items/{gadgetId}/properties/config",
    headers={
        "Accept": "application/json",
        "Content-Type": "application/json"
    },
    auth=AUTH,
    json=payload_updateGadgetFilter
)
print(response_gadgetUpdate.status_code)
print(response_gadgetUpdate.text)


