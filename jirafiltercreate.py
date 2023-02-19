from jira import JIRA

# Set up the JIRA server URL and API token
jira_url = 'https://tba'
jira_api_token = ''

# Connect to the JIRA server using the API token
jira = JIRA(jira_url, basic_auth=('', jira_api_token))

# Define the JQL query for the filter
jql_query = 'project = SNOW AND Sprint = Sprint-17'

# Define the filter name and description
filter_name = 'Sprint-17 Issues_Second'
filter_description = 'A filter that shows all Sprint 17 issues'

# Create the filter using the JIRA API
jira.create_filter(filter_name, filter_description, jql_query)
