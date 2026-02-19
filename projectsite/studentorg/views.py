from django.views.generic import ListView
from studentorg.models import Organization

class HomePageView(ListView):
    model = Organization
    template_name = "home.html"
    context_object_name = "organizations"
    paginate_by = 10