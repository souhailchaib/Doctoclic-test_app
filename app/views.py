from django.shortcuts import render, redirect
from .forms import LoginForm, UserPasswordResetForm
from django.contrib.auth import logout
from admin_adminlte.forms import LoginForm, RegistrationForm
from django.contrib.auth import views as auth_views
from django.shortcuts import render


def user_logout_view(request):
    logout(request)
    return redirect("/")


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = "accounts/forgot-password.html"
    form_class = UserPasswordResetForm


class UserLoginView(auth_views.LoginView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"


# pages
def index(request):
    context = {"parent": "dashboard", "segment": "dashboardv1"}
    return render(request, "pages/index.html", context)


def index2(request):
    context = {"parent": "dashboard", "segment": "dashboardv2"}
    return render(request, "pages/index2.html", context)


def index3(request):
    context = {"parent": "dashboard", "segment": "dashboardv3"}
    return render(request, "pages/index.html", context)


def widgets(request):
    context = {"parent": "", "segment": "widgets"}
    return render(request, "pages/widgets.html", context)


def profile(request):
    context = {"parent": "pages", "segment": "profile"}
    return render(request, "pages/examples/profile.html", context)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Account created successfully!")
            return redirect("/accounts/login/")
        else:
            print("Registration failed!")
    else:
        form = RegistrationForm()

    context = {"form": form}
    return render(request, "accounts/register.html", context)


# def save_event(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         start_date_str = request.POST.get('start')
#         end_date_str = request.POST.get('end')
#         all_day_str = request.POST.get('allDay')

#         # Parse the datetime strings into datetime objects
#         start_date = parse_datetime(start_date_str)
#         end_date = parse_datetime(end_date_str) if end_date_str else None

#         # Convert 'true' and 'false' strings to boolean values
#         all_day = all_day_str.lower() == 'true'

#         # Create a new event
#         new_event = CalendarEvent.objects.create(
#             title=title,
#             start_date=start_date,
#             end_date=end_date,
#             all_day=all_day
#         )

#         # Return the ID of the newly created event in the response
#         return JsonResponse({'success': True, 'event_id': new_event.id})
#     else:
#         return JsonResponse({'success': False, 'error': 'Invalid request method'})


# def update_event(request):
#     if request.method == 'POST':
#         event_id = request.POST.get('event_id')
#         title = request.POST.get('title')
#         start_date_str = request.POST.get('start')
#         end_date_str = request.POST.get('end')
#         all_day_str = request.POST.get('allDay')

#         # Parse the datetime strings into datetime objects
#         start_date = parse_datetime(start_date_str)
#         end_date = parse_datetime(end_date_str) if end_date_str else None

#         # Convert 'true' and 'false' strings to boolean values
#         all_day = all_day_str.lower() == 'true'

#         try:
#             event = CalendarEvent.objects.get(id=event_id)
#             event.title = title
#             event.start_date = start_date
#             event.end_date = end_date
#             event.all_day = all_day
#             event.save()
#             return JsonResponse({'success': True})
#         except CalendarEvent.DoesNotExist:
#             return JsonResponse({'success': False, 'error': 'Event not found'})
#     return JsonResponse({'success': False, 'error': 'Invalid request method'})
