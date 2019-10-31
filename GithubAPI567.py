#This is a branch Mocking!
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:46:14 2019

@author: jchlu
"""

import requests
import json

def getRepos(username):
    url = json.loads(requests.get(f'https://api.github.com/users/{username}/repos').text)
    repos = []
    for repo in url:
        repos.append(repo['name'])
    return repos

def getCommits(username, repoName):
    url = json.loads(requests.get(f'https://api.github.com/repos/{username}/{repoName}/commits').text)
    return len(url)

def getReposAndCommits(username):
    repoNames = getRepos(username)
    repoDict = {}
    for repoName in repoNames:
        numCommits = getCommits(username, repoName)
        repoDict[repoName] = numCommits
    return repoDict

def printRepoDict(repoDict):
    for repo, commits in repoDict.items():
        print(f"Repo: {repo} Number of commits: {commits}")


#Below I tested two of my friends githubs and they were all correct. I also tested (with print statements)
#The output of the requests.get (variable)
#The array of repos
#The requests.get (variable + repository)

#Test 1
#print(getUser("tommypinto"))
#$Output should be
#Repo: SchoolWork - Number of commits: 3

#Test 2
#print(getUser("tkautz12"))
#$Output should be
#Repo: Everything- - Number of commits: 15

#Test 3
#print(getUser("jchlus"))
#$Output should be
#Repo: Baseball-scouter - Number of commits: 6
#Repo: GitHubApi567 - Number of commits: 4
#Repo: SW-567 - Number of commits: 1
#Repo: Triangle567-Hw02 - Number of commits: 3
#Repo: Triangles - Number of commits: 2