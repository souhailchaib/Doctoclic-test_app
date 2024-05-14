from django.contrib import admin
from django.urls import include, path

from app import views

from app.routing import websocket_urlpatterns


from app.Events.Views.GetCalendar import GetCalendar
from app.Events.Views.GetEvents import GetEvents
from app.Events.Views.GetEvent import GetEvent
from app.Events.Views.DeleteEvent import DeleteEvent
from app.Events.Views.SaveEvent import SaveEvent
from app.Events.Views.UpdateEvent import UpdateEvent
from app.Events.Views.GetClientsName import GetClientsName

from app.Events.Views.CalendarEventListCreate import CalendarEventListCreate

from app.Clients.Views.ClientListView import ClientListView
from app.Clients.Views.GetClient import GetCLient
from app.Clients.Views.CreateClient import CreateClient
from app.Clients.Views.UpdateClient import UpdateClient
from app.Clients.Views.DeleteClient import DeleteClient


urlpatterns = [
    path("get_events/", GetEvents.as_view(), name="get_events"),
    path("calendar/get_events/", CalendarEventListCreate.as_view(), name="get_events"),
    path("calendar/", GetCalendar.as_view(), name="examples_calendar"),
    path("calendar/get_client/", GetClientsName.as_view(), name="calendar_client"),
    path("get_event/", GetEvent.as_view(), name="get_event"),
    path("save_event/", SaveEvent.as_view(), name="save"),
    path("delete_event/", DeleteEvent.as_view(), name="delete_event"),
    path("update_event/", UpdateEvent.as_view(), name="update_event"),
    path("", views.UserLoginView.as_view(), name="login"),
    path("admin/", admin.site.urls),
    path("accounts/register/", views.register, name="register"),
    # path('login/', views.UserLoginView.as_view(), name='login'),
    path("client_list/", ClientListView.as_view(), name="client_list"),
    path("create/", CreateClient.as_view(), name="create_client"),
    path("client_list/get_client/", GetCLient.as_view(), name="get_client"),
    path("update/<int:client_id>/", UpdateClient.as_view(), name="update_client"),
    path("delete/<int:client_id>/", DeleteClient.as_view(), name="delete_client"),
    path("accounts/logout/", views.user_logout_view, name="logout"),
    path("dashboard-v2/", views.index2, name="dashboardv2"),
    path("dashboard-v3/", views.index3, name="dashboardv3"),
    path("widgets/", views.widgets, name="widgets"),
    path("profile/", views.profile, name="profile"),
    # path('test_app/', include('test_app.urls')),  # Include your regular Django app URLs
    # path('ws/', include('routing.websocket_urlpatterns')),
]
