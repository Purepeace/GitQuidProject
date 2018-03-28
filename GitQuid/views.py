from django.shortcuts import render, redirect
from GitQuid.models import Category
from GitQuid.forms import CategoryForm
# from GitQuid.forms import ProjectForm


from django.http import JsonResponse
from GitQuid.forms import *
from GitQuid.models import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserChangeForm


# from django import template


def index(request):
    # request.session.set_test_cookie()
    # category_list = Category.objects.order_by('-likes')[:5]
    # project_list = Project.objects.order_by('-views')[:5]
    # context_dict = {'categories': category_list, 'projects': project_list}
    #
    # visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

        category_list = Category.objects.order_by('-likes')[:5]
        context_dict = {'categories': category_list}

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)

    response = render(request, 'GitQuid/index.html')
    return response


def about(request):
    response = render(request, 'GitQuid/about.html')
    return response


#
#
# # A helper method
# def get_server_side_cookie(request, cookie, default_val=None):
#     val = request.session.get(cookie)
#     if not val:
#         val = default_val
#     return val
#
#
# def visitor_cookie_handler(request):
#     visits = int(get_server_side_cookie(request, 'visits', '1'))
#     last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
#     last_visit_time = datetime.strptime(last_visit_cookie[:-7],
#                                         '%Y-%m-%d %H:%M:%S')
#     # If it's been more than a day since the last visit...
#     if (datetime.now() - last_visit_time).days > 0:
#         visits = visits + 1
#         # update the last visit cookie now that we have updated the count
#         request.session['last_visit'] = str(datetime.now())
#
#     else:
#         visits = 1
#         # set the last visit cookie
#         request.session['last_visit'] = last_visit_cookie
#
#     # Update/set the visits cookie
#     request.session['visits'] = visits
#
#
# def about(request):
#     # prints out whether the method is a GET or a POST
#     print(request.method)
#     # prints out the user name, if no one is logged in it prints 'AnonymousUser'
#     print(request.user)
#
#     if request.session.test_cookie_worked():
#         print("TEST COOKIE WORKED!")
#         request.session.delete_test_cookie()
#     context_dict = {}
#     visitor_cookie_handler(request)
#     context_dict['visits'] = request.session['visits']
#     response = render(request, 'GitQuid/about.html', context=context_dict)
#     return response
#
#
def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated projects.
        # Note that filter() will return a list of project objects or an empty list
        projects = Project.objects.filter(category=category)

        # Add our results list to the template context under name projects.
        context_dict['projects'] = projects
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use theis in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # we get here if we didn't find the specified category.
        # don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['projects'] = None
    # Go render the response and return it to the client.
    return render(request, 'GitQuid/index.html', context_dict)


# def add_category(request):
#     form = CategoryForm()
#
#     # A HTTP POST?
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#
#         # Have we been provided with a valid form?
#         if form.is_valid():
#             # Save the new category to the database
#             cat = form.save(commit=True)
#             print(cat, cat.slug)
#             # Now that the category is saved
#             # We colud give a confirnation message
#             # But since the most recent category added is on the index project
#             # Then we can direct the user bacl to the index project.
#             return index(request)
#         else:
#             # The supplied form contained errors -
#             # just print them to the terminal
#             print(form.errors)
#
#     # Will handle the bad form, new form, or no form supplied cases.
#     # Render the form with error messages(if any).
#
#     return render(request, 'GitQuid/add_category.html', {'form': form})
#
#


#
#
# def view_detail(request):
#     searchWord = request.POST.get('search', '')
#     return HttpResponse(searchWord)


# register = template.Library()
#
#
# @register.simple_tag(takes_context=True)
def browseProjects(request):
    projects = Project.objects.all()
    donations = Donation.objects.all()

    for project in projects:
        donation_sum = 0
        for donation in donations:
            if project.name == donation.project.name:
                donation_sum += donation.amount
        # Update Project model with sum of donations
        p = Project.objects.get(id=project.id)
        p.donations = donation_sum

    # Get parameter by which projects are going to be sorted
    sort = request.GET.get('sort', 'name')

    # Get all projects, sorting alphabetically by default

    context_dict = {'projects': projects.order_by(sort)}

    return render(request, 'GitQuid/browseProjects.html', context_dict)


