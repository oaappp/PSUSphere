from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, CreateView, UpdateView, DeleteView
)

from .models import Organization, Student, OrgMember, College, Program
from .forms import OrganizationForm, StudentForm, OrgMemberForm, CollegeForm, ProgramForm


class HomePageView(TemplateView):
    template_name = "home.html"


# ===================== ORGANIZATION CRUD + SEARCH =====================
class OrganizationListView(ListView):
    model = Organization
    template_name = "org_list.html"
    context_object_name = "organizations"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related("college")
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q) |
                Q(college__college_name__icontains=q)
            )
        return qs


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "org_del.html"
    success_url = reverse_lazy("organization-list")


# ===================== STUDENT CRUD + SEARCH =====================
class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related("program", "program__college")
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(
                Q(student_id__icontains=q) |
                Q(lastname__icontains=q) |
                Q(firstname__icontains=q) |
                Q(middlename__icontains=q) |
                Q(program__prog_name__icontains=q) |
                Q(program__college__college_name__icontains=q)
            )
        return qs


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student-list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student-list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_del.html"
    success_url = reverse_lazy("student-list")


# ===================== ORGMEMBER CRUD + SEARCH =====================
class OrgMemberListView(ListView):
    model = OrgMember
    template_name = "member_list.html"
    context_object_name = "members"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related(
            "student", "student__program", "organization"
        )
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(
                Q(student__student_id__icontains=q) |
                Q(student__lastname__icontains=q) |
                Q(student__firstname__icontains=q) |
                Q(organization__name__icontains=q)
            )
        return qs


class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "member_form.html"
    success_url = reverse_lazy("member-list")


class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "member_form.html"
    success_url = reverse_lazy("member-list")


class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = "member_del.html"
    success_url = reverse_lazy("member-list")


# ===================== COLLEGE CRUD + SEARCH =====================
class CollegeListView(ListView):
    model = College
    template_name = "college_list.html"
    context_object_name = "colleges"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(college_name__icontains=q)
        return qs


class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")


class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")


class CollegeDeleteView(DeleteView):
    model = College
    template_name = "college_del.html"
    success_url = reverse_lazy("college-list")


# ===================== PROGRAM CRUD + SEARCH =====================
class ProgramListView(ListView):
    model = Program
    template_name = "program_list.html"
    context_object_name = "programs"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related("college")
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(
                Q(prog_name__icontains=q) |
                Q(college__college_name__icontains=q)
            )
        return qs


class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program-list")


class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program-list")


class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "program_del.html"
    success_url = reverse_lazy("program-list")