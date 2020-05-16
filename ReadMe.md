
## thanks_bot
A Reddit bot that looks for the work "!Thanks" in the posts with flair marked "Question". If if finds the word. It changes the flair to "Solved" and gives one score to whoever the comment replied to.
It checks following things
- Comment is not top level (Bot can't reward a Question)
- OP of post isn't thanking its own comment
-  Post isn't already solved

To setup CONFIG see the following template below

    import praw
    
    # Login information
    username = 'bot_account_name'
    password = 'account password'
    
    # API information
    # This is from [Authorized Applications](https://www.reddit.com/prefs/apps)
    client_id = 'Client ID'
    client_secret = 'Client Secret'
    user_agent = 'Thanks_Bot 1.0 by /u/msuleman67h'
    
    # Put the name of your subreddit here
    subreddit_name = "yoursubreddithere"
    
    # Login Api
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         username=username,
                         password=password,
                         user_agent=user_agent)
    
    # Flair IDs (from flair settings)
    solved_id = "COPY and past flair ID here"
    score_id = "COPY and past flair ID here"
