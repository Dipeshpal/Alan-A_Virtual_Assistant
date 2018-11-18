from django.shortcuts import render
from django.views.generic import TemplateView
from reminder.forms import HomeForm4


class HomeView(TemplateView):
    template_name = 'reminder/reminder.html'

    def get(self, request):
        form = HomeForm4()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm4(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            message = form.cleaned_data['message']
            file = open("Reminder.txt", 'a')
            file.write("\n" + date + " " + time + " " + message + "\n")
            file.close()
            args3 = {'form': form, 'successful': "Your reminder has been successfully created"}
            return render(request, self.template_name, args3)
