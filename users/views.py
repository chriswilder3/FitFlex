from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse

from .forms import SignUpForm

# Create your views here.

def signup(request):
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

            # After obtaining and processing this data internally, we
            # can redirect the page to another with HttpResponseRedirect
            HttpResponseRedirect( '/users/user_dashboard')
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
                # <form action="/users/signup" method="post">
                #     {% csrf_token %}
                #     {{ signUpForm }}
                #     <input type="submit" value="Submit">
                # </form>


def signin(request):
    signInTemplate = loader.get_template('signin.html')

    return HttpResponse( signInTemplate.render() )

