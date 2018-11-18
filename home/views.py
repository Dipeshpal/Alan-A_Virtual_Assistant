from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from home.weather import Weather
from home.remainder import rem_call



obj = Weather()
class HomeView(TemplateView, Weather):
    template_name = 'home/home.html'

    def get(self, request):
        template_name = 'search/search.html'
        form = HomeForm()

        ## Weather Forecast Start
        temp, city = obj.fun_weather()
        ## Reminder Start
        reminder_result = rem_call()
        args1 = {'form': form, 'temp': temp, 'city': city, 'reminder_result': reminder_result}
        return render(request, self.template_name, args1)
        ## Reminder Stop
        ##Weather ForeCasting Stop



    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']

            bot = ChatBot('Toto')
            bot.set_trainer(ListTrainer)
            while True:
                message = text
                if message.strip != 'Bye':
                    reply = bot.get_response(message)
                    args2 = {'form': form, 'text': reply}
                    return render(request, self.template_name, args2)
                    #print('TOTO : ', reply)
                    break
                if message.strip() == 'Bye':
                    print('TOTO : Bye')
                    break
