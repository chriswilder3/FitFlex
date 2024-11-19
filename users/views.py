from django.shortcuts import render, redirect

from django.template import loader

from django.http import HttpResponseRedirect

from .forms import SignUpForm, SignInForm

from .models import User

from django.contrib.auth import login,logout, authenticate

from django.contrib.auth import User as AuthUser
    # Since we have already used the User for our ORM model, 
    # For authentication object we cant use the same name
    # So lets rename it to AuthUser

# Create your views here.

def signupdummy(request):
    # Note that view functions are able handle both GET/ POST requests.
    # GET : when the page is first loaded, showing an empty form. We need
            # Inject form along with template as response
    # POST : When the the form is submitted. We need to validate the
            # the fields and if correct the user to another page, 
            # ex : in our case to users dashboard.

    if request.method == 'POST' :  
        # Checks if the request is a form submission

        submittedForm = SignUpForm( request.POST)
          # If yes, the submitted data will be in request.POST
          # Now we create an instance of Form defined in forms.py and 
          # populate it with submitted data. This is called binding 
          # data to the form.

        if submittedForm.is_valid():
            # After running validations on form, if all correct, the
            # is_valid() is set true. otherwise false.
            # Since its true, validated data will be in 
            # form_instance.cleaned_data variable

            # Lets just print it : 
            print(submittedForm.cleaned_data)

            # After obtaining and processing this data internally, we
            # can redirect the page to another with HttpResponseRedirect
            return HttpResponseRedirect( '/users/signup')
            # Remember we have to return the above object.
    else:
        # If the request was not POST, then it was GET( since only 2 
        # possible for forms). It means the page is being requested for
        # the first time. Hence we need to instantiate the form
        # and inject into the template.
        newForm = SignUpForm()

            # Note that the below render() does the same work render()
            # we used from template.loader() But practice this one
            # Since, it directly returns HttpResponse object and 
            # recommeded by Django. Its much simpler.
        context = { 'signUpForm' : newForm }
        return render(request,'signup.html', context )
                # Now Go to signup.html and enter {{signUpForm}} to
                # generate this form there.
                # Just add structure similar to this : 
                # <form action="/users/signup/" method="post">
                #     {% csrf_token %}
                #     {{ signUpForm }}
                #     <input type="submit" value="Submit">
                # </form>
                #  Remember wherever POST is sent to. dont
                # forget / at the end of link in the method of forms in html


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            formData = form.cleaned_data
            print(userData)
            # {{'name': 'sachin', 'username': 'sachin'...}
            # Hence its a dictionary, Now lets load up the Django model
            # User and push this data to the user, so that we can verify 
            # later during sign in.
            # Note that User in the model, and 
            x = User(name = formData['name'],
                    username = formData['username'],
                    email = formData['email'],
                    phone = formData['phone'],
                    password =  formData['password'])
            x.save()
            # Now we also need to login into Django auth system
            # Which is able to handle auth and session tasks
            # Note that auth object User(AuthUser here) is also
            # a special ORM model created by django to store
            # info of users into DB. Hence we can apply
            # ORM operations to CRUD on it.

            # auth.User API :
            # Note that auth.User class has following attributes.
            # username, password, email, first_name, last_name
            # So best way to create users is to use
            # create_user() helper function , pass these params to it.

            newUser = AuthUser.objects.create_user(
                first_name = formData['name'],
                # Since We in form we took the whole name, we
                # will assign it to first_name and ignore last_name attr

                username = formData['username'],
                email = formData['email'],
                password = formData['password']
            )
            newUser.save()
            # Now that we have the credentials. We need to authenticate
            # and login like in signin to go to the user dashboard

            # Authenticating/Login :
            #  syntax : user = authenticate(request=None, **credentials)
            # We can use it to verify a set of credentials and takes them
            # as kwarguments, generally 2 things :username, password.
            # It checks the credentials against auth backends. The auth 
            # backends are different kind of authentication services.
            # We can use either normal django ones or third party auth backends.
            # If credentials are valid for a backend, then an auth.User is
            # returned , other wise PermissionDenied is raised and None is returned
            # Hence we can use this as login point also.

            authenticated_user = authenticate( username = formData['name'] 
                    , password = formData['password'])

            # Now we need to login this authenticated user.
            # Note that Django uses sessions and middleware to hook the
            # authentication system into request objects.

            # To log the user in,We use login(), which takes the request
            # object and authenticated User object as param. login() saves
            # the user’s ID in the session, using Django’s session framework

            if authenticated_user: # if returned user object in NOT None
                login( request, authenticated_user)
                # Now redirect to success page, which is dashboard for us.
                return redirect('/users/dashboard/')
            # Note that login, logout, authenticate all three must be
            # imported from django.contrib.auth

        else:
            # If the form is invalid, just render the form with errors
            # But I found a variable with all errors
            print( form.errors)
            return render(request, 'signup.html', 
                        {'form': form,'error': 1 })
    else:
        form = SignUpForm()
        return render( request, 'signup.html',{'form': form, 'error':0})

def signin(request):
    if request.method == 'POST': # POST must be str her
        form = SignInForm( request.POST )
        if form.is_valid():
            formData = form.cleaned_data
            username = formData['username']
            password = formData['password']
            user_object = User.objects.all().values()
            print( type(user_object))
            print( user_object[0]['name'])
            unameExists = False
            for x in user_object:
                #print( x['name'],x['password'])
                if username == x['username']:
                    unameExists = True
                    if password != x['password']:
                        # wrong password
                        print('wrong password')
                        return render(render, 'signin.html', {'form':form, 'error':1})
                    else:
                         # credentials look good, Now authenticate
                         # and log into the system
                        authenticated_user = authenticate( username = username
                            , password = password)
                        if authenticated_user:
                            login( request, authenticated_user)
                            print('success login')
                            return redirect('/users/dashboard/')
            # username doesnt exist
            return render( request, 'signin.html', {'form':form, 'error':1})
        else:
            # form validation fail
            return render( request, 'signin.html', {'form':form, 'error':1})
    else:
        # Request is GET/ first time visit
        form = SignInForm()
        return render( request, 'signin.html', {'form': form, 'error':0})

def dashboard( request):

     # Note that we just came into this view. But we also
     # need to verfiy thatthe user is authentified and logged in.
     # We can do this using this using request object since we know 
    # Django save the user info in it.

    # Djangos session framework provides request.user attribute and 
    # a request.auser async method on every request which represents the
    # current user. 
    # If the current user has not logged in, this attribute will be set 
    # to an instance of AnonymousUser, otherwise it will be an instance
    #  of User (AuthUser in our case).

    if request.user.is_authenticated:
        # User is now on his dashboard. But we also need
        # to pass userinfo to it. But note that, We only
        # need to get hold of the username to know everything abt him
        # since usernames are unique.
        # Hence lets fetch, username and pass it to the user to
        # be printed.
        print(request.user);
        context ={

        }
        return render( request, 'dashboard.html', context)
        
    else:
        print(' Anonyymous user, returning to login...')
        return redirect( '/users/signin/')
    
    # We can acheive the same as above using @login_required decorator
    # which is part of contrib.auth.deorator.
    # Ex: 
    # from django.contrib.auth.decorators import login_required
    # from django.shortcuts import render

    # @login_required
    # def dashboard_view(request):
    #     #do something