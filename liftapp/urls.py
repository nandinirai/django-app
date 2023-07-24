from django.urls import path

from .views import ElevatorView, RequestView

urlpatterns = [
    path("elevators/", ElevatorView.as_view()),
    path("elevators/<int:elevator_id>/requests/", RequestView.as_view()),
    path(
        "elevators/<int:elevator_id>/requests/add/",
        RequestView.as_view(),
        name="add_request",
    ),
    path(
        "elevators/<int:elevator_id>/next_destination/",
        ElevatorView.as_view(),
        name="next_destination",
    ),
    path(
        "elevators/<int:elevator_id>/is_moving/",
        ElevatorView.as_view(),
        name="is_moving",
    ),
    path(
        "elevators/<int:elevator_id>/door/",
        ElevatorView.as_view(),
        name="door",
    ),
]
