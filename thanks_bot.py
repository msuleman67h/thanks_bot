import CONFIG
import functions

# Only works in the subreddit mentioned in CONFIG
subreddit = CONFIG.reddit.subreddit(CONFIG.subreddit_name)

# Looks for this word
keypharse = "!Thanks"

# Looks for comment in comments stream
for comment in subreddit.stream.comments():
    # Gets the submission in which comment is posted
    submission = comment.submission
    # Making both text uppercase so we don't have to worry about case sensitivity
    if keypharse.capitalize() in comment.body.capitalize() and submission.link_flair_text == 'Question':
        # Verifies if the checks have passed
        result = functions.verify_checks(comment)
        # Calls respond function that will reply according to result
        functions.respond(result, comment)
