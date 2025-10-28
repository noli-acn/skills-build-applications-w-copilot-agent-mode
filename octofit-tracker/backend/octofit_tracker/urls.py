"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    UserListCreateView, UserDetailView,
    TeamListCreateView, TeamDetailView,
    ActivityListCreateView, ActivityDetailView,
    LeaderboardListCreateView, LeaderboardDetailView,
    WorkoutListCreateView, WorkoutDetailView
)
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': request.build_absolute_uri('/users/'),
        'teams': request.build_absolute_uri('/teams/'),
        'activities': request.build_absolute_uri('/activities/'),
        'leaderboard': request.build_absolute_uri('/leaderboard/'),
        'workouts': request.build_absolute_uri('/workouts/'),
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('teams/', TeamListCreateView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('activities/', ActivityListCreateView.as_view(), name='activity-list-create'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('leaderboard/', LeaderboardListCreateView.as_view(), name='leaderboard-list-create'),
    path('leaderboard/<int:pk>/', LeaderboardDetailView.as_view(), name='leaderboard-detail'),
    path('workouts/', WorkoutListCreateView.as_view(), name='workout-list-create'),
    path('workouts/<int:pk>/', WorkoutDetailView.as_view(), name='workout-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = [
    path('admin/', admin.site.urls),
]
