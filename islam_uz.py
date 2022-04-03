import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs

from loader import urls, agent
from app.data import region_ids, uz_countries

NAMAZ_TIMES = {}

class IslamUz:
    def get_times(self) -> list:
        """
        O'zbekistondagi deyarli barcha Shahar/Viloyat/Qishloq larning
        namoz vaqtlarini ro'yhat ko'rinishida qaytaruvchi metod. 
        !!! Namoz vaqtlari islom.uz saytidan dan olindadi.
        """
        DATA = []

        for i in region_ids:     
            r = requests.get(urls[0]+i, headers=agent)
            soup = bs(r.content, 'html.parser')

            hour = soup.findAll(class_='cricle')
            hours = soup.findAll(class_='p_clock')

            for hour in (hours):
                result = f"{hour.text}"
                DATA.append(result)

        return DATA

    def get_country_names(self, url) -> list:
        """
        O'zbekiston ichidagi mintaqalarni 
        ro'yhat ko'rinishida qaytaruvchi metod.
        !!! Mintaqalar ro'yhati islom.uz saytidan dan olindadi.
        """
        r = requests.get(url, headers=agent)
        soup = bs(r.content, 'html.parser')
        h = soup.findAll(class_='custom-select')
        return [i.text.lower() for i in h[0].findAll('option')]

    def get_country_times(self) -> dict:
        global NAMAZ_TIMES
        NAMAZ_TIMES = {}

        times = IslamUz().get_times()

        n = 0
        for i in uz_countries:
            NAMAZ_TIMES[i] = []
            for k in range(len(times)):
                if len(NAMAZ_TIMES[i]) >= 6:
                    break

                else:
                    NAMAZ_TIMES[i].append(times[n])
                    n += 1


if not NAMAZ_TIMES:
    namaz_times = IslamUz()
    namaz_times.get_country_times()