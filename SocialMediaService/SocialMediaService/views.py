from django.http import JsonResponse, HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the SocialMediaService index.")


def mockTweets(request):
    # I'd need to apply for research token to get access to Twitter api. This being just a
    # demo, here is some recent Tweets of Novak Djokovic
    tweets = {
        "Tweet 1": "I’m excited to announce I am now a brand ambassador for @LemeroImage",
        "Tweet 2": "The feeling is totally mutual @DaniilMedwed All respect to you your team",
        "Tweet 3": "I’m sending everyone best wishes, many blessings to everyone <3",
        "Tweet 4": "Blessed to experience first snow in Serbian mountains."
    }
    return JsonResponse(tweets)
