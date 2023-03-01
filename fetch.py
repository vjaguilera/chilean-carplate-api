import requests

# RUN curl commmand to extract HTML


def fetchHTML(plate: str, save_file=False) -> str:
    url = 'https://www.patentechile.com/resultados'
    headers = {
        'authority': 'www.patentechile.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.patentechile.com',
        'referer': 'https://www.patentechile.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    raw_data = f'frmTerm={plate}&frmOpcion=vehiculo'

    print("FETCHING URL ----")

    resp = requests.post(
        url=url,
        headers=headers,
        data=raw_data
    )

    if (resp.status_code == 200 and save_file):
        with open("response.html", "w") as f:
            f.write(resp.text)

    return resp.text
