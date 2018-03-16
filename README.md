# GitHubReadmeCorpus
A project to compile a corpus of all github README documentation in English

Currently compatible with Python3

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
3. Add your github username and password to the local environment variables (if in a linux environment, just type this in the terminal)
```
export GITHUB_USERNAME=YOUR_GITHUB_USERNAME_HERE
export GITHUB_PASSWORD=YOUR_GITHUB_PASSWORD_HERE
```
4. add a data directory (or whichever name you like and update that in collect.py)
```
mkdir data
```
5. Run the script
```
python collect.py
```
