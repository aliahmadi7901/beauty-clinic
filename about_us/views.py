from django.shortcuts import render
from django.views.generic import View

from about_us.models import AboutUs, GrowthHistory, Advantages


class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        about_us: AboutUs = AboutUs.objects.last()
        growth_history: GrowthHistory = GrowthHistory.objects.all()[:3]
        advantages = Advantages.objects.last()
        context = {'about_us': about_us, 'growth_history': growth_history, 'advantages': advantages}
        return render(request, 'about_us/about_us.html', context)
