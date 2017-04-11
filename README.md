# GitHubReadmeCorpus
A project to compile a corpus of all github README documentation in English

## Aim
a corpus of all publicly available README documentation from GitHub has a number
of potential applications
* create a list of the most common words by word class (noun, verb, adjective...) for this register
* same as above, but broken down by programming language
* create a dataset for teachers to use in creating materials for a hypothetical "writing documentation" component of an ESP course for programmers
* etc...

## Running the scripts to create your own dataset
1. Clone this repository
2. Install the dependencies via 
```
pip install -r requirements.txt
```
3. Create a file titled 'settings.yaml', and enter your github username and password in the following format
```
---
user: [YOUR_GITHUB_USERNAME_HERE]
password: [YOUR_GITHUB_PASSWORD_HERE]
```
4. Run the script
```
python collect.py
```
