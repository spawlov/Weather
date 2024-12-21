import requests


def get_weather_report(place: str) -> str:
    url = f"https://wttr.in/{place}"
    payload = {
        "nTqM": "",
        "lang": "ru",
    }
    response = requests.get(
        url=url,
        params=payload,
        timeout=30,
    )
    response.raise_for_status()
    return response.text


def main(places: list[str]) -> None:
    for place in places:
        print(get_weather_report(place))  # noqa


if __name__ == "__main__":
    main(["Лондон", "Шереметьево", "Череповец"])
