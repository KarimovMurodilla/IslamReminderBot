from bs4 import BeautifulSoup as bs
import requests


url = "https://islom.uz"

agent = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def times():
    r = requests.get(url, headers=agent)
    soup = bs(r.content, 'html.parser')

    h = soup.findAll(class_='cricle')
    hour = soup.findAll(class_='p_clock')
    # name = soup.findAll(class_='p_v')


    DATA = []


    for h in (hour):
        result = f"{h.text}"
        DATA.append(result)

    return {DATA[0]: "Bomdod", DATA[1]: "Quyosh", DATA[2]: "Peshin", DATA[3]: "Asr", DATA[4]: "Shom", DATA[5]: "Xufton"}