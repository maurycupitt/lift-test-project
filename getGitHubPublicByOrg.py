#!/usr/bin/env python

import json
import urllib.request
import sys

# Query LinkedIn for users of a company
def getLinkedInUsers(company):
    # Get company's employees
    url = "https://api.linkedin.com/v2/companies/%s/employees?format=json" % company
    employees = json.loads(urllib.request.urlopen(url).read())
    employees = [employee['firstName'] + ' ' + employee['lastName'] for employee in employees]
    print(employees)

# Get public Github repos for user
def getGitHubPublicByUser(user):
    # Get user's public repos
    url = "https://api.github.com/users/%s/repos?type=all&per_page=100" % user
    repos = json.loads(urllib.request.urlopen(url).read())
    repos = [repo['name'] for repo in repos]
    print(repos)


def main():
    args = sys.argv
    # getGitHubPublicByUser(args[1])
    getLinkedInUsers(args[1])

    

if __name__ == "__main__":
    main()