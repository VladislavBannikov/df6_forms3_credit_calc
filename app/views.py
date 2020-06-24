from django.shortcuts import render
from django.views import View

from .forms import CalcForm


class CalcView(View):
    form_class = CalcForm
    template_name = "app/calc.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        context = {
            'form': form
        }
        if form.is_valid():
            initial_fee = form.cleaned_data.get("initial_fee")
            rate = form.cleaned_data.get("rate")
            months_count = form.cleaned_data.get("months_count")

            result = (initial_fee + initial_fee * rate) / months_count
            common_result = result * months_count
            context.update({
                'result': result,
                'common_result': common_result,
            })

        return render(request, self.template_name, context)
