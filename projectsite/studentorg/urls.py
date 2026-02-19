from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Organization
from .forms import OrganizationForm

class OrganizationListView(ListView):
    model = Organization
    template_name = "organization_list.html"
    context_object_name = "organizations"
    paginate_by = 10

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "organization_form.html"
    success_url = reverse_lazy("org_list")

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "organization_form.html"
    success_url = reverse_lazy("org_list")

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "organization_confirm_delete.html"
    success_url = reverse_lazy("org_list")