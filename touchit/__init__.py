import argparse
import json
import random
import praw
import time


def should_upvote():
    random_int = random.randint(0, 1000)
    return random_int <= (upvote_percentage * 10)


def random_wait():
    wait = random.randint(0, 10)
    print "Waiting %i seconds" % wait
    time.sleep(wait)


# Set up argparse
parser = argparse.ArgumentParser(description='Upvote some links.')
parser.add_argument('links', nargs='+',
                    help='A link to upvote')
parser.add_argument('--config', dest='config', nargs='?', default="config.json",
                    help='Path to the config file')

# Parse the arguments
args = parser.parse_args()

# Load the config file
config = json.load(file(args.config))

# Extract some configuration
upvote_percentage = config['upvotePercentage']

# Iterate over the links and upvote them
for link in args.links:
    for account in config['accounts']:
        print "Logging in as %s" % account['username']
        reddit = praw.Reddit(client_id=config['clientId'],
                             client_secret=config['clientSecret'],
                             user_agent='touchit',
                             redirect_uri='http://localhost',
                             username=account['username'],
                             password=account['password'],
                             https_proxy=account['proxy'])

        # Wait a random amount of time
        random_wait()

        # Fetch the submission
        print "Fetching the target submission"
        submission = reddit.submission(url=link)

        # Wait a random amount of time
        random_wait()

        # Upvote the link
        if should_upvote():
            print "User %s upvoting target" % account['username']
            submission.upvote()
        else:
            print "User %s downvoting target" % account['username']
            submission.downvote()

        # Wait a random amount of time
        random_wait()

        # Vote on something from /r/all to seem more real
        for submission in reddit.subreddit('all').hot(limit=1):
            print "User %s voting on hottest post in /r/all" % account['username']
            if should_upvote():
                submission.upvote()
            else:
                submission.downvote()