@login_required()
def addProject(request):
    context_dic = {'form': None}
    if request.method == "POST":
        form = AddProjectForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_id = request.user.id
            f.dateCreated = timezone.now()
            f.save()
            project = form.instance
            # Proceed to project editing
            return HttpResponseRedirect((reverse('GitQuid:editProject', kwargs={'slug': project.slug})))
        else:
            print(form.errors)
    else:
        form = AddProjectForm()
        context_dic['form'] = form

    return render(request, 'GitQuid/addProject.html', context_dic)


@login_required()
def editProject(request, slug):
    context_dic = {'form': None, 'project': None}
    # get currently editable project
    project = get_object_or_404(Project, slug=slug)
    context_dic['project'] = project
    # if user is the author of the project enable editing
    if request.user == project.user:
        if request.method == "POST":
            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                form.save()
                # redirect to the same page
                return HttpResponseRedirect(reverse('GitQuid:editProject', kwargs={'slug': slug}))
            else:
                print(form.errors)
        else:
            form = ProjectForm(instance=project)
            context_dic['form'] = form
    else:
        # go to projects page
        return HttpResponseRedirect(reverse('GitQuid:browseProjects'))

    return render(request, 'GitQuid/editProject.html', context_dic)


def viewProject(request, slug):
    context_dic = {'project': None, 'donations': None, 'form': None, 'authenticated': False, 'author': False, 'leftToGoal': 0.0,
                   'percentCollected': 0.0}
    project = get_object_or_404(Project, slug=slug)
    if request.user.is_authenticated:
        context_dic['authenticated'] = True

    if request.method == 'POST' and request.user.is_authenticated:
        form = DonationForm(data=request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.date = timezone.now()
            f.user_id = request.user.id
            f.project_id = project.id
            f.save()
            donation = form.instance
            updatedDonations = project.donations + donation.amount
            Project.objects.filter(id=project.id).update(donations=updatedDonations)
            return HttpResponseRedirect(reverse('GitQuid:viewProject', kwargs={'slug': slug}))
    else:
        context_dic['project'] = project
        context_dic['leftToGoal'] = max(0, project.goal - project.donations)
        context_dic['percentCollected'] = round(project.donations / project.goal * 100, 2)
        # show donations are not implemented yet
        context_dic['donations'] = Donation.objects.filter(project=project)
        context_dic['form'] = DonationForm()
        if request.user.is_authenticated and request.user == project.user:
            context_dic['author'] = True
        return render(request, 'GitQuid/viewProject.html', context_dic)


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()
            login(request, user)

            # Update our variable to indicate that the template
            #  registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            #  Print problems to the terminal.
            print(user_form.errors, profile_form.errors)

    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        #  These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    # Render the template depending on the context.
    return render(request, 'GitQuid/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


# renders user's account
def account(request, slug):
    context_dic = {'accUser': None, 'curUser': request.user}
    au = get_object_or_404(UserProfile, slug=slug)
    if au.user:
        projects_list = Project.objects.filter(user=au.user)
        context_dic['projects_list'] = projects_list
    context_dic['accUser'] = au.user
    return render(request, 'GitQuid/account.html', context_dic)


#
#
#
#
# Use the login_required() decorator to ensure only those logged in can
# access the view.
@login_required()
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homeproject.
    return HttpResponseRedirect(reverse('index'))


#
#
#

@login_required()
def editProfile(request, slug):
    # if user who is not logged in is typing using url which would edit another user's profile
    if request.user.userprofile.slug != slug:
        print("Redirecting to view account as this not belongs to you")  # rip my london at this point aylamo
        return HttpResponseRedirect(
            reverse('GitQuid:account', kwargs={'slug': request.user.userprofile.slug}))

    if request.method == 'POST':

        form = EditProfileForm(data=request.POST, instance=request.user)
        otherform = EditRestForm(data=request.POST, instance=request.user.userprofile)

        if form.is_valid() and otherform.is_valid():
            form.save()
            otherform.save()
            return HttpResponseRedirect(
                reverse('GitQuid:account', kwargs={'slug': request.user.userprofile.slug}))

    else:
        form = EditProfileForm(instance=request.user)
        otherform = EditRestForm(instance=request.user.userprofile)
        context_dict = {'form': form, 'otherform': otherform}
        return render(request, 'GitQuid/editProfile.html', context_dict)


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
