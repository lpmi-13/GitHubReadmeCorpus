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
3. Create a github token and add it to the environment variables (if in a linux environment, just type this in the terminal)
```
export GITHUB_TOKEN=YOUR_GITHUB_TOKEN_HERE
```
4. add a data directory (or whichever name you like and update that in collect.py)
```
mkdir data
```
5. Run the script
```
python collect.py
```

## Docker method

1. build the container

```
docker build -t corpus_collector .
```

2. run it

> be sure to `export GITHUB_TOKEN=YOUR_TOKEN_HERE` prior to running this.

```
docker run -it --rm -v $(pwd)/data:/app/data -e GITHUB_TOKEN=$GITHUB_TOKEN corpus_collector
```

The data should wind up in the local `./data` dir so you can stop the container and start it again later without needing to re-process all the readmes from the start.
