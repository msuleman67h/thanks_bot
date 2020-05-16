# File function: Stores all the functions that are used in thanks_bot.py
import CONFIG

ALREADY_SOLVED = 0
CANNOT_AWARD_POST = 1
CANNOT_AWARD_YOURSELF = 2
ONLY_OP_CAN_THANK = 3
PASSED = 4


# Function that rewards the comments if all conditions passes
# Also updates the post flair to solved
def award_point(p_comment):
    author_name = p_comment.author.name
    # if the author has no flair
    if p_comment.author_flair_css_class == '':
        # sets the flair to one
        CONFIG.reddit.subreddit(CONFIG.subreddit_name).flair.set(author_name, text='1',
                                                                 flair_template_id=CONFIG.score_id)
    else:
        # Getting the flair and incrementing it by one
        thanks_score = p_comment.author_flair_text
        thanks_score = int(thanks_score)
        thanks_score += 1
        # Setting the new flair
        CONFIG.reddit.subreddit(CONFIG.subreddit_name).flair.set(author_name, text=str(thanks_score),
                                                                 flair_template_id=CONFIG.score_id)
    # Sets the post flair to solved
    submission = p_comment.submission
    submission.flair.select(CONFIG.solved_id)
    pass


# Function that responds to the request according to verify_checks result
def respond(checks_passed, comment):
    # If op is thanking more than once
    if checks_passed == ALREADY_SOLVED:
        response = "You can Thank only once per post. To reverse the previous thank please contact mods"
        response = response + "\n\n*^(This action was performed by a bot, please contact the mods for any questions.)*"
        comment.reply(response)
    # Someone tries to thank the post
    elif checks_passed == CANNOT_AWARD_POST:
        response = "Only the comments can be rewarded!"
        response = response + "\n\n*^(This action was performed by a bot, please contact the mods for any questions.)*"
        comment.reply(response)
    # If OP tries to thanks its comments
    elif checks_passed == CANNOT_AWARD_YOURSELF:
        response = "You cannot reward a point to yourself!"
        response = response + "\n\n*^(This action was performed by a bot, please contact the mods for any questions.)*"
        comment.reply(response)
    # Someone else besides OP tries to thank
    elif checks_passed == ONLY_OP_CAN_THANK:
        response = "Only the OP can thank in this post!"
        response = response + "\n\n*^(This action was performed by a bot, please contact the mods for any questions.)*"
        comment.reply(response)
    # All conditions passes
    else:
        # Replies with confirmation comment
        response = "You have awarded one point to " + str(comment.parent().author)
        response = response + "\n\n*^(This action was performed by a bot, please contact the mods for any questions.)*"
        comment.reply(response)
        # Calls function that gives point to parent comment author
        award_point(comment.parent())
    pass


# Function that verifies if the score should be given
# Checks if op has thanked more than once
# Also checks that op should award themselves
def verify_checks(comment):
    submission = comment.submission
    parent_comment = comment.parent()
    # Checks the post is marked as solved
    if submission.link_flair_text == 'Solved':
        return ALREADY_SOLVED
    # Top level comments are ignored
    elif comment.is_root:
        return CANNOT_AWARD_POST
    # Checks if OP is thanking its own comment
    elif comment.author == parent_comment.author:
        return CANNOT_AWARD_YOURSELF
    # Only the OP of post can thank
    elif submission.author != comment.author:
        return ONLY_OP_CAN_THANK
    # If every check passed
    else:
        return PASSED
