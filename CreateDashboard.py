import requests


# Set up the JIRA server URL and API token
jira_url = 'https://tba'
jira_api_token = ''
AUTH = ('the', jira_api_token)


def create_dashboard(title, description):
    # Create the payload for the POST request
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Make the POST request to the Jira REST API to create the dashboard
    payload = {
        "description": "A dashboard to help auditors identify sample of issues to check.",
        "name": "Auditors dashboard",
        "sharePermissions": [
            {
                "type": "authenticated"
            }
        ]
    }

    response = requests.post(
        f"{jira_url}/rest/api/2/dashboard",
        auth=AUTH,
        json=payload
    )

    print(response.status_code)
    # Check the response status code to make sure the request was successful
    if response.status_code == 200:
        print("Successfully created dashboard.")
    else:
        print(f"Failed to create dashboard. Response: {response.content}")


# Example usage
create_dashboard("My New Dashboard", "This is my first Jira dashboard.")
