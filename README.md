touchit
=======

Votes on a target reddit submission using a configured set of accounts and proxies

# Requirements
* python2.7

# Reddit Setup
In order to access the reddit api, you must first create an application.
1. Go to https://www.reddit.com/prefs/apps/
2. Click "are you a developer?"
3. Enter any name
4. Select "script"
5. Set "redirect uri" to "http://localhost"
6. Note your client id and client secret to be used in the script configuration

# Installation
First extract the source files to wherever you want.
 
Executing the following from the command line:
```commandline
cd /path/to/requirements.txt
pip install requirements.txt
```

# Configuration
Configuring touchit is done via a json file. See config.json.example for an example.


# Usage
## Options
```
touchit.py [-h] [--config [CONFIG]] links [links ...]

Upvote some links.

positional arguments:
  links              A link to upvote

optional arguments:
  -h, --help         show this help message and exit
  --config [CONFIG]  Path to the config file

```

##Example invocation:
```commandline
python /path/to/touchit.py --config /path/to/config.json https://reddit.com/link/to/upvote
```

