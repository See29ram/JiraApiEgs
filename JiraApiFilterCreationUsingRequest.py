import requests
import json

# Set up the JIRA server URL and API token
jira_url = 'https://tba'
jira_api_token = ''

# Define the JQL query for the filter
jql_query = 'project = SNOW AND Sprint = Sprint-17'

# Define the filter name and description
filter_name = 'Sprint 17 using requests Open Issues2'
filter_description = 'A filter that shows all open issues in YOUR_PROJECT_KEY'

# Set up the request headers and data
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
data = {
    'jql': jql_query,
    'name': filter_name,
    'description': filter_description,
    'favourite': False,
    'sharePermissions':[
    {
        "type": "authenticated"
    }]


}

# Send the request to create the filter using the JIRA API
response = requests.post(
    f'{jira_url}/rest/api/2/filter',
    auth=('', jira_api_token),
    headers=headers,
    data=json.dumps(data)
)
print(response)
filter_details = response.json()

# Get the share permissions for the filter
#share_permissions = filter_details['sharePermissions']
#print(share_permissions)
# Check the response status code
if response.status_code == 200:
    print(f'Filter "{filter_name}" was created successfully.')
    print(response.content)
else:
    print(f'Error creating filter: {response.content}')
