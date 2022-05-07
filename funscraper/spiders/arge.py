import scrapy

from scrapy import Request
import requests

import json

class ArgeSpider(scrapy.Spider):
    name = 'arge'
    # allowed_domains = ['https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs?berufsfeld=Softwareentwicklung%20und%20Programmierung']
    # start_urls = ['http://https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs?berufsfeld=Softwareentwicklung%20und%20Programmierung/']






    def start_requests(self):


        cookies = {
            'cookie_consent': 'accepted',
            'personalization_consent': 'accepted',
            '_pk_id.1000.cfae': '764b31b90604b5d2.1650804217.',
            '_pk_id.3.cfae': '05fd0d4925f5c2ee.1650804217.',
            'chatbotFeatures': '%5B%22enableStartseiteFreeText%22%5D',
            'chatbotAlertText': '%5B%22StartSeiteBot%22%5D',
            '_pk_id.35.cfae': 'd96c80056e3ef738.1650804232.',
            'LANG': 'de',
            'CSRF-TOKEN': '031941d8-628b-4c9e-9d9e-cd829435b246',
            '_pk_ses.35.cfae': '1',
            'OAMAuthnHintCookie': '0@1650807911',
            'OAMAuthnCookie_rest.arbeitsagentur.de_443': '0bad316624f50bca11209a940452358f29c037f5%7El2DrpStb6PBUHjolQqwFUBwvvm8MEC6o3O868EBODWhWq4DMXTN6i%2BOJw%2Fv6y%2FfXQ4lX2YyHgeimWgvhObaY3qfxiwkT5ufeQWmXPLn64c%2Fz58Qqg8mYRHZ%2BOXFQt6LN9XbPaaV1T3pE8vWpZOzMyiLY53uBB2JPfKh9VqudBs1XqDUPqZHfhyto1BDuCKk9PN56Wc0esPuxtUWBYdtjh%2BcSHHWIjtWFGuliBfGuFBhMA2KRbRaeBU0KRWnQl%2B3k%2BpyBJXOjha3M5Qt%2FLdXuilRHwNDt7zJHODdOucADlM%2FcoMii%2FK6x0l2zjP%2F8xvBkiAv%2Bz7n4QTHXN%2B90x9JJi3eDtIK4%2Faudh9wF7MbrRY%2FsmkFhV0M7rz%2Fhu%2BIOCKJVf%2B6pLbteDb5msRt1plI2Pw%3D%3D',
            'rest': '024dae17b4-4300-45JpzZ44x8PrPFwRGXGq6XJWoiZZi2haTjYDeNAouvrKo69RL1HVrA-J-w04Hlayb7U08',
            'JSESSIONID': '4769EEE4B2DDE8A34C9A0ED7100F0981',
        }

        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'Accept': 'application/json, text/plain, */*',
            'OAuthAccessToken': 'eyJhbGciOiJIUzUxMiJ9.eyAic3ViIjogIm05RGg2RVByZWlYckMrbE9aSUpLQ3paVXlSWT0iLCAiaXNzIjogIk9BRyIsICJpYXQiOiAxNjUwODA5NjA4LCAiZXhwIjogMS42NTA4MTMyMDhFOSwgImF1ZCI6IFsgIk9BRyIgXSwgIm9hdXRoLnNjb3BlcyI6ICJhcG9rX21ldGFzdWdnZXN0LCBqb2Jib2Vyc2Vfc3VnZ2VzdC1zZXJ2aWNlLCBhYXMsIGpvYmJvZXJzZV9rYXRhbG9nZS1zZXJ2aWNlLCBqb2Jib2Vyc2Vfam9ic3VjaGUtc2VydmljZSwgaGVhZGVyZm9vdGVyX2hmLCBhcG9rX2hmLCBqb2Jib2Vyc2VfcHJvZmlsLXNlcnZpY2UiLCAib2F1dGguY2xpZW50X2lkIjogImRjZGVhY2JkLTJiNjItNDI2MS1hMWZhLWQ3MjAyYjU3OTg0OCIgfQ.g1VdV0SEhRuazUcjoSaIYJBIEHZ7qr5kI_FkHIxDAvePSaoMdSelaJiveJ2Ln-szaL_-mL21zT0GT-0zRMgQGA',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
            'Correlation-ID': 'ba79da0b-c7c8-8446-5874-42c9e70611ee',
            'sec-ch-ua-platform': '"Linux"',
            'Origin': 'https://www.arbeitsagentur.de',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Language': 'en-US,en;q=0.9',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'cookie_consent=accepted; personalization_consent=accepted; _pk_id.1000.cfae=764b31b90604b5d2.1650804217.; _pk_id.3.cfae=05fd0d4925f5c2ee.1650804217.; chatbotFeatures=%5B%22enableStartseiteFreeText%22%5D; chatbotAlertText=%5B%22StartSeiteBot%22%5D; _pk_id.35.cfae=d96c80056e3ef738.1650804232.; LANG=de; CSRF-TOKEN=031941d8-628b-4c9e-9d9e-cd829435b246; _pk_ses.35.cfae=1; OAMAuthnHintCookie=0@1650807911; OAMAuthnCookie_rest.arbeitsagentur.de_443=0bad316624f50bca11209a940452358f29c037f5%7El2DrpStb6PBUHjolQqwFUBwvvm8MEC6o3O868EBODWhWq4DMXTN6i%2BOJw%2Fv6y%2FfXQ4lX2YyHgeimWgvhObaY3qfxiwkT5ufeQWmXPLn64c%2Fz58Qqg8mYRHZ%2BOXFQt6LN9XbPaaV1T3pE8vWpZOzMyiLY53uBB2JPfKh9VqudBs1XqDUPqZHfhyto1BDuCKk9PN56Wc0esPuxtUWBYdtjh%2BcSHHWIjtWFGuliBfGuFBhMA2KRbRaeBU0KRWnQl%2B3k%2BpyBJXOjha3M5Qt%2FLdXuilRHwNDt7zJHODdOucADlM%2FcoMii%2FK6x0l2zjP%2F8xvBkiAv%2Bz7n4QTHXN%2B90x9JJi3eDtIK4%2Faudh9wF7MbrRY%2FsmkFhV0M7rz%2Fhu%2BIOCKJVf%2B6pLbteDb5msRt1plI2Pw%3D%3D; rest=024dae17b4-4300-45JpzZ44x8PrPFwRGXGq6XJWoiZZi2haTjYDeNAouvrKo69RL1HVrA-J-w04Hlayb7U08; JSESSIONID=4769EEE4B2DDE8A34C9A0ED7100F0981',
        }

        params = {
            'berufsfeld': 'Softwareentwicklung und Programmierung',
            'angebotsart': '1',
            'page': '1',
            'size': '25',
            'pav': 'false',
        }

        r = requests.get('https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs', params=params,
                                cookies=cookies, headers=headers)











        # pretty_json = json.loads(r.text)
        # print(json.dumps(pretty_json, indent=2))