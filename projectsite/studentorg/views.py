from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    TemplateView, ListView, CreateView, UpdateView, DeleteView
)

from .models import Organization, Student, OrgMember, College, Program
from .forms import OrganizationForm, StudentForm, OrgMemberForm, CollegeForm, ProgramForm


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_students"] = Student.objects.count()
        context["total_organizations"] = Organization.objects.count()
        context["total_programs"] = Program.objects.count()

        today = timezone.now().date()
        context["students_joined_this_year"] = (
            OrgMember.objects.filter(date_joined__year=today.year)
            .values("student")
            .distinct()
            .count()
        )
        return context


# ===================== ORGANIZATION CRUD + SEARCH + SORT =====================
class OrganizationListView(LoginRequiredMixin, ListView):
    model = Organization
    template_name = "org_list.html"
    context_object_name = "organizations"
    paginate_by = 10

    # SORTING (Exercise 5 - static)
    ordering = ["college__college_name", "name"]

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


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationUpdateView(LoginRequiredMixin, UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organization
    template_name = "org_del.html"
    success_url = reverse_lazy("organization-list")


# ===================== STUDENT CRUD + SEARCH =====================
class StudentListView(LoginRequiredMixin, ListView):
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


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student-list")


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student-list")


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = "student_del.html"
    success_url = reverse_lazy("student-list")


# ===================== ORGMEMBER CRUD + SEARCH + SORT =====================
class OrgMemberListView(LoginRequiredMixin, ListView):
    model = OrgMember
    template_name = "member_list.html"
    context_object_name = "members"
    paginate_by = 10

    # SORTING (Exercise 5)
    ordering = ["student__lastname", "student__firstname", "-date_joined"]

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


class OrgMemberCreateView(LoginRequiredMixin, CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "member_form.html"
    success_url = reverse_lazy("member-list")


class OrgMemberUpdateView(LoginRequiredMixin, UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "member_form.html"
    success_url = reverse_lazy("member-list")


class OrgMemberDeleteView(LoginRequiredMixin, DeleteView):
    model = OrgMember
    template_name = "member_del.html"
    success_url = reverse_lazy("member-list")


# ===================== COLLEGE CRUD + SEARCH =====================
class CollegeListView(LoginRequiredMixin, ListView):
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


class CollegeCreateView(LoginRequiredMixin, CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")


class CollegeUpdateView(LoginRequiredMixin, UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")


class CollegeDeleteView(LoginRequiredMixin, DeleteView):
    model = College
    template_name = "college_del.html"
    success_url = reverse_lazy("college-list")


# ===================== PROGRAM CRUD + SEARCH + DYNAMIC SORT =====================
class ProgramListView(LoginRequiredMixin, ListView):
    model = Program
    template_name = "program_list.html"
    context_object_name = "programs"
    paginate_by = 10

    # SORTING (Exercise 5 - dynamic)
    def get_ordering(self):
        allowed = ["prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "prog_name"

    def get_queryset(self):
        qs = super().get_queryset().select_related("college")
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(
                Q(prog_name__icontains=q) |
                Q(college__college_name__icontains=q)
            )
        return qs


class ProgramCreateView(LoginRequiredMixin, CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program-list")


class ProgramUpdateView(LoginRequiredMixin, UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program-list")


class ProgramDeleteView(LoginRequiredMixin, DeleteView):
    model = Program
    template_name = "program_del.html"
    success_url = reverse_lazy("program-list")