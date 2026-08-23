import datetime
import os
import requests
from dateutil import relativedelta

HEADERS = {'authorization': 'token ' + os.environ['ACCESS_TOKEN']}
USER_NAME = os.environ['USER_NAME']  # 'riteshkrsingh'

def get_user_info():
    url = f"https://api.github.com/users/{USER_NAME}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return None

def graphql_request(query, variables):
    request = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables}, headers=HEADERS)
    if request.status_code == 200:
        return request.json()
    raise Exception(f"GraphQL failed: {request.text}")

def get_repo_stars():
    # Fetching all repos to sum stars
    cursor = None
    total_stars = 0
    repo_count = 0
    while True:
        query = """
        query($login: String!, $cursor: String) {
          user(login: $login) {
            repositories(first: 100, after: $cursor, ownerAffiliations: OWNER) {
              totalCount
              edges {
                node {
                  stargazers { totalCount }
                }
              }
              pageInfo { endCursor hasNextPage }
            }
          }
        }
        """
        variables = {'login': USER_NAME, 'cursor': cursor}
        data = graphql_request(query, variables)
        user_data = data['data']['user']
        repo_count = user_data['repositories']['totalCount']
        for edge in user_data['repositories']['edges']:
            total_stars += edge['node']['stargazers']['totalCount']
        if not user_data['repositories']['pageInfo']['hasNextPage']:
            break
        cursor = user_data['repositories']['pageInfo']['endCursor']
    return repo_count, total_stars

def get_commit_count():
    today = datetime.datetime.today()
    one_year_ago = today - relativedelta.relativedelta(years=1)
    query = """
    query($login: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $login) {
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar { totalContributions }
        }
      }
    }
    """
    variables = {'login': USER_NAME, 'from': one_year_ago.isoformat(), 'to': today.isoformat()}
    data = graphql_request(query, variables)
    return data['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions']

def update_svg():
    user_info = get_user_info()
    repo_count, star_count = get_repo_stars()
    commit_count = get_commit_count()
    follower_count = user_info['followers'] if user_info else 0
    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

    with open('dark_mode.svg', 'r') as f:
        svg = f.read()

    svg = svg.replace('{{ repo_count }}', str(repo_count))
    svg = svg.replace('{{ star_count }}', str(star_count))
    svg = svg.replace('{{ follower_count }}', str(follower_count))
    svg = svg.replace('{{ commit_count }}', str(commit_count))
    svg = svg.replace('{{ update_time }}', update_time)

    with open('dark_mode.svg', 'w') as f:
        f.write(svg)

if __name__ == "__main__":
    update_svg()
