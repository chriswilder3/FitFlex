# context processors allow us inject data into all templates renderd by
# Django. We can further define what should these templates
# display based on whether request is sent by authenticated user or
# anonymous user.


def user_context( request ):

    if request.user.is_authenticated:
        return { 'logged_in_user' : request.user}
    else:
        return {'logged_in_user' : None}