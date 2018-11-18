from django.shortcuts import render
from django.views.generic import TemplateView
from search.forms import HomeForm2
import requests
from bs4 import BeautifulSoup


class HomeView(TemplateView):
    template_name = 'search/search.html'

    def get(self, request):
        #template_name = 'search/search.html'
        form = HomeForm2()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm2(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            data = []
            query = text
            results = self.scrape_google(query, 100, "en")
            for result in results:
                data.append(result)

            args2 = {'form': form, 'text': data[0]['description']}
            return render(request, self.template_name, args2)



    def fetch_results(self, search_term, number_results, language_code):
        USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        assert isinstance(search_term, str), 'Search term must be a string'
        assert isinstance(number_results, int), 'Number of results must be an integer'

        temp = search_term.split(" ")
        escaped_search_term = []
        for index in range(len(temp)):
            if temp[index] == "":
                pass
            else:
                escaped_search_term.append(temp[index])
        print(escaped_search_term)
        escaped_search_term = "+".join(escaped_search_term)
        print(escaped_search_term)

        google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
        response = requests.get(google_url, headers=USER_AGENT)
        response.raise_for_status()
        return search_term, response.text


    def parse_results(self, html, keyword):
        soup = BeautifulSoup(html, 'html.parser')

        found_results = []
        rank = 1
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            link = result.find('a', href=True)
            title = result.find('h3', attrs={'class': 'r'})
            description = result.find('span', attrs={'class': 'st'})
            if link and title:
                link = link['href']
                title = title.get_text()
                if description:
                    description = description.get_text()
                    if link != '#':
                        found_results.append({'keyword': keyword, 'rank': rank, 'title': title, 'description': description})
                        rank += 1
        return found_results

    def scrape_google(self, search_term, number_results, language_code):
        try:
            keyword, html = self.fetch_results(search_term, number_results, language_code)
            results = self.parse_results(html, keyword)
            return results
        except AssertionError:
            raise Exception("Incorrect arguments parsed to function")
        except requests.HTTPError:
            raise Exception("You appear to have been blocked by Google")
        except requests.RequestException:
            raise Exception("Appears to be an issue with your connection")

obj = HomeView()
