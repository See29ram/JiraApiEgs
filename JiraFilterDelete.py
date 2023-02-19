import requests
import json

# Set up the JIRA server URL and API token
jira_url = 'https://tba'
jira_api_token = ''
AUTH =('the', jira_api_token)


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


# Send the request to create the filter using the JIRA API
response = requests.get(
    f'{jira_url}/rest/api/2/filter/my',
    auth=AUTH,
    headers=headers,

)

if response.status_code == 200:
        filters = response.json()
        if not filters:
            print(f'No filters found for user')
        else:
            # loop through the matching filters and delete them one by one
            for filter in filters:
                filter_id = filter['id']

                delete_response = requests.delete(f'{jira_url}/rest/api/2/filter/{filter_id}',
                                                  auth=AUTH)
                if delete_response.status_code == 204:
                    print(f'Filter {filter_id} has been deleted.')
                else:
                    print(f'Error: failed to delete filter {filter_id}.')
else:
        print('Error: failed to search for filters.')

