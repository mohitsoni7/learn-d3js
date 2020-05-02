from django.shortcuts import render
from django.views import View


class VisualHome(View):
    template_name = 'visualisationhome.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class FirstVisual(View):
    template_name = 'firstvisual.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class BasicStaticChartVisual(View):
    template_name = 'basic-static-chart.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class BasicShapesVisual(View):
    template_name = 'basic-shapes.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
