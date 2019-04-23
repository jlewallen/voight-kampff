from discord import Embed
from commands_library.query_helper import query_request
from helper_functions.logger import general_debug, general_info
from helper_functions.errorHelpers import errorEmbedBuilder

def shortStringBuild(title, url, com):
    return "["+title+"]("+url+") | [comments](https://www.reddit.com"+com+")\n"


def reddit_top3(req_sub):
    data = query_request("www.reddit.com",
                         "/r/{s}/top/.json?limit=3".format(s=req_sub),
                         )

    general_debug("Reddit is: " + str(data))

    if "error" in data.keys():
        return errorEmbedBuilder("Subreddit doesn't exist",
                                 "Reddit"
                                 )

    tops = data["data"]["children"]
    if len(tops) < 3:
        return errorEmbedBuilder("Subreddit has less than 3 posts recently",
                                 "Reddit"
                                 )

    message = ""
    for i in range(0, 3):
        message += str(i+1) + '. ' + \
                              shortStringBuild(tops[i]['data']['title'],
                                               tops[i]['data']['url'],
                                               tops[i]['data']['permalink'])

    em = Embed(title="Top posts of /r/" + req_sub,
                       description=message,
                       colour=0x0000FF)

    general_info("Reddit created and returned embed object")
    return em
