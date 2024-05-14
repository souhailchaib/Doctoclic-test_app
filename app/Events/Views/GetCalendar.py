from django.views.generic import TemplateView


class GetCalendar(TemplateView):

    template_name = "pages/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["parent"] = ""
        context["segment"] = "calendar"
        return context
