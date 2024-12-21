import urllib.parse

import requests


def get_weather_report(place: str) -> str:
    template_url = f"https://wttr.in/{place}?nTqM&lang=ru"
    encoded_place = urllib.parse.quote(place)
    url = template_url.replace("{place}", encoded_place)
    response = requests.get(
        url=url,
        timeout=30,
    )
    response.raise_for_status()
    return response.text


def main(places: list[str]) -> None:
    for place in places:
        print(get_weather_report(place))  # noqa


if __name__ == "__main__":
    main(["Лондон", "Шереметьево", "Череповец"])
