from django.shortcuts import render
from django.views.generic import View, ListView

from about_us.models import AboutUs, GrowthHistory, Advantages, Questions
from team.models import Doctor


class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        about_us: AboutUs = AboutUs.objects.last()
        growth_history: GrowthHistory = GrowthHistory.objects.all()[:3]
        advantages = Advantages.objects.last()
        doctors = Doctor.objects.order_by('?')[:3]
        context = {'about_us': about_us, 'growth_history': growth_history, 'advantages': advantages, 'doctors': doctors}
        return render(request, 'about_us/about_us.html', context)


class QuestionsView(ListView):
    model = Questions
    context_object_name = 'questions'
    template_name = 'about_us/questions.html'
