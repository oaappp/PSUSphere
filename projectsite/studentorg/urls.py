from django.urls import path
from .views import (
    OrganizationListView, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    OrgMemberListView, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView,
    CollegeListView, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
    ProgramListView, ProgramCreateView, ProgramUpdateView, ProgramDeleteView,
)

urlpatterns = [
    # Organizations
    path("organization_list/", OrganizationListView.as_view(), name="organization-list"),
    path("organization_list/add/", OrganizationCreateView.as_view(), name="organization-add"),
    path("organization_list/<int:pk>/", OrganizationUpdateView.as_view(), name="organization-update"),
    path("organization_list/<int:pk>/delete/", OrganizationDeleteView.as_view(), name="organization-delete"),

    # Students
    path("students/", StudentListView.as_view(), name="student-list"),
    path("students/add/", StudentCreateView.as_view(), name="student-add"),
    path("students/<int:pk>/", StudentUpdateView.as_view(), name="student-update"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student-delete"),

    # Org Members
    path("members/", OrgMemberListView.as_view(), name="member-list"),
    path("members/add/", OrgMemberCreateView.as_view(), name="member-add"),
    path("members/<int:pk>/", OrgMemberUpdateView.as_view(), name="member-update"),
    path("members/<int:pk>/delete/", OrgMemberDeleteView.as_view(), name="member-delete"),

    # Colleges
    path("colleges/", CollegeListView.as_view(), name="college-list"),
    path("colleges/add/", CollegeCreateView.as_view(), name="college-add"),
    path("colleges/<int:pk>/", CollegeUpdateView.as_view(), name="college-update"),
    path("colleges/<int:pk>/delete/", CollegeDeleteView.as_view(), name="college-delete"),

    # Programs
    path("programs/", ProgramListView.as_view(), name="program-list"),
    path("programs/add/", ProgramCreateView.as_view(), name="program-add"),
    path("programs/<int:pk>/", ProgramUpdateView.as_view(), name="program-update"),
    path("programs/<int:pk>/delete/", ProgramDeleteView.as_view(), name="program-delete"),
]